from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class TriangleGroup:
    """
    A group of triangles that represents a triangulated surface.
    
    Triangles may be specified by providing an array of packed vertex
    (x,y,z) coordinates and an array of packed (i,j,k) vertex indices.
    Each triplet (i,j,k) of vertex indices corresponds to one triangle.
    
    Alternatively, triangles may be specified by providing only the array
    of packed vertex (x,y,z) coordinates. In this case, a vertex index is
    assigned automatically to each vertex.
    
    Normal vectors are computed for each vertex as an area-weighted
    average of the vectors normal to all triangles that reference that
    vertex with the same index. These area-weighted normal vectors are
    used in lighting.
    Danielle Schulte, Colorado School of Mines
    """

    @overload
    def __init__(self, vn: bool, xyz: Float1D) -> None:
        """
        Constructs a triangle group with specified vertex coordinates.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3. The number
        of triangles is nt = nv/3 = xyz.length/9.
        
        Normal vectors may be computed for either vertices or triangles.
        When computed for a vertex, a normal vector is the area-weighted
        average of the normal vectors for all triangles with that vertex.
        
        If no vertices have the same (x,y,z) coordinates, then vertex and
        triangle normal vectors are the same vectors, but triangle normal
        vectors are less costly to compute.
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for triangle normals.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        """

    @overload
    def __init__(self, vn: bool, xyz: Float1D, rgb: Float1D) -> None:
        """
        Constructs a triangle group with specified vertex coordinates.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3. The number
        of triangles is nt = nv/3 = xyz.length/9.
        
        The (r,g,b) components of colors are packed into the specified
        array rgb. The number of colors equals the number of vertices.
        
        Normal vectors may be computed for either vertices or triangles.
        When computed for a vertex, a normal vector is the area-weighted
        average of the normal vectors for all triangles with that vertex.
        
        If no vertices have the same (x,y,z) coordinates, then vertex and
        triangle normal vectors are the same vectors, but triangle normal
        vectors are less costly to compute.
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for triangle normals.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        rgb : Float1D
            array[3nv] of packed color components.
        """

    @overload
    def __init__(self, vn: bool, sx: Sampling, sy: Sampling,
                 z: Float2D) -> None:
        """
        Constructs a triangle group for a sampled function z = f(x,y).
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for triangle normals.
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
        Constructs a triangle group for a sampled function z = f(x,y).
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for triangle normals.
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
    def __init__(self, ijk: Int1D, xyz: Float1D) -> None:
        """
        Constructs a triangle group with specified vertex coordinates.
        
        Triangles are specified by triplets of vertex indices (i,j,k), one
        triplet per triangle, packed into the specified array of integers
        ijk. The number of triangles is nt = ijk.length/3.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        For any vertex with index iv, this method computes a normal vector
        as an area-weighted average of the normal vectors for all triangles
        specified with index iv.
        
        Parameters
        -----------
        ijk : Int1D
            array[3nt] of packed vertex indices.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        """

    @overload
    def __init__(self, xyz: Float1D, uvw: Float1D) -> None:
        """
        Constructs a triangle group with specified vertex coordinates.
        
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
    def __init__(self, ijk: Int1D, xyz: Float1D, uvw: Float1D) -> None:
        """
        Constructs a triangle group with specified vertex coordinates.
        
        Triangles are specified by triplets of vertex indices (i,j,k), one
        triplet per triangle, packed into the specified array of integers
        ijk. The number of triangles is nt = ijk.length/3.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        The (u,v,w) components of normal vectors are packed into the specified
        array uvw. The number of normal vectors equals the number of vertices.
        
        Parameters
        -----------
        ijk : Int1D
            array[3nt] of packed vertex indices.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        uvw : Float1D
            array[3nv] of packed normal vector components.
        """

    @overload
    def __init__(self, xyz: Float1D, uvw: Float1D, rgb: Float1D) -> None:
        """
        Constructs a triangle group with specified vertex coordinates
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
    def __init__(self, ijk: Int1D, xyz: Float1D, uvw: Float1D,
                 rgb: Float1D) -> None:
        """
        Constructs a triangle group with specified vertex coordinates
        and optional corresponding normal vectors and colors.
        
        Triangles are specified by triplets of vertex indices (i,j,k), one
        triplet per triangle, packed into the specified array of integers
        ijk. The number of triangles is nt = ijk.length/3.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3.
        
        The (u,v,w) components of normal vectors are packed into the specified
        array uvw. If not null, the number of normal vectors equals the number
        of vertices.
        
        The (r,g,b) components of colors are packed into the specified array
        rgb. If not null, the number of colors equals the number of vertices.
        
        Parameters
        -----------
        ijk : Int1D
            array[3nt] of packed vertex indices.
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
        Computes indices ijk for triangle vertex coordinates xyz.
        
        The (x,y,z) coordinates of vertices are packed into the specified
        array xyz. The number of vertices is nv = xyz.length/3. The number
        of triangles is nt = nv/3 = xyz.length/9.
        
        For each triangle, this method computes a triplet (i,j,k) of integer
        vertex indices. A vertex index is an integer in the range [0,nv-1].
        The (x,y,z) coordinates of a vertex with index iv are xyz[3iv+0],
        xyz[3iv+1] and xyz[3iv+2], respectively.
        
        The simplest indexing is the sequence {0, 1, 2, ..., nv-1}. In this
        case, indices are assigned sequentially, so that every vertex of
        every triangle has a different index.
        
        In non-sequential indexing, vertices with the same (x,y,z) coordinates
        are assigned the same index. Again, index vertices will be in the range
        [0,nv-1], but some integers in this range may not be used. Whereas
        sequential indexing would assign integers ia and ib to two vertices
        that have the same (x,y,z) coordinates, non-sequential indexing will
        assign the smaller index min(ia,ib) to both vertices; the larger index
        max(ia,ib) will be unused.
        
        Triplets of indices (i,j,k), one triplet per triangle, are packed
        into the returned array of integers ijk, which has length 3nt.
        
        Parameters
        -----------
        sequential : bool
            true, for sequential indexing; false, otherwise.
        xyz : Float1D
            array[3nv] of packed vertex coordinates.
        
        Returns
        --------
        output : Int1D
            an array[3nt] of packed vertex indices.
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the color of the triangles in this triangle group.
        Note that if per-vertex colors were specified when this triangle group was
        constructed, then the color specified here is not used.
        
        Parameters
        -----------
        color : Color
            the color.
        """
