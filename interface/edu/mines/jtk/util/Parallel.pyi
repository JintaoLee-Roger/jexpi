from typing import overload
from edu.mines.jtk.mapping import *


class Parallel:
    """
    Utilities for parallel computing in loops over independent tasks.
    This class provides convenient methods for parallel processing of
    tasks that involve loops over indices, in which computations for
    different indices are independent.
    
    As a simple example, consider the following function that squares
    floats in one array and stores the results in a second array.
    <pre><code>
    static void sqr(float[] a, float[] b) {
    int n = a.length;
    for (int i=0; i&lt;n; ++i)
    b[i] = a[i]a[i];
    }
    </code></pre>
    A serial version of a similar function for 2D arrays is:
    <pre><code>
    static void sqrSerial(float[][] a, float[][] b)
    {
    int n = a.length;
    for (int i=0; i&lt;n; ++i) {
    sqr(a[i],b[i]);
    }
    </code></pre>
    Using this class, the parallel version for 2D arrays is:
    <pre><code>
    static void sqrParallel(final float[][] a, final float[][] b) {
    int n = a.length;
    Parallel.loop(n,new Parallel.LoopInt() {
    public void compute(int i) {
    sqr(a[i],b[i]);
    }
    });
    }
    </code></pre>
    In the parallel version, the method {@code compute} defined by the
    interface {@code LoopInt} will be called n times for different
    indices i in the range [0,n-1]. The order of indices is both
    indeterminant and irrelevant because the computation for each
    index i is independent. The arrays a and b are declared final
    as required for use in the implementation of {@code LoopInt}.
    
    Note: because the method {@code loop} and interface {@code LoopInt}
    are static members of this class, we can omit the class name prefix
    {@code Parallel} if we first import these names with
    <pre><code>
    import static edu.mines.jtk.util.Parallel.;
    </code></pre>
    A similar method facilitates tasks that reduce a sequence of indexed
    values to one or more values. For example, given the following method:
    <pre><code>
    static float sum(float[] a) {
    int n = a.length;
    float s = 0.0f;
    for (int i=0; i&lt;n; ++i)
    s += a[i];
    return s;
    }
    </code></pre>
    serial and parallel versions for 2D arrays may be written as:
    <pre><code>
    static float sumSerial(float[][] a) {
    int n = a.length;
    float s = 0.0f;
    for (int i=0; i&lt;n; ++i)
    s += sum(a[i]);
    return s;
    }
    </code></pre>
    and
    <pre><code>
    static float sumParallel(final float[][] a) {
    int n = a.length;
    return Parallel.reduce(n,new Parallel.ReduceInt&lt;Float&gt;() {
    public Float compute(int i) {
    return sum(a[i]);
    }
    public Float combine(Float s1, Float s2) {
    return s1+s2;
    }
    });
    }
    </code></pre>
    In the parallel version, we implement the interface {@code ReduceInt}
    with two methods, one to {@code compute} sums of array elements and
    another to {@code combine} two such sums together. The same pattern
    works for other reduce operations. For example, with similar functions
    we could compute minimum and maximum values (in a single reduce) for
    any indexed sequence of values.
    
    More general loops are supported, and are equivalent to the following
    serial code:
    <pre><code>
    for (int i=begin; i&lt;end; i+=step)
    // some computation that depends on i
    </code></pre>
    The methods loop and reduce require that begin is less than end and
    that step is positive. The requirement that begin is less than end
    ensures that reduce is always well-defined. The requirement that step
    is positive ensures that the loop terminates.
    
    Static methods loop and reduce submit tasks to a fork-join framework
    that maintains a pool of threads shared by all users of these methods.
    These methods recursively split tasks so that disjoint sets of indices
    are processed in parallel by different threads.
    
    In addition to the three loop parameters begin, end, and step, a
    fourth parameter chunk may be specified. This chunk parameter is
    a threshold for splitting tasks so that they can be performed in
    parallel. If a range of indices to be processed is smaller than
    the chunk size, or if too many tasks have already been queued for
    processing, then the indices are processed serially. Otherwise,
    the range is split into two parts for processing by new tasks. If
    specified, the chunk size is a lower bound; the number of indices
    processed serially will never be lower, but may be higher, than
    a specified chunk size. The default chunk size is one.
    
    The default chunk size is often sufficient, because the test for
    an excess number of queued tasks prevents tasks from being split
    needlessly. This test is especially useful when parallel loops are
    nested, as when looping over elements of multi-dimensional arrays.
    
    For example, an implementation of the method {@code sqrParallel} for
    3D arrays could simply call the 2D version listed above. Tasks will
    naturally tend to be split for outer loops, but not inner loops,
    thereby reducing overhead, time spent splitting and queueing tasks.
    
    Reference: A Java Fork/Join Framework, by Doug Lea, describes the
    framework used to implement this class. This framework will be part
    of JDK 7.
    """

    @overload
    @staticmethod
    def loop(self, end: int, body: LoopInt) -> None:
        """
        Performs a loop <code>for (int i=0; i&lt;end; ++i)</code>.
        
        Parameters
        -----------
        end : int
            the end index (not included) for the loop.
        body : LoopInt
            the loop body.
        """

    @overload
    @staticmethod
    def loop(self, begin: int, end: int, body: LoopInt) -> None:
        """
        Performs a loop <code>for (int i=begin; i&lt;end; ++i)</code>.
        
        Parameters
        -----------
        begin : int
            the begin index for the loop; must be less than end.
        end : int
            the end index (not included) for the loop.
        body : LoopInt
            the loop body.
        """

    @overload
    @staticmethod
    def loop(self, begin: int, end: int, step: int, body: LoopInt) -> None:
        """
        Performs a loop <code>for (int i=begin; i&lt;end; i+=step)</code>.
        
        Parameters
        -----------
        begin : int
            the begin index for the loop; must be less than end.
        end : int
            the end index (not included) for the loop.
        step : int
            the index increment; must be positive.
        body : LoopInt
            the loop body.
        """

    @overload
    @staticmethod
    def loop(self, begin: int, end: int, step: int, chunk: int,
             body: LoopInt) -> None:
        """
        Performs a loop <code>for (int i=begin; i&lt;end; i+=step)</code>.
        
        Parameters
        -----------
        begin : int
            the begin index for the loop; must be less than end.
        end : int
            the end index (not included) for the loop.
        step : int
            the index increment; must be positive.
        chunk : int
            the chunk size; must be positive.
        body : LoopInt
            the loop body.
        """

    @overload
    @staticmethod
    def reduce(self, end: int, body: ReduceInt) -> V:
        """
        Performs a reduce <code>for (int i=0; i&lt;end; ++i)</code>.
        
        Parameters
        -----------
        end : int
            the end index (not included) for the loop.
        body : ReduceInt
            the loop body.
        
        Returns
        --------
        output : V
            the computed value.
        """

    @overload
    @staticmethod
    def reduce(self, begin: int, end: int, body: ReduceInt) -> V:
        """
        Performs a reduce <code>for (int i=begin; i&lt;end; ++i)</code>.
        
        Parameters
        -----------
        begin : int
            the begin index for the loop; must be less than end.
        end : int
            the end index (not included) for the loop.
        body : ReduceInt
            the loop body.
        
        Returns
        --------
        output : V
            the computed value.
        """

    @overload
    @staticmethod
    def reduce(self, begin: int, end: int, step: int, body: ReduceInt) -> V:
        """
        Performs a reduce <code>for (int i=begin; i&lt;end; i+=step)</code>.
        
        Parameters
        -----------
        begin : int
            the begin index for the loop; must be less than end.
        end : int
            the end index (not included) for the loop.
        step : int
            the index increment; must be positive.
        body : ReduceInt
            the loop body.
        
        Returns
        --------
        output : V
            the computed value.
        """

    @overload
    @staticmethod
    def reduce(self, begin: int, end: int, step: int, chunk: int,
               body: ReduceInt) -> V:
        """
        Performs a reduce <code>for (int i=begin; i&lt;end; i+=step)</code>.
        
        Parameters
        -----------
        begin : int
            the begin index for the loop; must be less than end.
        end : int
            the end index (not included) for the loop.
        step : int
            the index increment; must be positive.
        chunk : int
            the chunk size; must be positive.
        body : ReduceInt
            the loop body.
        
        Returns
        --------
        output : V
            the computed value.
        """

    @staticmethod
    def setParallel(self, parallel: bool) -> None:
        """
        Enables or disables parallel processing by all methods of this class.
        By default, parallel processing is enabled. If disabled, all tasks
        will be executed on the current thread.
        
        <em>Setting this flag to false disables parallel processing for all
        users of this class.</em> This method should therefore be used for
        testing and benchmarking only.
        
        Parameters
        -----------
        parallel : bool
            true, for parallel processing; false, otherwise.
        """
