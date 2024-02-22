from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class PointGroup:
    """
    A group of unstructured points.
    """

    @overload
    def __init__(self, xyz: Float1D) -> None:
        """
        Constructs a points group with specified coordinates.
        
        The (x,y,z) coordinates of points are packed into the specified
        array xyz. The number of points is np = xyz.length/3.
        
        Parameters
        -----------
        xyz : Float1D
            array[3np] of packed point coordinates.
        """

    @overload
    def __init__(self, xyz: Float1D, rgb: Float1D) -> None:
        """
        Constructs a points group with specified coordinates and colors.
        
        The (x,y,z) coordinates of points are packed into the specified
        array xyz. The number of points is np = xyz.length/3.
        
        The (r,g,b) components of colors are packed into the specified
        array rgb. The number of colors equals the number of points.
        
        Parameters
        -----------
        xyz : Float1D
            array[3np] of packed point coordinates.
        rgb : Float1D
            array[3np] of packed color components.
        """

    @overload
    def __init__(self, size: float, xyz: Float1D) -> None:
        """
        Constructs a points group with specified coordinates.
        
        The (x,y,z) coordinates of points are packed into the specified
        array xyz. The number of points is np = xyz.length/3.
        
        Parameters
        -----------
        size : float
            size of cubes used to represent points.
        xyz : Float1D
            array[3np] of packed point coordinates.
        """

    @overload
    def __init__(self, size: float, xyz: Float1D, rgb: Float1D) -> None:
        """
        Constructs a points group with specified coordinates and colors.
        
        The (x,y,z) coordinates of points are packed into the specified
        array xyz. The number of points is np = xyz.length/3.
        
        The (r,g,b) components of colors are packed into the specified
        array rgb. The number of colors equals the number of points.
        
        Parameters
        -----------
        size : float
            size of cubes used to represent points.
        xyz : Float1D
            array[3np] of packed point coordinates.
        rgb : Float1D
            array[3np] of packed color components.
        """
