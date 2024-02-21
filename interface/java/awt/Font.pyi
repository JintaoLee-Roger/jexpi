from typing import overload


class Font:
    """
    The Font class represents fonts, which are used to render 
    text in a visible way. A font provides the information needed 
    to map sequences of characters to sequences of glyphs and to render 
    sequences of glyphs on Graphics and Component objects.
    """

    @overload
    def __init__(self, font: Font) -> None:
        """Creates a new Font from the specified font."""

    @overload
    def __init__(self, name: str, style: int, size: int) -> None:
        """
        Creates a new Font from the specified name, style and point size.
        """
