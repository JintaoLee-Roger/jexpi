from typing import overload
from edu.mines.jtk.mapping import *


class ColorMap:
    """
    A color map converts a range of double values to colors.
    For any double value, a color map
    (1) transforms the value to an integer pixel in the range [0,255],
    (2) maps this integer pixel to a color using an index color model.
    
    The method {@link #getIndex(double)} performs step (1). For any
    double value, that method
    (1a) clips to a specified min-max range of values,
    (1b) linearly translates and scales to [0.0,255.0], and
    (1c) rounds to the nearest integer pixel in [0,255].
    Extensions of this class may of course override this method to
    implement alternative mappings.
    
    A color map maintains a list of color map listeners, and notifies those
    listeners whenever its mapping from values to colors has changed.
    """

    @overload
    def __init__(self, colorModel: IndexColorModel) -> None:
        """
        Constructs a color map for values in [0,1].
        The integers 0 and 255 must be valid pixels for the color model.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the index color model.
        """

    @overload
    def __init__(self, vmin: double, vmax: double,
                 colorModel: IndexColorModel) -> None:
        """
        Constructs a color map for specified values.
        The integers 0 and 255 must be valid pixels for the color model.
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        colorModel : IndexColorModel
            the index color model.
        """

    @overload
    def __init__(self, vmin: double, vmax: double, c: Color1D) -> None:
        """
        Constructs a color map for specified values and colors.
        The default value range is [0.0,1.0].
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        c : Color1D
            array[256] of colors.
        """

    @overload
    def __init__(self, vmin: double, vmax: double, r: Byte1D, g: Byte1D,
                 b: Byte1D) -> None:
        """
        Constructs a color map for specified values and colors. Red, green,
        and blue components are bytes in the range [0,255], inclusive.
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        r : Byte1D
            array[256] of reds.
        g : Byte1D
            array[256] of greens.
        b : Byte1D
            array[256] of blues.
        """

    @overload
    def __init__(self, vmin: double, vmax: double, r: Float1D, g: Float1D,
                 b: Float1D) -> None:
        """
        Constructs a color map for specified values and colors. Red, green,
        and blue components are floats in the range [0,1], inclusive.
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        r : Float1D
            array[256] of reds.
        g : Float1D
            array[256] of greens.
        b : Float1D
            array[256] of blues.
        """

    @overload
    def __init__(self, c: Color) -> None:
        """
        Constructs a color map for a specified solid color.
        
        Parameters
        -----------
        c : Color
            a color.
        """

    @overload
    def __init__(self, vmin: double, vmax: double, c: Color) -> None:
        """
        Constructs a color map for a specified solid color within a given [0,1]
        range.
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        c : Color
            a color.
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

    def getColorModel(self) -> IndexColorModel:
        """
        Gets the index color model used by this color map.
        Returns
        --------
        output : IndexColorModel
            the index color model.
        """

    def getColor(self, v: double) -> Color:
        """
        Gets the color corresponding to the specified value.
        
        Parameters
        -----------
        v : double
            the value to be mapped to a color.
        
        Returns
        --------
        output : Color
            the color.
        """

    def getIndex(self, v: double) -> int:
        """
        Gets the index in the range [0,255] corresponding to the specified value.
        
        Parameters
        -----------
        v : double
            the value to be mapped to an index.
        
        Returns
        --------
        output : int
            the index in the range [0,255].
        """

    def getRgbFloats(self, v: Float1D) -> Float1D:
        """
        Maps an array of floats to a packed array of RGB float values in [0,1].
        
        Parameters
        -----------
        v : Float1D
            the array of float values to be mapped to colors.
        
        Returns
        --------
        output : Float1D
            array[3v.length] of packed RGB float values.
        """

    def getHslFloats(self, v: Float1D) -> Float1D:
        """
        Maps an array of floats to a packed array of HSL float values in [0,1].
        
        Parameters
        -----------
        v : Float1D
            the array of float values to be mapped to HSL values.
        
        Returns
        --------
        output : Float1D
            array[3v.length] of packed HSL float values.
        """

    def getCieLabFloats(self, v: Float1D) -> Float1D:
        """
        Maps color values to the CIE Lab (CIELab) colorspace.
        
        CIE Lab is a non-linear color space specified by the "Commission
        internationale de l'éclairage", or CIE (English: International
        Commission of Illumination), and describes all colors visible to the
        human eye. This colorspace defines color positions along three axes: one
        axis being lightness (L), one axis representing the position between
        magenta and green (a), and one axis representing the position between
        yellow and blue (b).
        
        The design of this colorspace is to control mimic logarithmic response
        the human eye, and when mapped into three-dimensional space the
        perceptual difference can be estimated by the measuring the Euclidean
        distance between points.
        
        Parameters
        -----------
        v : Float1D
            the array of floats to be mapped to CIELab values.
        
        Returns
        --------
        output : Float1D
            array[3v.length] of packaed CIELab values.
        """

    @staticmethod
    def rgbToHsl(self, r: float, g: float, b: float) -> Float1D:
        """
        Maps an RGB value into HSL colorspace.
        
        Hue (H) is measured as an angle [0-360).
        Saturation (S) and Lightness (L) are computed as decimal percent [0,1].
        
        Parameters
        -----------
        r : float
            the red color value in range [0,1].
        g : float
            the green color value in range [0,1].
        b : float
            the blue color value in range [0,1].
        
        Returns
        --------
        output : Float1D
            an array[3] containing the HSL values.
        """

    @staticmethod
    def hslToRgb(self, h: float, s: float, l: float) -> Float1D:
        """
        Maps an HSL value into the RGB colorspace.
        
        Parameters
        -----------
        h : float
            the hue in range [0,360).
        s : float
            the saturation in range [0,1].
        l : float
            the lightness in range [0,1].
        
        Returns
        --------
        output : Float1D
            an array[3] containing mapped RGB values.
        """

    @overload
    @staticmethod
    def rgbToCieLab(self, rgb: Float1D) -> Float1D:
        """
        Converts an RGB value to the CIE Lab colorspace.
        
        Parameters
        -----------
        rgb : Float1D
            an array containing an RGB value.
        
        Returns
        --------
        output : Float1D
            an array[3] containing the CIE Lab values.
        """

    @overload
    @staticmethod
    def rgbToCieLab(self, r: float, g: float, b: float) -> Float1D:
        """
        Converts an RGB value to the CIE Lab colorspace.
        
        Parameters
        -----------
        r : float
            the red color value [0,1].
        g : float
            the green color value [0,1].
        b : float
            the blue color value [0,1].
        
        Returns
        --------
        output : Float1D
            an array[3] of CIE Lab values
        """

    @overload
    @staticmethod
    def cieLabToRgb(self, lab: Float1D) -> Float1D:
        """
        Converts a CIE Lab color value to an RGB color value.
        
        Parameters
        -----------
        lab : Float1D
            an array containing the CIE Lab values.
        
        Returns
        --------
        output : Float1D
            an array[3] containing RGB values.
        """

    @overload
    @staticmethod
    def cieLabToRgb(self, Ls: float, asf: float, bs: float) -> Float1D:
        """
        Converts a CIE Lab color value to an RGB color value.
        
        Parameters
        -----------
        Ls : float
            the CIE Lightness (L) value.
        asf : float
            the CIE a value.
        bs : float
            the CIE b value.
        
        Returns
        --------
        output : Float1D
            an array[3] containing RGB values.
        """

    def setValueRange(self, vmin: double, vmax: double) -> None:
        """
        Sets the min-max range of values mapped to colors. Values outside this
        range are clipped. The default range is [0.0,1.0].
        
        Parameters
        -----------
        vmin : double
            the minimum value.
        vmax : double
            the maximum value.
        """

    @overload
    def setColorModel(self, colorModel: IndexColorModel) -> None:
        """
        Sets the index color model for this color map.
        
        Parameters
        -----------
        colorModel : IndexColorModel
            the index color model.
        """

    @overload
    def setColorModel(self, c: Color) -> None:
        """
        Sets the index color model for this color map to a single color.
        
        Parameters
        -----------
        c : Color
            a color.
        """

    def addListener(self, cml: ColorMapListener) -> None:
        """
        Adds the specified color map listener.
        Then notifies the listener that this color map has changed.
        
        Parameters
        -----------
        cml : ColorMapListener
            the listener.
        """

    def removeListener(self, cml: ColorMapListener) -> None:
        """
        Removes the specified color map listener.
        
        Parameters
        -----------
        cml : ColorMapListener
            the listener.
        """

    @overload
    @staticmethod
    def getGray(self) -> IndexColorModel:
        """
        Gets a linear gray black-to-white color model.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getGray(self, g0: double, g255: double) -> IndexColorModel:
        """
        Gets a linear gray color model for the specified gray levels. Gray
        levels equal to 0.0 and 1.0 correspond to colors black and white,
        respectively.
        
        Parameters
        -----------
        g0 : double
            the gray level corresponding to index value 0.
        g255 : double
            the gray level corresponding to index value 255.
        
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getGray(self, g0: double, g255: double,
                alpha: double) -> IndexColorModel:
        """
        Gets a linear gray color model for the specified gray levels. Gray
        levels equal to 0.0 and 1.0 correspond to colors black and white,
        respectively.
        
        Parameters
        -----------
        g0 : double
            the gray level corresponding to index value 0.
        g255 : double
            the gray level corresponding to index value 255.
        alpha : double
            the opacity for all colors in this color model.
        
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getJet(self) -> IndexColorModel:
        """
        Gets a red-to-blue color model like Matlab's jet color map.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getJet(self, alpha: double) -> IndexColorModel:
        """
        Gets a red-to-blue color model like Matlab's jet color map.
        
        Parameters
        -----------
        alpha : double
            the opacity for all colors in this color model.
        
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getGmtJet(self) -> IndexColorModel:
        """
        Gets a red-to-blue color model like GMT's jet color map.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getGmtJet(self, alpha: double) -> IndexColorModel:
        """
        Gets a red-to-blue color model like GMT's jet color map.
        
        Parameters
        -----------
        alpha : double
            the opacity for all colors in this color model.
        
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @staticmethod
    def getPrism(self) -> IndexColorModel:
        """
        Gets a color model with eight complete cycles of hues.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getHue(self) -> IndexColorModel:
        """
        Gets a red-to-blue linear hue color model.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @staticmethod
    def getHueRedToBlue(self) -> IndexColorModel:
        """
        Gets a red-to-blue linear hue color model.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @staticmethod
    def getHueBlueToRed(self) -> IndexColorModel:
        """
        Gets a blue-to-red linear hue color model.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getHue(self, h0: double, h255: double) -> IndexColorModel:
        """
        Gets a linear hue color model for the specified hues. Hues equal to
        0.00, 0.33, and 0.67, and 1.00 correspond approximately to the colors
        red, green, blue, and red, respectively.
        
        Parameters
        -----------
        h0 : double
            the hue corresponding to index value 0.
        h255 : double
            the hue corresponding to index value 255.
        
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @overload
    @staticmethod
    def getHue(self, h0: double, h255: double,
               alpha: double) -> IndexColorModel:
        """
        Gets a linear hue color model for the specified hues and alpha.
        Hues equal to 0.00, 0.33, and 0.67, and 1.00 correspond
        approximately to the colors red, green, blue, and red, respectively.
        
        Parameters
        -----------
        h0 : double
            the hue corresponding to index value 0.
        h255 : double
            the hue corresponding to index value 255.
        alpha : double
            the opacity for all colors in this color model.
        
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @staticmethod
    def getRedWhiteBlue(self) -> IndexColorModel:
        """
        Gets a red-white-blue color model.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @staticmethod
    def getBlueWhiteRed(self) -> IndexColorModel:
        """
        Gets a blue-white-red color model.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @staticmethod
    def getGrayYellowRed(self) -> IndexColorModel:
        """
        Gets the gray-yellow-red color model.
        Returns
        --------
        output : IndexColorModel
            the color model.
        """

    @staticmethod
    def makeIndexColorModel(self, c: Color1D) -> IndexColorModel:
        """
        Returns an index color model for the specified array of 256 colors.
        
        Parameters
        -----------
        c : Color1D
            array[256] of colors.
        
        Returns
        --------
        output : IndexColorModel
            the index color model.
        """

    @staticmethod
    def makeSolidColors(self, c: Color) -> IndexColorModel:
        """
        Returns an index color model for a single color.
        
        Parameters
        -----------
        c : Color
            a color.
        
        Returns
        --------
        output : IndexColorModel
            the index color model.
        """

    @overload
    @staticmethod
    def setAlpha(self, icm: IndexColorModel, alpha: double) -> IndexColorModel:
        """
        Returns an index color model with specified opacity (alpha).
        
        Parameters
        -----------
        icm : IndexColorModel
            an index color model from which to copy RGBs.
        alpha : double
            opacity in the range [0.0,1.0].
        
        Returns
        --------
        output : IndexColorModel
            the index color model with alpha.
        """

    @overload
    @staticmethod
    def setAlpha(self, icm: IndexColorModel,
                 alpha: Float1D) -> IndexColorModel:
        """
        Returns an index color model with specified opacities (alphas).
        
        Parameters
        -----------
        icm : IndexColorModel
            an index color model from which to copy RGBs.
        alpha : Float1D
            array of opacities in the range [0.0,1.0].
        
        Returns
        --------
        output : IndexColorModel
            the index color model with alphas.
        """
