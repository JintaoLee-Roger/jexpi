from typing import overload
from edu.mines.jtk.mapping import *


class Clips:
    """
    Clips (clipMin,clipMax) are lower and upper bounds for arrays of values.
    The name "clips" comes from the way these bounds are used, as when
    displaying data. Typically, below/above clipMin/clipMax are clipped
    to these bounds. Clips maintain the bounds, but do not perform the
    clipping.
    
    The lower bound clipMin must be less than the upper bound clipMax;
    this restriction is silently enforced by all methods of this class.
    This means that clips returned may not exactly equal those specified.
    
    This class is most useful when computing clips from percentiles.
    For example, the bounds clipMin and clipMax may correspond to
    percMin=1% and percMax=99%, respectively. The default percentiles
    percMin=0% and percMax=100% correspond to minimum and maximum values.
    
    Clips maintain a reference to an array of values, so that clips can be
    updated when percentiles are changed. If not using percentiles, because
    clipMin and clipMax are specified explicitly, then these arrays are
    ignored.
    """

    @overload
    def __init__(self, f: Float1D) -> None:
        """
        Constructs clips for the specified array.
        Uses default percentiles of 0.0 and 100.0.
        
        Parameters
        -----------
        f : Float1D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, f: Float2D) -> None:
        """
        Constructs clips for the specified array.
        Uses default percentiles of 0.0 and 100.0.
        
        Parameters
        -----------
        f : Float2D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, f: Float3D) -> None:
        """
        Constructs clips for the specified array.
        Uses default percentiles of 0.0 and 100.0.
        
        Parameters
        -----------
        f : Float3D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, f3: Float3) -> None:
        """
        Constructs clips for the specified array.
        Uses default percentiles of 0.0 and 100.0.
        
        Parameters
        -----------
        f3 : Float3
            abstract 3-D array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, percMin: double, percMax: double, f: Float1D) -> None:
        """
        Constructs clips for the specified percentiles and array.
        Computation of clips is deferred until they are got.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        f : Float1D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, percMin: double, percMax: double, f: Float2D) -> None:
        """
        Constructs clips for the specified percentiles and array.
        Computation of clips is deferred until they are got.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        f : Float2D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, percMin: double, percMax: double, f: Float3D) -> None:
        """
        Constructs clips for the specified percentiles and array.
        Computation of clips is deferred until they are got.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        f : Float3D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, percMin: double, percMax: double, f3: Float3) -> None:
        """
        Constructs clips for the specified percentiles and array.
        Computation of clips is deferred until they are got.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        f3 : Float3
            abstract 3-D array of values; by reference, not by copy.
        """

    @overload
    def setArray(self, f: Float1D) -> None:
        """
        Sets the array of values for these clips.
        These values are used only when computing clips from percentiles.
        
        Parameters
        -----------
        f : Float1D
            array of values; by reference, not by copy.
        """

    @overload
    def setArray(self, f: Float2D) -> None:
        """
        Sets the array of values for these clips.
        These values are used only when computing clips from percentiles.
        
        Parameters
        -----------
        f : Float2D
            array of values; by reference, not by copy.
        """

    @overload
    def setArray(self, f: Float3D) -> None:
        """
        Sets the array of values for these clips.
        These values are used only when computing clips from percentiles.
        
        Parameters
        -----------
        f : Float3D
            array of values; by reference, not by copy.
        """

    @overload
    def setArray(self, f3: Float3) -> None:
        """
        Sets the array of values for these clips.
        These values are used only when computing clips from percentiles.
        
        Parameters
        -----------
        f3 : Float3
            array of values; by reference, not by copy.
        """

    def setClips(self, clipMin: double, clipMax: double) -> None:
        """
        Sets the clip min and max values explicitly.
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        Parameters
        -----------
        clipMin : double
            values &lt; clipMin will be clipped to clipMin.
        clipMax : double
            values &gt; clipMax will be clipped to clipMax.
        """

    def getClipMin(self) -> float:
        """
        Gets the minimum clip value.
        Returns
        --------
        output : float
            the minimum clip value.
        """

    def getClipMax(self) -> float:
        """
        Gets the maximum clip value.
        Returns
        --------
        output : float
            the maximum clip value.
        """

    def setPercentiles(self, percMin: double, percMax: double) -> None:
        """
        Sets the percentiles used to compute clips for this view. The default
        percentiles are 0.0 and 100.0, which correspond to the minimum and
        maximum values in the array of values to be clipped.
        
        Calling this method enables the computation of clips from percentiles.
        Any clip min and max specified or computed previously will be forgotten.
        
        Clip min and max values can only be computed if an array of values has
        been specified. If clips were constructed without such an array, then
        both percentiles and an array of values should be set to enable the
        use of percentiles.
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        """

    def getPercentileMin(self) -> float:
        """
        Gets the minimum percentile.
        Returns
        --------
        output : float
            the minimum percentile.
        """

    def getPercentileMax(self) -> float:
        """
        Gets the maximum percentile.
        Returns
        --------
        output : float
            the maximum percentile.
        """
