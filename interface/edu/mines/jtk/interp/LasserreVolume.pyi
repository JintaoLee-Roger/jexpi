from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *


class LasserreVolume:
    """
    Volume of an n-dimensional convex polytope, via Lasserre's algorithm.
    The n-dimensional (nD) polytope is specified as the intersection of
    at least n+1 half-spaces. A 1D polytope is a line segment defined by
    two intersecting half-lines (or rays); a 2D polytope is a polygon
    defined by at least three intersecting half-planes, a 3D polytope is a
    polyhedron defined by at least four intersecting half-spaces, and so on.
    
    Each nD half-space is represented by an inequality of the form
    a1x1 + a2x2 + ... + anxn &lt;= b. For example, in 2D, each
    half-space is defined by coefficients a1, a2 and b, and at least
    three such half-spaces are required to define a bounded polygon.
    This class computes the area of such a polygon or, more generally,
    the volume of an nD polytope, using Lasserre's recursive algorithm.
    
    This implementation currently assumes that the half-planes for any
    redundant half-spaces are not parallel. This assumption is and (the
    computed volume) is valid if each specified half-plane represents
    part of the boundary of a strictly convex polytope. In particular,
    this assumption is valid for any Voronoi polytope.
    
    See Lasserre J.B., 1983, An analytical expression and an algorithm
    for the volume of a convex polyhedron in R^n: Journal of Optimization
    Theory and Applications, 39, 363--377.
    """

    def __init__(self, n: int) -> None:
        """
        Constructs an initially unbounded (infinite) volume in n dimensions.
        
        Parameters
        -----------
        n : int
            the number of dimensions.
        """

    @overload
    def addHalfSpace(self, a1: double, b: double) -> None:
        """
        Adds a 1D half-space a1x1 &lt;= b to bound this volume.
        Other coefficients a2, a3, ..., an, if any, are assumed to be zero.
        The dimension of this volume must be at least 2.
        
        Parameters
        -----------
        a1 : double
            the coefficient a1.
        b : double
            the right-hand-side.
        """

    @overload
    def addHalfSpace(self, a1: double, a2: double, b: double) -> None:
        """
        Adds a 2D half-space a1x1 + a2x2 &lt;= b to bound this volume.
        Other coefficients a3, a4, ..., an, if any, are assumed to be zero.
        The dimension of this volume must be at least 2.
        
        Parameters
        -----------
        a1 : double
            the coefficient a1.
        a2 : double
            the coefficient a2.
        b : double
            the right-hand-side.
        """

    @overload
    def addHalfSpace(self, a1: double, a2: double, a3: double,
                     b: double) -> None:
        """
        Adds a 3D half-space a1x1 + a2x2 + a3x3 &lt;= b to bound this volume.
        Other coefficients a4, a5, ..., an, if any, are assumed to be zero.
        The dimension of this volume must be at least 3.
        
        Parameters
        -----------
        a1 : double
            the coefficient a1.
        a2 : double
            the coefficient a2.
        a3 : double
            the coefficient a3.
        b : double
            the right-hand-side.
        """

    @overload
    def addHalfSpace(self, a: Double1D, b: double) -> None:
        """
        Adds an nD half-space a1x1 + a2x2 + &hellip; + anxn &lt;= b.
        Any missing coefficients are assumed to be zero.
        
        Parameters
        -----------
        a : Double1D
            array {a1,a2,...,an} of coefficients.
        b : double
            the right-hand-side.
        """

    @overload
    def clear(self) -> None:
        """
        Removes all half-spaces for this volume, making it infinite.
        """

    def getVolume(self) -> double:
        """
        Gets this volume.
        Returns
        --------
        output : double
            the volume; may be infinite.
        """
