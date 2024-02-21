from typing import overload
from edu.mines.jtk.mapping import *


class Tuple3:
    """
    A tuple with three components x, y, and z.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a tuple with all components equal to zero.
        """

    @overload
    def __init__(self, x: double, y: double, z: double) -> None:
        """
        Constructs a tuple with specified components.
        
        Parameters
        -----------
        x : double
            the x component.
        y : double
            the y component.
        z : double
            the z component.
        """

    @overload
    def __init__(self, t: Tuple3) -> None:
        """
        Constructs a copy of the specified tuple.
        
        Parameters
        -----------
        t : Tuple3
            the tuple.
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
