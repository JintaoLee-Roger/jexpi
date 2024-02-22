from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Plane:
    """
    A plane. A plane divides a 3-dimensional space into points above it,
    points below it, and points within it. The signed distance s from a
    point (x,y,z) to a plane is s = ax + by + cz + d, where (a,b,c,d)
    are coefficients that define the plane. Points within the plane satisfy
    the equation s = 0.
    """

    @overload
    def __init__(self, a: double, b: double, c: double, d: double) -> None:
        """
        Constructs a plane with specified coefficients.
        
        Parameters
        -----------
        a : double
            the coefficient a.
        b : double
            the coefficient b.
        c : double
            the coefficient c.
        d : double
            the coefficient d.
        """

    @overload
    def __init__(self, p: Point3, n: Vector3) -> None:
        """
        Constructs a plane. The plane will contain the specified point p
        and be orthogonal to the specified normal vector n, which points
        toward the space above the plane.
        
        Parameters
        -----------
        p : Point3
            the point in the plane.
        n : Vector3
            the normal vector.
        """

    @overload
    def __init__(self, p: Plane) -> None:
        """
        Constructs a copy of the specified plane.
        
        Parameters
        -----------
        p : Plane
            the plane.
        """

    def set(self, a: double, b: double, c: double, d: double) -> None:
        """
        Sets the coefficients of this plane.
        
        Parameters
        -----------
        a : double
            the coefficient a.
        b : double
            the coefficient b.
        c : double
            the coefficient c.
        d : double
            the coefficient d.
        """

    def getA(self) -> double:
        """
        Gets the plane coefficient a.
        Returns
        --------
        output : double
            the plane coefficient a.
        """

    def getB(self) -> double:
        """
        Gets the plane coefficient b.
        Returns
        --------
        output : double
            the plane coefficient b.
        """

    def getC(self) -> double:
        """
        Gets the plane coefficient c.
        Returns
        --------
        output : double
            the plane coefficient c.
        """

    def getD(self) -> double:
        """
        Gets the plane coefficient d.
        Returns
        --------
        output : double
            the plane coefficient d.
        """

    def getNormal(self) -> Vector3:
        """
        Gets the unit-vector normal to this plane. The vector points toward
        the space above the plane.
        Returns
        --------
        output : Vector3
            the unit-vector normal.
        """

    @overload
    def distanceTo(self, x: double, y: double, z: double) -> double:
        """
        Returns the signed distance from this plane to a specified point.
        Distance is negative for points below the plane, zero for points
        within the plane, and positive for points above the plane.
        
        Parameters
        -----------
        x : double
            the x coordinate of the point.
        y : double
            the y coordinate of the point.
        z : double
            the z coordinate of the point.
        
        Returns
        --------
        output : double
            the signed distance.
        """

    @overload
    def distanceTo(self, p: Point3) -> double:
        """
        Returns the signed distance from this plane to a specified point.
        Distance is negative for points below the plane, zero for points
        within the plane, and positive for points above the plane.
        
        Parameters
        -----------
        p : Point3
            the point.
        
        Returns
        --------
        output : double
            the signed distance.
        """

    def transform(self, m: Matrix44) -> None:
        """
        Transforms this plane, given the specified transform matrix.
        If the inverse of the transform matrix is known, the method
        {@link #transformWithInverse(Matrix44)} is more efficient.
        
        Let M denote the matrix that transforms points p from old to new
        coordinates; i.e., p' = Mp, where p' denotes a transformed point.
        In old coordinates, the plane P = (a,b,c,d) satisfies the equation
        ax + by + cz + d = 0, for all points p = (x,y,z) within the plane.
        This method returns a new transformed plane P' = (a',b',c',d') that
        satisfies the equation a'x' + b'y' + c'z' + d' = 0 for all
        transformed points p' = (x',y',z') within the transformed plane.
        
        Parameters
        -----------
        m : Matrix44
            the transform matrix.
        """

    def transformWithInverse(self, mi: Matrix44) -> None:
        """
        Transforms this plane, given the inverse of the transform matrix.
        If the inverse of the transform matrix is known, this method is
        more efficient than the method {@link #transform(Matrix44)}.
        
        Parameters
        -----------
        mi : Matrix44
            the inverse of the transform matrix.
        """

    def toString(self) -> String:
        """
    
        """
