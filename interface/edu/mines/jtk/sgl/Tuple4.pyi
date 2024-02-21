from typing import overload
from edu.mines.jtk.mapping import *


class Tuple4:
    """
    A tuple with four components x, y, z, and w.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a tuple with all components equal to zero.
        """

    @overload
    def __init__(self, x: double, y: double, z: double, w: double) -> None:
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
        w : double
            the w component.
        """

    @overload
    def __init__(self, t: Tuple4) -> None:
        """
        Constructs a copy of the specified tuple.
        
        Parameters
        -----------
        t : Tuple4
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
