from typing import overload
from java.awt import *
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import *


class QuadGroup:
    """
    A group of quads that represents a surface.
    
    Quads may be specified by providing an array of packed vertex
    (x,y,z) coordinates and an array of packed (i,j,k,l) vertex indices.
    Each set (i,j,k,l) of four vertex indices corresponds to one quad.
    
    Alternatively, quads may be specified by providing only the array
    of packed vertex (x,y,z) coordinates. In this case, a vertex index is
    assigned automatically to each vertex.
    
    Normal vectors are computed for each vertex as an area-weighted
    average of the vectors normal to all quads that reference that
    vertex with the same index. These area-weighted normal vectors are
    used in lighting.
    """

    @overload
    def __init__(self, vn: bool, xyz: Float1D) -> None:
        """
        Constructs a quad group with specified vertex coordinates.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3. The number
        of quads is nq = nv/4 = xyz.length/12.
        
        Normal vectors may be computed for either vertices or quads.
        When computed for a vertex, a normal vector is the area-weighted
        average of the normal vectors for all quads with that vertex.
        
        If no vertices have the same (x,y,z) coordinates, then vertex and
        quad normal vectors are the same vectors, but quad normal vectors
        are less costly to compute.
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for quad normals.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        """

    @overload
    def __init__(self, vn: bool, xyz: Float1D, rgb: Float1D) -> None:
        """
        Constructs a quad group with specified vertex coordinates.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3. The number
        of quads is nq = nv/4 = xyz.length/12.
        
        The (r,g,b) components of colors are packed into the specified
        array rgb. The number of colors equals the number of vertices.
        
        Normal vectors may be computed for either vertices or quads.
        When computed for a vertex, a normal vector is the area-weighted
        average of the normal vectors for all quads with that vertex.
        
        If no vertices have the same (x,y,z) coordinates, then vertex and
        quad normal vectors are the same vectors, but quad normal vectors
        are less costly to compute.
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for quad normals.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        rgb : Float1D
            array[3nv] of packed color components.
        """

    @overload
    def __init__(self, vn: bool, sx: Sampling, sy: Sampling,
                 z: Float2D) -> None:
        """
        Constructs a quad group for a sampled function z = f(x,y).
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for quad normals.
        sx : Sampling
            sampling of x coordinates; may be non-uniform.
        sy : Sampling
            sampling of y coordinates; may be non-uniform.
        z : Float2D
            array[nx][ny] of z coordinates z = f(x,y).
        """

    @overload
    def __init__(self, vn: bool, sx: Sampling, sy: Sampling, z: Float2D,
                 r: Float2D, g: Float2D, b: Float2D) -> None:
        """
        Constructs a quad group for a sampled function z = f(x,y).
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for quad normals.
        sx : Sampling
            sampling of x coordinates; may be non-uniform.
        sy : Sampling
            sampling of y coordinates; may be non-uniform.
        z : Float2D
            array[nx][ny] of z coordinates z = f(x,y).
        r : Float2D
            array[nx][ny] of red color components.
        g : Float2D
            array[nx][ny] of green color components.
        b : Float2D
            array[nx][ny] of blue color components.
        """

    @overload
    def __init__(self, ijkl: Int1D, xyz: Float1D) -> None:
        """
        Constructs a quad group with specified vertex coordinates.
        
        Quads are specified by sets of four vertex indices (i,j,k,l),
        one set per quad, packed into the specified array of integers
        ijkl. The number of quads is nq = ijkl.length/4.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        For any vertex with index iv, this method computes a normal vector
        as an area-weighted average of the normal vectors for all quads
        specified with index iv.
        
        Parameters
        -----------
        ijkl : Int1D
            array[4nq] of packed vertex indices.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        """

    @overload
    def __init__(self, xyz: Float1D, uvw: Float1D) -> None:
        """
        Constructs a quad group with specified vertex coordinates.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        The (u,v,w) components of normal vectors are packed into the specified
        array uvw. The number of normal vectors equals the number of vertices.
        
        Parameters
        -----------
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        uvw : Float1D
            array[3nv] of packed normal vector components.
        """

    @overload
    def __init__(self, ijkl: Int1D, xyz: Float1D, uvw: Float1D) -> None:
        """
        Constructs a quad group with specified vertex coordinates.
        
        Quads are specified by sets of four vertex indices (i,j,k,l),
        one set per quad, packed into the specified array of integers
        ijkl. The number of quads is nq = ijkl.length/4.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        The (u,v,w) components of normal vectors are packed into the specified
        array uvw. The number of normal vectors equals the number of vertices.
        
        Parameters
        -----------
        ijkl : Int1D
            array[4nq] of packed vertex indices.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        uvw : Float1D
            array[3nv] of packed normal vector components.
        """

    @overload
    def __init__(self, xyz: Float1D, uvw: Float1D, rgb: Float1D) -> None:
        """
        Constructs a quad group with specified vertex coordinates
        and optional corresponding normal vectors and colors.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        The (u,v,w) components of normal vectors are packed into the specified
        array uvw. The number of normal vectors equals the number of vertices.
        
        The (r,g,b) components of colors are packed into the specified array
        rgb. The number of colors equals the number of vertices.
        
        Parameters
        -----------
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        uvw : Float1D
            array[3nv] of packed normal vector components.
        rgb : Float1D
            array[3nv] of packed color components.
        """

    @overload
    def __init__(self, ijkl: Int1D, xyz: Float1D, uvw: Float1D,
                 rgb: Float1D) -> None:
        """
        Constructs a quad group with specified vertex coordinates
        and optional corresponding normal vectors and colors.
        
        Quads are specified by sets of four vertex indices (i,j,k),
        one set per quad, packed into the specified array of integers
        ijkl. The number of quads is nq = ijkl.length/4.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        The (u,v,w) components of normal vectors are packed into the specified
        array uvw. If not null, the number of normal vectors equals the number
        of vertices.
        
        The (r,g,b) components of colors are packed into the specified array
        rgb. If not null, the number of colors equals the number of vertices.
        
        Parameters
        -----------
        ijkl : Int1D
            array[4nq] of packed vertex indices.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        uvw : Float1D
            array[3nv] of packed normal vector components.
        rgb : Float1D
            array[3nv] of packed color components.
        """

    @staticmethod
    def indexVertices(self, sequential: bool, xyz: Float1D) -> Int1D:
        """
        Computes indices ijkl for quad vertex coordinates xyz.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3. The number
        of quads is nq = nv/4 = xyz.length/12.
        
        For each quad, this method computes a set (i,j,k,l) of integer
        vertex indices. A vertex index is an integer in the range [0,nv-1].
        The (x,y,z) coordinates of a vertex with index iv are xyz[3iv+0],
        xyz[3iv+1] and xyz[3iv+2], respectively.
        
        The simplest indexing is the sequence {0, 1, 2, ..., nv-1}. In this
        case, indices are assigned sequentially, so that every vertex of
        every quad has a different index.
        
        In non-sequential indexing, vertices with the same (x,y,z) coordinates
        are assigned the same index. Again, index vertices will be in the range
        [0,nv-1], but some integers in this range may not be used. Whereas
        sequential indexing would assign integers ia and ib to two vertices
        that have the same (x,y,z) coordinates, non-sequential indexing will
        assign the smaller index min(ia,ib) to both vertices; the larger index
        max(ia,ib) will be unused.
        
        Sets of four indices (i,j,k,l), one set per quad, are packed
        into the returned array of integers ijkl, which has length 4nq.
        
        Parameters
        -----------
        sequential : bool
            true, for sequential indexing; false, otherwise.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        
        Returns
        --------
        output : Int1D
            an array[4nq] of packed vertex indices.
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the color of the quads in this quad group.
        Note that if per-vertex colors were specified when this quad
        group was constructed, then the color specified here is not used.
        
        Parameters
        -----------
        color : Color
            the color.
        """
