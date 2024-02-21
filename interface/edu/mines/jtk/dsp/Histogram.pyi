from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import *

class Histogram:
    """
    A histogram summarizes the distribution of values v in an array.
    The range (vmax-vmin) of values v in the array is partitioned uniformly
    into some number of bins. Each bin then contains the number of values
    that lie closest to the center of that bin.
    
    If the values v in the array are assumed to be instances of some random
    variable, then a probability density function may be estimated for that
    variable by simply dividing the count in each bin by the total number of
    values in the array. The resulting fractions are called the densities.
    
    The number of bins may be specified or computed automatically. In the
    automatic case, we compute bin width = 2.0(v75-v25)/pow(n,1.0/3.0),
    where n denotes the number of values, and v25 and v75 are the 25th and
    75th percentiles, respectively. The number of bins is then computed by
    dividing the range (vmax-vmin) of values by that bin width, rounding
    down to the nearest integer. In this way, the number of bins grows
    as the cube root of the number of values n.
    
    Minimum and maximum values (vmin and vmax) may also be specified or
    computed automatically. If specified, then only values in the range
    [vmin,vmax] are binned, and values outside this range are ignored.
    
    Reference: Izenman, A. J., 1991, Recent developments in nonparametric
    density estimation: Journal of the American Statistical Association,
    v. 86, p. 205-224.
    """

    @overload
    def __init__(self, v: Float1D) -> None:
        """
        Constructs a histogram for the specified array of values.
        Computes the number of bins to obtain a robust estimate of the density
        function. Counts and bins all values.
        
        Parameters
        -----------
        v : Float1D
            the array of values.
        """

    @overload
    def __init__(self, v: Float1D, nbin: int) -> None:
        """
        Constructs a histogram for the specified array of values.
        Counts and bins all values.
        
        Parameters
        -----------
        v : Float1D
            the array of values.
        nbin : int
            the number of bins.
        """

    @overload
    def __init__(self, v: Float1D, vmin: float, vmax: float) -> None:
        """
        Constructs a histogram for the specified array of values.
        Computes the number of bins to obtain a robust estimate of the density
        function. Counts and bins only those values in [vmin,vmax].
        
        Parameters
        -----------
        v : Float1D
            the array of values.
        vmin : float
            the minimum value.
        vmax : float
            the maximum value.
        """

    @overload
    def __init__(self, v: Float1D, vmin: float, vmax: float,
                 nbin: int) -> None:
        """
        Constructs a histogram for the specified array of values.
        Counts and bins only those values in [vmin,vmax].
        
        Parameters
        -----------
        v : Float1D
            the array of values.
        vmin : float
            the minimum value.
        vmax : float
            the maximum value.
        nbin : int
            the number of bins.
        """

    def getMinValue(self) -> float:
        """
        Gets the minimum value (vmin) for this histogram.
        Returns
        --------
        output : float
            the minimum value.
        """

    def getMaxValue(self) -> float:
        """
        Gets the maximum value (vmax) for this histogram.
        Returns
        --------
        output : float
            the maximum value.
        """

    def getBinCount(self) -> int:
        """
        Gets the number of bins in this histogram.
        Returns
        --------
        output : int
            the number of bins.
        """

    def getBinDelta(self) -> double:
        """
        Gets the bin width (delta) for this histogram.
        Returns
        --------
        output : double
            the bin width.
        """

    def getBinFirst(self) -> double:
        """
        Gets the value of the center of the first bin for this histogram.
        Returns
        --------
        output : double
            the value of the center of the first bin.
        """

    def getBinSampling(self) -> Sampling:
        """
        Gets the bin sampling for this histogram.
        Values sampled are the centers of the bins.
        Returns
        --------
        output : Sampling
            the bin sampling.
        """

    def getCounts(self) -> Long1D:
        """
        Gets the array of counts, one count for each bin.
        Returns
        --------
        output : Long1D
            array[nbin] of counts, where nbin is the number of bins.
        """

    def getDensities(self) -> Float1D:
        """
        Gets the array of densities, one density for each bin.
        A density for one bin equals the fraction of values in that bin.
        Returns
        --------
        output : Float1D
            array[nbin] of densities, where nbin is the number of bins.
        """

    def getInCount(self) -> long:
        """
        Gets the number of values in the range [vmin,vmax].
        Returns
        --------
        output : long
            the number of values.
        """

    def getLowCount(self) -> long:
        """
        Gets the number of values less than vmin.
        Returns
        --------
        output : long
            the number of values.
        """

    def getHighCount(self) -> long:
        """
        Gets the number of values greater than vmax.
        Returns
        --------
        output : long
            the number of values.
        """
