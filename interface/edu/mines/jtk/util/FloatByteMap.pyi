from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.util import *


class FloatByteMap:
    """
    Maps float values to unsigned byte values in the range [0,255].
    This mapping is useful in graphics where the bytes are indices
    or components of colors in color maps.
    """

    @overload
    def __init__(self, f: Float1D) -> None:
        """
        Constructs a map for specified values.
        
        Parameters
        -----------
        f : Float1D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, f: Float2D) -> None:
        """
        Constructs a map for specified values.
        
        Parameters
        -----------
        f : Float2D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, f: Float3D) -> None:
        """
        Constructs a map for specified values.
        
        Parameters
        -----------
        f : Float3D
            array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, f3: Float3) -> None:
        """
        Constructs a map for specified values.
        
        Parameters
        -----------
        f3 : Float3
            abstract 3-D array of values; by reference, not by copy.
        """

    @overload
    def __init__(self, percMin: double, percMax: double, f: Float1D) -> None:
        """
        Constructs a map for the specified percentiles and array.
        
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
        Constructs a map for the specified percentiles and array.
        
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
        
        Parameters
        -----------
        percMin : double
            the percentile corresponding to clipMin.
        percMax : double
            the percentile corresponding to clipMax.
        f3 : Float3
            abstract 3-D array of values; by reference, not by copy.
        """

    def getByte(self, f: float) -> int:
        """
        Gets the byte value corresponding to the specified float value.
        
        Parameters
        -----------
        f : float
            the float value to be mapped.
        
        Returns
        --------
        output : int
            the unsigned byte value in the range [0,255].
        """

    @overload
    def getBytes(self, f: Float1D, b: Byte1D) -> None:
        """
        Gets byte values corresponding to specified float values.
        
        Parameters
        -----------
        f : Float1D
            input array of float values to be mapped.
        b : Byte1D
            output array of unsigned byte values in the range [0,255].
        """

    @overload
    def getBytes(self, f: Float2D, b: Byte2D) -> None:
        """
        Gets byte values corresponding to specified float values.
        
        Parameters
        -----------
        f : Float2D
            input array of float values to be mapped.
        b : Byte2D
            output array of unsigned byte values in the range [0,255].
        """

    @overload
    def getBytes(self, f: Float2D, b: Byte1D) -> None:
        """
        Gets byte values corresponding to specified float values.
        
        Parameters
        -----------
        f : Float2D
            input array of float values to be mapped.
        b : Byte1D
            output array of unsigned byte values in the range [0,255].
        """

    @overload
    def getBytes(self, f: Float3D, b: Byte3D) -> None:
        """
        Gets byte values corresponding to specified float values.
        
        Parameters
        -----------
        f : Float3D
            input array of float values to be mapped.
        b : Byte3D
            output array of unsigned byte values in the range [0,255].
        """

    @overload
    def getBytes(self, f: Float3D, b: Byte1D) -> None:
        """
        Gets byte values corresponding to specified float values.
        
        Parameters
        -----------
        f : Float3D
            input array of float values to be mapped.
        b : Byte1D
            output array of unsigned byte values in the range [0,255].
        """

    @overload
    def getBytes(self, f3: Float3, b: Byte3D) -> None:
        """
        Gets byte values corresponding to specified float values.
        
        Parameters
        -----------
        f3 : Float3
            input array of float values to be mapped.
        b : Byte3D
            output array of unsigned byte values in the range [0,255].
        """

    @overload
    def getBytes(self, f3: Float3, b: Byte1D) -> None:
        """
        Gets byte values corresponding to specified float values.
        
        Parameters
        -----------
        f3 : Float3
            input array of float values to be mapped.
        b : Byte1D
            output array of unsigned byte values in the range [0,255].
        """

    def setClips(self, clipMin: double, clipMax: double) -> None:
        """
        Sets the clips for this mapping.
        
        Calling this method disables the computation of clips from percentiles.
        Any clip values computed or specified previously will be forgotten.
        
        Parameters
        -----------
        clipMin : double
            the sample value corresponding to byte value 0.
        clipMax : double
            the sample value corresponding to color model index 255.
        """

    def getClipMin(self) -> float:
        """
        Gets the minimum clip value for this mapping.
        Returns
        --------
        output : float
            the minimum clip value.
        """

    def getClipMax(self) -> float:
        """
        Gets the maximum clip value for this mapping.
        Returns
        --------
        output : float
            the maximum clip value.
        """

    def setPercentiles(self, percMin: double, percMax: double) -> None:
        """
        Sets the percentiles used to compute clips for this mapping. The
        default percentiles are 0 and 100, which correspond to the minimum
        and maximum array values.
        
        Calling this method enables the computation of clips from percentiles.
        Any clip values specified or computed previously will be forgotten.
        
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
