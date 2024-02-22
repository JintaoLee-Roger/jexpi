from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Segment:
    """
    A segment of a line.
    """

    @overload
    def __init__(self, a: Point3, b: Point3) -> None:
        """
        Constructs a segment with the specified endpoints.
        
        Parameters
        -----------
        a : Point3
            the endpoint A.
        b : Point3
            the endpoint B.
        """

    @overload
    def __init__(self, ls: Segment) -> None:
        """
        Constructs a copy of the specified segment.
        
        Parameters
        -----------
        ls : Segment
            the segment.
        """

    def getA(self) -> Point3:
        """
        Gets the endpoint A of this segment.
        Returns
        --------
        output : Point3
            the endpoint A.
        """

    def getB(self) -> Point3:
        """
        Gets the endpoint B of this segment.
        Returns
        --------
        output : Point3
            the endpoint B.
        """

    def length(self) -> double:
        """
        Returns the length of this segment.
        Returns
        --------
        output : double
            the length.
        """

    def transform(self, m: Matrix44) -> None:
        """
        Transforms this segment, given the specified transform matrix.
        
        Parameters
        -----------
        m : Matrix44
            the transform matrix.
        """

    def intersectWithTriangle(self, xa: double, ya: double, za: double,
                              xb: double, yb: double, zb: double, xc: double,
                              yc: double, zc: double) -> Point3:
        """
        Tests this segment for intersection with the specified triangle. If
        such an intersection exists, this method returns the intersection point.
        
        Parameters
        -----------
        xa : double
            x coordinate of triangle vertex a.
        ya : double
            y coordinate of triangle vertex a.
        za : double
            z coordinate of triangle vertex a.
        xb : double
            x coordinate of triangle vertex b.
        yb : double
            y coordinate of triangle vertex b.
        zb : double
            z coordinate of triangle vertex b.
        xc : double
            x coordinate of triangle vertex c.
        yc : double
            y coordinate of triangle vertex c.
        zc : double
            z coordinate of triangle vertex c.
        
        Returns
        --------
        output : Point3
            the point of intersection; null, if none.
        """
