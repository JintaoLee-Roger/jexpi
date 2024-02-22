from typing import overload
from java.awt import *
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class HandleBox:
    """
    An axis-aligned handle box.
    """

    @overload
    def __init__(self, p: Point3) -> None:
        """
        Constructs a handle box with specified center location.
        
        Parameters
        -----------
        p : Point3
            the center point.
        """

    @overload
    def __init__(self, x: double, y: double, z: double) -> None:
        """
        Constructs a handle box with specified center coordinates.
        
        Parameters
        -----------
        x : double
            the center x coordinate.
        y : double
            the center y coordinate.
        z : double
            the center z coordinate.
        """

    @staticmethod
    def setColor(self, color: Color) -> None:
        """
        Sets the color of all handle boxes.
        
        Parameters
        -----------
        color : Color
            the color.
        """
