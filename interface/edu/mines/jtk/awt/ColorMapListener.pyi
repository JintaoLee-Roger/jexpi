from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.awt import ColorMap


class ColorMapListener:
    """
    A color map listener listens for changes to a color map.
    """

    def colorMapChanged(cm: ColorMap) -> None:
        """
        Called when the color map changes.
        
        Parameters
        -----------
        cm : ColorMap
            the color mapper.
        """
