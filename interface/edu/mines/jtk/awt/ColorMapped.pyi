from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.awt import ColorMap


class ColorMapped:
    """
    A color mapped object has a colormap.
    """

    def getColorMap() -> ColorMap:
        """
        Gets the color map.
        Returns
        --------
        output : ColorMap
            the color map.
        """
