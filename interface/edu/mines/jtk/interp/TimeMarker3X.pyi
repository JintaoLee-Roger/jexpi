from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.dsp import *


class TimeMarker3X:
    """
    EXPERIMENTAL: uses a heap instead of random shuffling of known samples.
    
    A time and closest-point transform for 3D anisotropic eikonal equations.
    Transforms an array of times and marks for known samples into an array
    of times and marks for all samples. Known samples are those for which
    times are zero, and times and marks for known samples are not modified.
    
    Times for unknown samples are computed by solving an anisotropic eikonal
    equation grad(t) dot W grad(t) = 1, where W denotes a positive-definite
    (velocity-squared) metric tensor field. The solution times t represent
    the traveltimes from one known sample to all unknown samples. Separate
    solution times t are computed for each known sample that has at least
    one unknown neighbor. (Such a known sample is sometimes called a
    "source point.") The output time for each sample is the minimum time
    computed in this way for all such known samples. Therefore, the times
    output for unknown samples are the traveltimes to the closest known
    samples, where "closest" here means least time, not least distance.
    
    As eikonal solutions t are computed for each known sample, the mark
    for that known sample is used to mark all unknown samples for which
    the solution time is smaller than the minimum time computed so far.
    If marks for known samples are distinct, then output marks for unknown
    samples indicate which known sample is closest. In this way output
    marks can represent a sampled Voronoi diagram, albeit one that has
    been generalized by replacing distance with time.
    
    This transform uses an iterative sweeping method to solve for times.
    Iterations are similar to those described by Jeong and Whitaker (2007).
    Computational complexity is O(M log K), where M is the number of
    unknown (missing) samples and K is the number of known samples.
    """

    def __init__(self, n1: int, n2: int, n3: int, tensors: Tensors3) -> None:
        """
        Constructs a time marker for the specified tensor field.
        
        Parameters
        -----------
        n1 : int
            number of samples in 1st dimension.
        n2 : int
            number of samples in 2nd dimension.
        n3 : int
            number of samples in 2nd dimension.
        tensors : Tensors3
            velocity-squared tensors.
        """

    def setTensors(self, tensors: Tensors3) -> None:
        """
        Sets the tensors used by this time marker.
        
        Parameters
        -----------
        tensors : Tensors3
            the tensors.
        """

    def setConcurrency(self, concurrency: Concurrency) -> None:
        """
        Sets the type of concurrency used to solve for times.
        The default concurrency is parallel.
        
        Parameters
        -----------
        concurrency : Concurrency
            the type of concurrency.
        """

    def apply(self, times: Float3D, marks: Int3D) -> None:
        """
        Transforms the specified array of times and marks.
        Known samples are those for which times are zero, and times
        and marks for these known samples are used to compute times
        and marks for unknown samples.
        
        Parameters
        -----------
        times : Float3D
            input/output array of times.
        marks : Int3D
            input/output array of marks.
        """
