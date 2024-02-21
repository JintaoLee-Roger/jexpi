from typing import overload
from edu.mines.jtk.mapping import *


class Point3:
    """
    A point with three coordinates x, y, and z.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a point with coordinates zero.
        """

    @overload
    def __init__(self, x: double, y: double, z: double) -> None:
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
        """

    @overload
    def __init__(self, p: Point4) -> None:
        """
        Constructs a point from the specified 4-d point. The (x,y,z)
        coordinates of the constructed point are (p.x/p.w,p.y/p.w,p.z/p.w).
        
        Parameters
        -----------
        p : Point4
            the 4-D point.
        """

    @overload
    def __init__(self, p: Point3) -> None:
        """
        Constructs a copy of the specified point.
        
        Parameters
        -----------
        p : Point3
            the point.
        """

    def plus(self, v: Vector3) -> Point3:
        """
        Returns the point q = p+v, for this point p and the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point3
            the point q = p+v.
        """

    @overload
    def minus(self, v: Vector3) -> Point3:
        """
        Returns the point q = p-v, for this point p and the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point3
            the point q = p-v.
        """

    @overload
    def minus(self, q: Point3) -> Vector3:
        """
        Returns the vector v = p-q, for this point p and the specified point q.
        
        Parameters
        -----------
        q : Point3
            the point q.
        
        Returns
        --------
        output : Vector3
            the vector v = p-q.
        """

    def plusEquals(self, v: Vector3) -> Point3:
        """
        Moves this point p by adding the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point3
            this point, p += v, moved.
        """

    def minusEquals(self, v: Vector3) -> Point3:
        """
        Moves this point p by subtracting the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Point3
            this point, p -= v, moved.
        """

    def affine(self, a: double, q: Point3) -> Point3:
        """
        Returns an affine combination of this point p and the specified point q.
        
        Parameters
        -----------
        a : double
            the weight of the point q.
        q : Point3
            the point q.
        
        Returns
        --------
        output : Point3
            the affine combination (1-a)p + aq.
        """

    def distanceTo(self, q: Point3) -> double:
        """
        Returns the distance between this point p and the specified point q.
        
        Parameters
        -----------
        q : Point3
            the point.
        
        Returns
        --------
        output : double
            the distance |q-p|.
        """
