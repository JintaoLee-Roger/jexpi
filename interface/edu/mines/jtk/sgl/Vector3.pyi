from typing import overload
from edu.mines.jtk.mapping import *


class Vector3:
    """
    A vector with three components x, y, and z.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a vector with components zero.
        """

    @overload
    def __init__(self, x: double, y: double, z: double) -> None:
        """
        Constructs a vector with specified components.
        
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
    def __init__(self, v: Vector3) -> None:
        """
        Constructs a copy of the specified vector.
        
        Parameters
        -----------
        v : Vector3
            the vector.
        """

    def length(self) -> double:
        """
        Returns the length of this vector.
        Returns
        --------
        output : double
            the length.
        """

    def lengthSquared(self) -> double:
        """
        Returns the length-squared of this vector.
        Returns
        --------
        output : double
            the length-squared.
        """

    def negate(self) -> Vector3:
        """
        Returns the negation -u of this vector u.
        Returns
        --------
        output : Vector3
            the negation -u.
        """

    def negateEquals(self) -> Vector3:
        """
        Negates this vector.
        Returns
        --------
        output : Vector3
            this vector, negated.
        """

    def normalize(self) -> Vector3:
        """
        Returns the unit vector with the same direction as this vector.
        Returns
        --------
        output : Vector3
            the unit vector.
        """

    def normalizeEquals(self) -> Vector3:
        """
        Normalizes this vector to have unit length; makes this a unit vector.
        Returns
        --------
        output : Vector3
            this vector, normalized.
        """

    def plus(self, v: Vector3) -> Vector3:
        """
        Returns the vector sum u+v for this vector u.
        
        Parameters
        -----------
        v : Vector3
            the other vector.
        
        Returns
        --------
        output : Vector3
            the vector sum u+v
        """

    def plusEquals(self, v: Vector3) -> Vector3:
        """
        Adds a vector v to this vector u.
        
        Parameters
        -----------
        v : Vector3
            the other vector.
        
        Returns
        --------
        output : Vector3
            this vector, after adding the vector v.
        """

    def minus(self, v: Vector3) -> Vector3:
        """
        Returns the vector difference u-v for this vector u.
        
        Parameters
        -----------
        v : Vector3
            the other vector.
        
        Returns
        --------
        output : Vector3
            the vector difference u-v
        """

    def minusEquals(self, v: Vector3) -> Vector3:
        """
        Subtracts a vector v from this vector u.
        
        Parameters
        -----------
        v : Vector3
            the other vector.
        
        Returns
        --------
        output : Vector3
            this vector, after subtracting the vector v.
        """

    def times(self, s: double) -> Vector3:
        """
        Returns the scaled vector su for this vector u.
        
        Parameters
        -----------
        s : double
            the scale factor.
        
        Returns
        --------
        output : Vector3
            the scaled vector.
        """

    def timesEquals(self, s: double) -> Vector3:
        """
        Scales this vector.
        
        Parameters
        -----------
        s : double
            the scale factor.
        
        Returns
        --------
        output : Vector3
            this vector, scaled.
        """

    def dot(self, v: Vector3) -> double:
        """
        Returns the dot product of this vector u and the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : double
            the dot product.
        """

    def cross(self, v: Vector3) -> Vector3:
        """
        Returns the cross product of this vector u and the specified vector v.
        
        Parameters
        -----------
        v : Vector3
            the vector v.
        
        Returns
        --------
        output : Vector3
            the cross product.
        """
