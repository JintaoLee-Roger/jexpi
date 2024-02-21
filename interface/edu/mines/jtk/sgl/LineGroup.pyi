from typing import overload
from edu.mines.jtk.mapping import *


class LineGroup:
    """
    A group of one or more sets of connected line segments.
    """

    @overload
    def __init__(self, xyz: Float1D) -> None:
        """
        Constructs a line group with one set of connected line segments.
        
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
        Constructs a line group with one set of connected line segments.
        
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
    def __init__(self, xyz: Float2D) -> None:
        """
        Constructs a line group with multiple sets of connected line segments.
        
        The number of sets is ns = xyz.length. For the set with index is, (x,y,z)
        coordinates of points are packed into the array xyz[is]. The number of
        points in that set is np = xyz[is].length/3.
        
        Parameters
        -----------
        xyz : Float2D
            array[ns][3np] of packed point coordinates.
        """

    @overload
    def __init__(self, xyz: Float2D, rgb: Float2D) -> None:
        """
        Constructs a line group with multiple sets of connected line segments.
        
        The number of sets is ns = xyz.length. For the set with index is, (x,y,z)
        coordinates of points are packed into the array xyz[is]. The number of
        points in that set is np = xyz[is].length/3.
        
        If rgb is not null, this array contains similarly packed (r,g,b)
        components of colors. The number of colors equals the number of points.
        
        Parameters
        -----------
        xyz : Float2D
            array[ns][3np] of packed point coordinates.
        rgb : Float2D
            array[ns][3np] of packed color components.
        """
