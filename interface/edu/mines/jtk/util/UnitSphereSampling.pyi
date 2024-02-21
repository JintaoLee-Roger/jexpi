from typing import overload
from edu.mines.jtk.mapping import *


class UnitSphereSampling:
    """
    A roughly uniform sampling of the unit-sphere.
    Maps integer sample indices i to points (x,y,z) on the unit sphere. The
    sampling is only approximately uniform because sampled points on the
    sphere are projections of points that uniformly sample an octahedron.
    The corners of that octahedron are the points (1,0,0), (-1,0,0), (0,1,0),
    (0,-1,0), (0,0,1), and (0,0,-1). Sampling near these corner points is
    finer than sampling elsewhere on the unit sphere.
    
    Positive sample indices correspond to points in the upper hemisphere
    for which z&gt;=0. Negative sample indices correspond to points in the
    lower hemisphere for which z&lt;=0. The sample index zero corresponds
    to no point. Points on the equator (x,y,z=0) correspond to both negative
    and positive sample indices.
    
    Points with positive and negative indices are sampled symmetrically
    about the center of the unit sphere. Specifically, if sample index i
    corresponds to a point (x,y,z), then sample index -i corresponds to
    the point (-x,-y,-z).
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a default sampling using sixteen bits per sample.
        Errors for 16-bit samples are less than one degree of arc.
        Where such errors are negligible, this default is both efficient
        and convenient because points can be encoded as 16-bit shorts.
        """

    @overload
    def __init__(self, nbits: int) -> None:
        """
        Constructs a sampling for the specified number of bits.
        Sample indices are signed integers with no more than this
        number of bits, which includes the sign bit.
        
        Parameters
        -----------
        nbits : int
            the number of bits; 4 &le; nbits &le; 32 required.
        """

    def countSamples(self) -> int:
        """
        Gets the number of points sampled on this unit sphere.
        Returns
        --------
        output : int
            the number of points sampled.
        """

    def getMaxIndex(self) -> int:
        """
        Gets the maximum sample index, a positive integer. The smallest
        positive index is one. The smallest index is the negative of the
        maximum index, and the largest negative index is minus one.
        
        This number equals the number of points sampled in one hemisphere,
        including points on the equator.
        Returns
        --------
        output : int
            the maximum index.
        """

    def getPoint(self, index: int) -> Float1D:
        """
        Gets the sampled point for the specified index, which must be non-zero.
        For efficiency, returns the array {x,y,z} of point coordinates
        by reference, not by copy. These coordinates must not be modified.
        
        Parameters
        -----------
        index : int
            the index of the sampled point; must be non-zero.
        
        Returns
        --------
        output : Float1D
            array {x,y,z} of point coordinates; by reference, not by copy.
        """

    @overload
    def getIndex(self, x: float, y: float, z: float) -> int:
        """
        Gets the index of the sampled point nearest to the specified point.
        Here, the nearest sampled point is that nearest on the octahedron.
        Returns a positive index for points in the upper hemisphere (z&gt;=0),
        including points on the equator (z=0). Returns a negative index for
        points in the lower hemisphere not on the equator (z&lt;0).
        
        Parameters
        -----------
        x : float
            x-coordinate of the point.
        y : float
            y-coordinate of the point.
        z : float
            z-coordinate of the point.
        
        Returns
        --------
        output : int
            the sample index.
        """

    @overload
    def getIndex(self, xyz: Float1D) -> int:
        """
        Gets the index of the sampled point nearest to the specified point.
        Here, the nearest sampled point is that nearest on the octahedron.
        
        Parameters
        -----------
        xyz : Float1D
            array {x,y,z} of point coordinates.
        
        Returns
        --------
        output : int
            the sample index.
        """

    @overload
    def getTriangle(self, x: float, y: float, z: float) -> Int1D:
        """
        Gets an array {ia,ib,ic} of three sample indices for the spherical
        triangle that contains the specified point. As viewed from outside
        the sphere, the sampled points corresponding to the returned indices
        are ordered counter-clockwise.
        
        Parameters
        -----------
        x : float
            x-coordinate of the point.
        y : float
            y-coordinate of the point.
        z : float
            z-coordinate of the point.
        
        Returns
        --------
        output : Int1D
            array of sample indices.
        """

    @overload
    def getTriangle(self, xyz: Float1D) -> Int1D:
        """
        Gets an array {ia,ib,ic} of three sample indices for a spherical
        triangle that contains the specified point. As viewed from outside
        the sphere, the sampled points corresponding to the returned indices
        are ordered counter-clockwise.
        
        Parameters
        -----------
        xyz : Float1D
            array {x,y,z} of point coordinates.
        
        Returns
        --------
        output : Int1D
            array of sample indices.
        """

    @overload
    def getWeights(self, x: float, y: float, z: float, iabc: Int1D) -> Float1D:
        """
        Gets an array {wa,wb,wc} of three weights for a point in a spherical
        triangle specified by sample indices of three points. The weights are
        proportional to volumes of tetrahedra, and are used for interpolation.
        Weights are non-negative and normalized so that their sum wa+wb+wc = 1.
        
        For example, let p denote the specified point with coordinates {x,y,z},
        and let o denote the center of the sphere with coordinates {0,0,0}.
        Then the weight wa is proportional to the volume of the tetrahedron
        formed by points p, b, c, and o.
        
        Parameters
        -----------
        x : float
            x-coordinate of the point.
        y : float
            y-coordinate of the point.
        z : float
            z-coordinate of the point.
        iabc : Int1D
            array {ia,ib,ic} of sample indices.
        
        Returns
        --------
        output : Float1D
            array {wa,wb,wc} of weights.
        """

    @overload
    def getWeights(self, xyz: Float1D, iabc: Int1D) -> Float1D:
        """
        Gets an array {wa,wb,wc} of three weights for a point in a spherical
        triangle specified by sample indices of three points. The weights are
        proportional to volumes of tetrahedra, and are used for interpolation.
        Weights are non-negative and normalized so that their sum wa+wb+wc = 1.
        
        For example, let p denote the specified point with coordinates {x,y,z},
        and let o denote the center of the sphere with coordinates {0,0,0}.
        Then the weight wa is proportional to the volume of the tetrahedron
        formed by points p, b, c, and o.
        
        Parameters
        -----------
        xyz : Float1D
            array {x,y,z} of point coordinates.
        iabc : Int1D
            array {ia,ib,ic} of sample indices.
        
        Returns
        --------
        output : Float1D
            array {wa,wb,wc} of weights.
        """

    @overload
    @staticmethod
    def encode16(self, x: Float1D, y: Float1D, z: Float1D) -> Short1D:
        """
        Encodes specified points as 16-bit (short) indices.
        
        Parameters
        -----------
        x : Float1D
            array of x-coordinates of points.
        y : Float1D
            array of y-coordinates of points.
        z : Float1D
            array of z-coordinates of points.
        
        Returns
        --------
        output : Short1D
            array of 16-bit (short) indices.
        """

    @overload
    @staticmethod
    def encode16(self, x: Float2D, y: Float2D, z: Float2D) -> Short2D:
        """
        Encodes specified points as 16-bit (short) indices.
        
        Parameters
        -----------
        x : Float2D
            array of x-coordinates of points.
        y : Float2D
            array of y-coordinates of points.
        z : Float2D
            array of z-coordinates of points.
        
        Returns
        --------
        output : Short2D
            array of 16-bit (short) indices.
        """

    @overload
    @staticmethod
    def encode16(self, x: Float3D, y: Float3D, z: Float3D) -> Short3D:
        """
        Encodes specified points as 16-bit (short) indices.
        
        Parameters
        -----------
        x : Float3D
            array of x-coordinates of points.
        y : Float3D
            array of y-coordinates of points.
        z : Float3D
            array of z-coordinates of points.
        
        Returns
        --------
        output : Short3D
            array of 16-bit (short) indices.
        """

    @staticmethod
    def main(self, args: String1D) -> None:
        """
    
        """
