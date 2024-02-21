from typing import overload
from edu.mines.jtk.mapping import *


class EllipsoidGlyph:
    """
    A glyph for fast rendering of ellipsoids (including spheres).
    This class is especially useful in any node that must render a large
    number of ellipsoids. Such a node would first construct a single
    ellipsoid glyph, and then call one of the glyph's draw methods for
    each ellipsoid to be rendered.
    
    Internally, each ellipsoid is drawn by transforming an approximation to
    a unit sphere (with radius one) that has been precomputed and stored in
    an OpenGL display list.
    
    The unit sphere is approximated by recursively subdividing the triangular
    faces of an octahedron. The quality of the approximation increases with
    the number of subdivisions, and the number of triangles increases by a
    factor of four with each subdivision.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an ellipsoid glyph with default quality of four subdivisions.
        """

    @overload
    def __init__(self, m: int) -> None:
        """
        Constructs an ellipsoid glyph with specified quality.
        
        Parameters
        -----------
        m : int
            the quality = the number of subdivisions.
        """

    def countVertices(self) -> int:
        """
        Returns the number of vertices used to approximate this glyph.
        Returns
        --------
        output : int
            the number of vertices.
        """

    def getVertices(self) -> Float1D:
        """
        Gets the vertices of the unit sphere used to approximate this glyph.
        not by copy. The array length is 3 times the number of vertices.
        Returns
        --------
        output : Float1D
            array of packed (x,y,z) coordinates of vertices; by reference,
        """

    @overload
    def draw(self) -> None:
        """
        Draws a unit sphere centered at the origin.
        """

    @overload
    def draw(self, cx: float, cy: float, cz: float, r: float) -> None:
        """
        Draws a sphere centered at a specified point with specified radius.
        
        Parameters
        -----------
        cx : float
            x coordinate of the center point.
        cy : float
            y coordinate of the center point.
        cz : float
            z coordinate of the center point.
        r : float
            radius of the sphere.
        """

    @overload
    def draw(self, cx: float, cy: float, cz: float, dx: float, dy: float,
             dz: float) -> None:
        """
        Draws an axis-aligned ellipsoid centered at a specified point.
        The lengths of the specified semi-principal axes must be positive.
        
        Parameters
        -----------
        cx : float
            x coordinate of the center point.
        cy : float
            y coordinate of the center point.
        cz : float
            z coordinate of the center point.
        dx : float
            semi-principal length in direction of x axis.
        dy : float
            semi-principal length in direction of y axis.
        dz : float
            semi-principal length in direction of z axis.
        """

    @overload
    def draw(self, cx: float, cy: float, cz: float, ux: float, uy: float,
             uz: float, vx: float, vy: float, vz: float, wx: float, wy: float,
             wz: float) -> None:
        """
        Draws an arbitrary ellipsoid centered at a specified point.
        The semi-principal axes of the ellipsoid are represented by three
        vectors u, v, and w. The lengths of these three vectors are the
        semi-principal lengths of the ellipsoid, and must be non-zero.
        
        Parameters
        -----------
        cx : float
            x coordinate of the center point.
        cy : float
            y coordinate of the center point.
        cz : float
            z coordinate of the center point.
        ux : float
            x component of vector u.
        uy : float
            y component of vector u.
        uz : float
            z component of vector u.
        vx : float
            x component of vector v.
        vy : float
            y component of vector v.
        vz : float
            z component of vector v.
        wx : float
            x component of vector w.
        wy : float
            y component of vector w.
        wz : float
            z component of vector w.
        """
