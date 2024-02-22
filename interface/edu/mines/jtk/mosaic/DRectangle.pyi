from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class DRectangle:
    """
    A double-precision rectangle. The rectangle is represented by a corner
    point (x,y) and size (width,height). The corner point (x,y) is that
    point inside the rectangle with minimum x and y coordinates. All points
    <em>contained</em> by the rectangle have x coordinates in the range
    [x,x+width] and y coordinates in the range [y,y+height].
    """

    @overload
    def __init__(self, x: double, y: double, width: double,
                 height: double) -> None:
        """
        Constructs a rectangle.
        
        Parameters
        -----------
        x : double
            the minimum x coordinate.
        y : double
            the minimum y coordinate.
        width : double
            the width; must not be negative.
        height : double
            the height; must not be negative.
        """

    @overload
    def __init__(self, r: DRectangle) -> None:
        """
        Constructs a copy of the specified rectangle.
        
        Parameters
        -----------
        r : DRectangle
            the rectangle.
        """

    def union(self, rect: DRectangle) -> DRectangle:
        """
        Returns the union of this rectangle and a specified rectangle.
        
        Parameters
        -----------
        rect : DRectangle
            a rectangle.
        
        Returns
        --------
        output : DRectangle
            the union.
        """

    def intersection(self, rect: DRectangle) -> DRectangle:
        """
        Returns the intersection of this rectangle and a specified rectangle.
        
        Parameters
        -----------
        rect : DRectangle
            a rectangle.
        
        Returns
        --------
        output : DRectangle
            the intersection.
        """

    def isEmpty(self) -> bool:
        """
        Determines whether this rectangle is empty.
        Returns
        --------
        output : bool
            true, if empty; false, otherwise.
        """

    @overload
    def contains(self, point: DPoint) -> bool:
        """
        Determines whether this rectangle contains the specified point.
        
        Parameters
        -----------
        point : DPoint
            the point.
        
        Returns
        --------
        output : bool
            true, if this rectangle contains the point; false, otherwise.
        """

    @overload
    def contains(self, x: double, y: double) -> bool:
        """
        Determines whether this rectangle contains the point (x,y).
        
        Parameters
        -----------
        x : double
            the x-coordinate of the point.
        y : double
            the y-coordinate of the point.
        
        Returns
        --------
        output : bool
            true, if this rectangle contains the point; false, otherwise.
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
