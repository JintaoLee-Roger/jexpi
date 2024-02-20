
from typing import overload
from edu.mines.jtk.mapping import *

class Sampling:
    """
    Sampling of one variable.
    
    Samplings are often used to represent independent variables for sampled 
    functions. They describe the values at which a function is sampled. For 
    efficiency, and to guarantee a unique mapping from sample value to 
    function value, we restrict samplings to be strictly increasing. In other
    words, no two samples have equal value, and sample values increase with 
    increasing sample index.
    
    Samplings are either uniform or non-uniform. Uniform samplings are
    represented by a sample count n, a sampling interval d, and a first
    sample value f. Non-uniform samplings are represented by an array of 
    sample values.
    
    All sample values are computed and stored in **double precision**. 
    This double precision can be especially important in uniform samplings, 
    where the sampling interval d and first sample value f may be used to
    compute values for thousands of samples, in loops like this one:
    <pre><code>
      int n = sampling.getCount();
      double d = sampling.getDelta();
      double f = sampling.getFirst();
      double v = f;
      for (int i=0; i&lt;n; ++i,v+=d) {
        // some calculation that uses the sample value v
      }
    </code></pre>
    In each iteration of the loop above, the sample value v is computed by 
    accumulating the sampling interval d. This computation is fast, but it 
    also yields rounding error that can grow quadratically with the number 
    of samples n. If v were computed in single (float) precision, then this 
    rounding error could exceed the sampling interval d for as few as 
    n=10,000 samples.
    
    If accumulating in double precision is insufficient, a more accurate 
    and more costly way to compute sample values is as follows:
    <pre><code>
      // ...
      double v = f;
      for (int i=0; i&lt;n; ++i,v=f+i*d) {
        // some calculation that uses the sample value v
      }
    </code></pre>
    With this computation of sample values, rounding errors can grow only 
    linearly with the number of samples n.
    
    Two samplings are considered equivalent if their sample values differ
    by no more than the **sampling tolerance**. This tolerance may be
    specified, as a fraction of the sampling interval, when a sampling is
    constructed. Alternatively, a default tolerance may be used. When
    comparing two samplings, the smaller of their tolerances is used.
    
    A sampling is immutable. New samplings can be constructed by applying
    various transformations (e.g., shifting) to an existing sampling, but
    an existing sampling cannot be changed. Therefore, multiple sampled
    functions can safely share the same sampling.
     *
    @author Dave Hale, Colorado School of Mines
    @version 2005.03.11
    """
    
    @overload
    def __init__(self, n: int) -> None:
        """
        Constructs a uniform sampling with specified count. The sampling 
        interval (delta) is 1.0, and the first sample value is 0.0.
        
        Parameters
        ----------
        n : int
            The description of int.
        """

    @overload
    def __init__(self, n: int, d: double, f: double) -> None:
        """
        Constructs a uniform sampling with specified parameters.
        
        Parameters
        ----------
        n : int
            the number (count) of samples; must be positive.
        d : double
            the sampling interval (delta); must be positive.
        f : double
            The description of double.
        """

    @overload
    def __init__(self, n: int, d: double, f: double, t: double) -> None:
        """
        Constructs a sampling with specified parameters.
        
        Parameters
        ----------
        n : int
            the number (count) of samples; must be positive.
        d : double
            the sampling interval (delta); must be positive.
        f : double
            the first sample value.
        t : double
            The description of double.
        """

    @overload
    def __init__(self, v: Double1D) -> None:
        """
        Constructs a sampling from the specified array of values. The values 
        must be strictly increasing.
        
        The constructed sampling may or may not be uniform, depending on the 
        specified values and default sampling tolerance. If uniform (to within 
        the default tolerance), then the array of values is discarded, and the 
        sampling is represented by the count, sampling interval, and first 
        sample value.
        
        Parameters
        ----------
        v : Double1D
            The description of Double1D.
        """

    @overload
    def __init__(self, v: Double1D, t: double) -> None:
        """
        Constructs a sampling from the specified array of values and tolerance.
        The values must be strictly increasing. 
        
        The constructed sampling may or may not be uniform, depending on the 
        specified values and tolerance. If uniform (to within the specified
        tolerance), then the array of values is discarded, and the sampling is 
        represented by the count, sampling interval, and first sample value.
        
        Parameters
        ----------
        v : Double1D
            the array of sampling values; must have non-zero length.
        t : double
            The description of double.
        """

    def getCount(self) -> int:
        """
        Gets the number of samples.
        
        Parameters
        ----------
        
        Returns
        -------
        output : int
            the number of samples.
        """

    def getDelta(self) -> double:
        """
        Gets the sampling interval. If not uniformly sampled, the sampling
        interval is the average difference between sample values.
        
        Parameters
        ----------
        
        Returns
        -------
        output : double
            the sampling interval; 1.0, if fewer than two samples.
        """

    def getFirst(self) -> double:
        """
        Gets the first sample value.
        
        Parameters
        ----------
        
        Returns
        -------
        output : double
            the first sample value.
        """

    def getLast(self) -> double:
        """
        Gets the last sample value.
        
        Parameters
        ----------
        
        Returns
        -------
        output : double
            the last sample value.
        """

    def getValue(self, i: int) -> double:
        """
        Gets the sample value with specified index.
        
        Parameters
        ----------
        i : int
            the index.
        
        Returns
        -------
        output : double
            the sample value.
        """

    def isUniform(self) -> bool:
        """
        Determines whether this sampling is uniform. A sampling is uniform 
        if its values can be computed, to within the sampling tolerance, by
        the expression v = f+i*d, for sampling indices i = 0, 1, ..., n-1.
        Samplings with only one sample are considered to be uniform.
        
        Note that, by this definition, samplings constructed with an array 
        of sample values may or may not be uniform.
        
        Parameters
        ----------
        
        Returns
        -------
        output : bool
            true, if uniform; false, otherwise.
        """

    def isEquivalentTo(self, s: Sampling) -> bool:
        """
        Determines whether this sampling is equivalent to the specified sampling.
        Two samplings are equivalent if each of their sample values differs by 
        no more than the sampling tolerance.
        
        Parameters
        ----------
        s : Sampling
            the sampling to compare to this sampling.
        
        Returns
        -------
        output : bool
            true, if equivalent; false, otherwise.
        """

    def isCompatible(self, s: Sampling) -> bool:
        """
        Determines whether this sampling is compatible with the specified sampling.
        Two samplings are incompatible if their ranges of sample values overlap, 
        but not all values in the overlapping parts are equivalent. Otherwise,
        they are compatible.
        
        Parameters
        ----------
        s : Sampling
            the sampling to compare to this sampling.
        
        Returns
        -------
        output : bool
            true, if compatible; false, otherwise.
        """

    def indexOf(self, x: double) -> int:
        """
        Returns the index of the sample with specified value. If this 
        sampling has a sample value that equals (to within the sampling 
        tolerance) the specified value, then this method returns the 
        index of that sample. Otherwise, this method returns -1.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : int
            the index of the matching sample; -1, if none.
        """

    def indexOfNearest(self, x: double) -> int:
        """
        Returns the index of the sample nearest to the specified value.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : int
            the index of the nearest sample.
        """

    def valueOfNearest(self, x: double) -> double:
        """
        Returns the value of the sample nearest to the specified value.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : double
            the value of the nearest sample.
        """

    @overload
    def isInBounds(self, i: int) -> bool:
        """
        Determines whether the specified index is in the bounds of this sampling.
        An index is in bounds if in the range [0,count-1] of the first and last
        sample indices.
        
        Parameters
        ----------
        i : int
            the index.
        
        Returns
        -------
        output : bool
            true, if in bounds; false, otherwise.
        """

    @overload
    def isInBounds(self, x: double) -> bool:
        """
        Determines whether the specified value is in the bounds of this sampling.
        A value is in bounds if in the range [first,last] defined by the first 
        and last sample values.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : bool
            true, if in bounds; false, otherwise.
        """

    def isInBoundsExtended(self, x: double) -> bool:
        """
        Determines whether the specified value is in the bounds of this sampling,
        which is assumed to be uniform. A value is in bounds if in the range
        [first-0.5*delta,last+0.5*delta] defined by the first and last sample 
        values and the sampling interval delta. In effect, this method extends
        the bounds of this sampling by one-half sample when testing the value.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : bool
            true, if in bounds; false, otherwise.
        """

    def getValueExtended(self, i: int) -> double:
        """
        Gets the value for the specified index, assuming uniform sampling.
        The index and the returned value need not be in the bounds of this 
        sampling, which must be uniform. That is, the specified index may be 
        less than zero or greater than or equal to the number of samples.
        
        Parameters
        ----------
        i : int
            the index.
        
        Returns
        -------
        output : double
            the value.
        """

    def indexOfNearestExtended(self, x: double) -> int:
        """
        Returns the index of the sample nearest the specified value, assuming 
        uniform sampling. The value and the returned index need not be in the 
        bounds of this sampling, which must be uniform. Specifically, the
        returned index may be less than zero or greater than or equal to the 
        number of samples.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : int
            the index of the sample nearest the value.
        """

    def valueOfNearestExtended(self, x: double) -> double:
        """
        Returns the value of the sample nearest to the specified value, 
        assuming uniform sampling. The specified and returned values need 
        not be in the bounds of this sampling, which must be uniform.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : double
            the value of the nearest sample.
        """

    def indexOfFloorExtended(self, x: double) -> int:
        """
        Returns the index of the floor of the specified value.
        The floor is the largest sampled value less than or equal to the 
        specified value. The value and the returned index need not be in 
        the bounds of this sampling, which must be uniform.
        Specifically, the returned index may be less than zero or greater 
        than or equal to the number of samples.
        
        Parameters
        ----------
        x : double
            the value.
        
        Returns
        -------
        output : int
            the index of the floor of the value.
        """

    def normalizedDifferenceExtended(self, x: double, i: int) -> double:
        """
        Returns the normalized difference between a specified value and 
        the sampled value for a specified index. Normalized difference is
        the difference (specified value minus sampled value) divided by 
        the sampling interval. The specified value and index not be in 
        the bounds of this sampling, which must be uniform.
        
        Parameters
        ----------
        x : double
            the value.
        i : int
            the index.
        
        Returns
        -------
        output : double
            the difference between a value and the sampled value.
        """

    def mergeWith(self, s: Sampling) -> Sampling:
        """
        Returns the union of this sampling with the specified sampling. This
        union is possible if and only if the two samplings are compatible.
        
        If the two samplings do not overlap, this method does not create
        samples within any gap that may exist between them. In other words,
        the number of samples in the sampling returned is exactly nt+ns-n, 
        where nt is the number of samples in this sampling, ns is the number 
        of samples in the specified sampling, and n is the number of samples 
        with equivalent values in any overlapping parts of the two samplings.
        If the samplings do not overlap, then n = 0. One consequence of this
        behavior is that the union of two uniform samplings with the same 
        sampling interval may be non-uniform.
        
        This method returns a new sampling; it does not modify this sampling.
        @see #overlapWith(Sampling)
        
        Parameters
        ----------
        s : Sampling
            the sampling to merge with this sampling.
        
        Returns
        -------
        output : Sampling
            the merged sampling; null, if no merge is possible.
        """

    def shift(self, s: double) -> Sampling:
        """
        Shifts this sampling.
        
        This method returns a new sampling; it does not modify this sampling.
        
        Parameters
        ----------
        s : double
            the value (shift) to add to this sampling's values.
        
        Returns
        -------
        output : Sampling
            the new sampling.
        """

    def prepend(self, m: int) -> Sampling:
        """
        Prepends samples to this sampling.
        If this sampling is not uniform, prepended sample values are computed 
        to preserve the average difference between adjacent sample values.
        
        This method returns a new sampling; it does not modify this sampling.
        
        Parameters
        ----------
        m : int
            the number of new samples prepended to this sampling.
        
        Returns
        -------
        output : Sampling
            the new sampling.
        """

    def append(self, m: int) -> Sampling:
        """
        Appends samples to this sampling.
        If this sampling is not uniform, appended sample values are computed 
        to preserve the average difference between adjacent sample values.
        
        This method returns a new sampling; it does not modify this sampling.
        
        Parameters
        ----------
        m : int
            the number of new samples appended to this sampling.
        
        Returns
        -------
        output : Sampling
            the new sampling.
        """

    def decimate(self, m: int) -> Sampling:
        """
        Decimates this sampling. Beginning with the first sample, keeps only 
        every m'th sample, while discarding the others in this sampling. If 
        this sampling has n values, the new sampling will have 1+(n-1)/m values.
        
        This method returns a new sampling; it does not modify this sampling.
        
        Parameters
        ----------
        m : int
            the factor by which to decimate; must be positive.
        
        Returns
        -------
        output : Sampling
            the new sampling.
        """

    def interpolate(self, m: int) -> Sampling:
        """
        Interpolates this sampling. Inserts m-1 evenly spaced samples between 
        each of the samples in this sampling. If this sampling has n values, 
        the new sampling will have 1+(n-1)*m values.
        
        This method returns a new sampling; it does not modify this sampling.
        
        Parameters
        ----------
        m : int
            the factor by which to interpolate.
        
        Returns
        -------
        output : Sampling
            the new sampling.
        """
