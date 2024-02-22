from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class DPoint:
    """
    A double-precision point (x,y).
    """

    @overload
    def __init__(self, x: double, y: double) -> None:
        """
        Constructs a point.
        
        Parameters
        -----------
        x : double
            the x-coordinate.
        y : double
            the y-coordinate.
        """

    @overload
    def __init__(self, p: DPoint) -> None:
        """
        Constructs a copy of the specified point.
        
        Parameters
        -----------
        p : DPoint
            the point.
        """

    def equals(self, obj: Object) -> bool:
        """
    
        """

    def hashCode(self) -> int:
        """
    
        """

    def toString(self) -> String:
        """
    
        """
