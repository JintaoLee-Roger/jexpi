from typing import overload
from edu.mines.jtk.mapping import *


class FloatColorMap:
    """
    Maps arrays of floats to colors.
    
    This mapping consists of two parts. Floats are first mapped to bytes,
    and then those bytes are mapped to colors.
    
    The first mapping from floats to bytes is linear between minimum and
    maximum clip values. Values below and above these min and max values
    are clipped. Clips may be computed from percentiles or may be specified
    explicitly. By default, the clip min and max values are the minimum
    and maximum values in specified arrays of floats.
    
    The second mapping depends on the number of arrays of floats specified.
    When only one array is specified, each byte from the float-to-byte
    mapping is used as an index for an index color model with 256 colors.
    
    When three arrays are specified, a float value from each of the three
    arrays is first mapped independently (using different float-to-byte
    maps, possibly with different clips) to obtain three bytes. These
    three bytes are then interpreted directly as color components in
    either (red,green,blue) or (hue,saturation,brightness) color models.
    Because each color component can have 256 values, millions of colors
    are possible.
    
    When four arrays are specified, the mapping is the same as for three
    arrays, except that the fourth array corresponds to an alpha (opacity)
    component.
    
    An index color model may be useful even when three or four arrays are
    specified, by specifying one of the arrays to serve as a source of
    of byte indices. This capability enables a single float value to be
    mapped to a color, even when three or four arrays of floats are
    specified. For example, if the index color model contained fully
    saturated and bright colors with different hues, then one might
    specify the array corresponding to the hue component as the source
    of byte indices. The indexed colors might then be displayed in a color
    bar.
    
    By default, direct color components with indices 0, 1, and 2 are red,
    green, and blue, respectively. If HSB components are enabled, then
    these same indices instead correspond to components hue, saturation,
    and brightness. Enabling HSB adds an extra conversion step to the
    mapping from floats to colors. After three bytes are computed from
    three floats, these HSB byte values are then mapped to the nearest
    RGB byte values. The hues corresponding to min/max byte values 0
    and 255 are red (0.00) and blue (0.67), but these hues may be
    specified explicitly. This extra conversion step is never performed
    for indexed color mappings of single float values.
    """

    @overload
    def __init__(self, f: Float2D, icm: IndexColorModel) -> None:
        """
        Constructs a color map with only indexed colors.
        
        Parameters
        -----------
        f : Float2D
            an array of floats.
        icm : IndexColorModel
            the index color model.
        """

    @overload
    def __init__(self, f: Float3D, ic: int, icm: IndexColorModel) -> None:
        """
        Constructs a color map with more than one color components.
        
        Parameters
        -----------
        f : Float3D
            arrays of floats, one array for each color component.
        ic : int
            array index of the component for the index color model.
        icm : IndexColorModel
            the index color model corresponding to one component.
        """

    def setHSB(self, hsb: bool) -> None:
        """
        Enables or disables HSB components. By default, color components
        0, 1, and 2 (if specified) correspond to red, green, and blue. If HSB
        components are enabled, these indices correspond to hue, saturation,
        and brightness. Then, as floats are mapped to colors, bytes for HSB
        are converted to RGB.
        
        Parameters
        -----------
        hsb : bool
            true, to enable HSB components; false, for RGB components.
        """

    def setHues(self, hue000: double, hue255: double) -> None:
        """
        Sets hue values corresponding to byte values 0 and 255.
        These hues are used only when HSB components are enabled.
        
        Parameters
        -----------
        hue000 : double
            hue corresponding to byte value 0; default is 0.00 (red).
        hue255 : double
            hue corresponding to byte value 255; default is 0.67 (blue).
        """

    @overload
    def getIndex(self, f: float) -> int:
        """
        Gets the color index corresponding to the specified value.
        
        Parameters
        -----------
        f : float
            the value to be mapped to index.
        
        Returns
        --------
        output : int
            the index in the range [0,255].
        """

    @overload
    def getARGB(self, f: float) -> int:
        """
        Gets the 32-bit color in 0xAARRGGBB format for the specified value.
        This method uses the index color model.
        
        Parameters
        -----------
        f : float
            the value to be mapped to a color.
        
        Returns
        --------
        output : int
            the pixel.
        """

    def getRGB(self, f0: float, f1: float, f2: float) -> int:
        """
        Gets the 32-bit color in 0xffRRGGBB format for specified values.
        This method does not use the index color model.
        
        Parameters
        -----------
        f0 : float
            the value for color component 0.
        f1 : float
            the value for color component 1.
        f2 : float
            the value for color component 2.
        
        Returns
        --------
        output : int
            the color.
        """

    @overload
    def getARGB(self, f0: float, f1: float, f2: float, f3: float) -> int:
        """
        Gets the 32-bit color in 0xAARRGGBB format for specified values.
        This method does not use the index color model.
        
        Parameters
        -----------
        f0 : float
            the value for color component 0.
        f1 : float
            the value for color component 1.
        f2 : float
            the value for color component 2.
        f3 : float
            the value for color component 3.
        
        Returns
        --------
        output : int
            the color.
        """

    @overload
    def getIndex(self, v: double) -> int:
        """
        Gets the color index corresponding to the specified value.
        
        Parameters
        -----------
        v : double
            the value to be mapped to index.
        
        Returns
        --------
        output : int
            the index in the range [0,255].
        """

    def getMinValue(self) -> double:
        """
        Gets the minimum value in the range of mapped values.
        Returns
        --------
        output : double
            the minimum value.
        """

    def getMaxValue(self) -> double:
        """
        Gets the maximum value in the range of mapped values.
        Returns
        --------
        output : double
            the maximum value.
        """

    def setValueRange(self, vmin: double, vmax: double) -> None:
        """
        Sets the min-max range of values mapped to colors. Values outside this
        range are clipped. The default range is the min and max clips in the
        mapping from floats to bytes.
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        """
