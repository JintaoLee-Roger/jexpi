from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Point4:
    """
    A point with four coordinates x, y, z, and w.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a point with coordinates (x,y,z) = 0 and w = 1.
        """

    @overload
    def __init__(self, x: double, y: double, z: double) -> None:
        """
        Constructs a point with specified (x,y,z) coordinates and w = 1.
        
        Parameters
        -----------
        x : double
            the x coordinate.
        y : double
            the y coordinate.
        z : double
            the z coordinate.
        """

    @overload
    def __init__(self, x: double, y: double, z: double, w: double) -> None:
        """
        Constructs a point with specified coordinates.
        
        Parameters
        -----------
        x : double
            the x coordinate.
        y : double
            the y coordinate.
        z : double
            the z coordinate.
        w : double
            the w coordinate.
        """

    @overload
    def __init__(self, p: Point3) -> None:
        """
        Constructs a point from the specified 3-D point.
        The (x,y,z,w) coordinates of the constructed point are (p.x,p.y,p.z,1).
        
        Parameters
        -----------
        p : Point3
            the 3-D point.
        """

    @overload
    def __init__(self, p: Point4) -> None:
        """
        Constructs a copy of the specified point.
        
        Parameters
        -----------
        p : Point4
            the point.
        """

    def homogenize(self) -> Point4:
        """
        Returns the homogenized point equivalent to this point.
        Homogenization is division of the coordinates (x,y,z,w) by w.
        Returns
        --------
        output : Point4
            the homogenized point.
        """

    def homogenizeEquals(self) -> Point4:
        """
        Homogenizes this point.
        Homogenization is division of the coordinates (x,y,z,w) by w.
        Returns
        --------
        output : Point4
            this homogenized point.
        """

    def plus(self, v: Vector3) -> Point4:
        """
        Returns the point q = p+v, for this point p and the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point4
            the point q = p+v.
        """

    def minus(self, v: Vector3) -> Point4:
        """
        Returns the point q = p-v, for this point p and the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point4
            the point q = p-v.
        """

    def plusEquals(self, v: Vector3) -> Point4:
        """
        Moves this point p by adding the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point4
            this point, p += v, moved.
        """

    def minusEquals(self, v: Vector3) -> Point4:
        """
        Moves this point p by subtracting the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point4
            this point, p -= v, moved.
        """

    def affine(self, a: double, q: Point4) -> Point4:
        """
        Returns an affine combination of this point p and the specified point q.
        
        Parameters
        -----------
        a : double
            the weight of the point q.
        q : Point4
            the point q.
        
        Returns
        --------
        output : Point4
            the affine combination (1-a)p + aq.
        """
