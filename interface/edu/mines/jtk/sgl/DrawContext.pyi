from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class DrawContext:
    """
    A transform context for drawing.
    """

    def __init__(self, canvas: ViewCanvas) -> None:
        """
        Constructs a draw context for the specified view canvas.
        
        Parameters
        -----------
        canvas : ViewCanvas
            the view canvas.
        """
