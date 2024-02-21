from typing import overload


class Color:
    """
    The Color class is used to encapsulate colors in the default 
    sRGB color space or colors in arbitrary color spaces identified 
    by a ColorSpace. Every color has an implicit alpha value of 
    1.0 or an explicit one provided in the constructor. The alpha 
    value defines the transparency of a color and can be represented 
    by a float value in the range 0.0 - 1.0 or 0 - 255. An alpha 
    value of 1.0 or 255 means that the color is completely opaque 
    and an alpha value of 0 or 0.0 means that the color is completely 
    transparent. When constructing a Color with an explicit alpha or 
    getting the color/alpha components of a Color, the color components 
    are never premultiplied by the alpha component.
    """

    @overload
    def __init__(self, r: float, g: float, b: float) -> None:
        """
        Creates an opaque sRGB color with the specified red, green, 
        and blue values in the range (0.0 - 1.0).
        """

    @overload
    def __init__(self, r: float, g: float, b: float, a: float) -> None:
        """
        Creates an sRGB color with the specified red, green, blue, 
        and alpha values in the range (0.0 - 1.0).
        """

    @overload
    def __init__(self, rgb: int) -> None:
        """
        Creates an opaque sRGB color with the specified combined RGB 
        value consisting of the red component in bits 16-23, the 
        green component in bits 8-15, and the blue component in bits 0-7.
        """

    @overload
    def __init__(self, rgba: int, hasalpha: bool) -> None:
        """
        Creates an sRGB color with the specified combined RGBA value 
        consisting of the alpha component in bits 24-31, the red 
        component in bits 16-23, the green component in bits 8-15, 
        and the blue component in bits 0-7.
        """

    @overload
    def __init__(self, r: int, g: int, b: int) -> None:
        """
        Creates an opaque sRGB color with the specified red, green, 
        and blue values in the range (0 - 255).
        """

    @overload
    def __init__(self, r: int, g: int, b: int, a: int) -> None:
        """
        Creates an sRGB color with the specified red, green, blue, 
        and alpha values in the range (0 - 255).
        """

