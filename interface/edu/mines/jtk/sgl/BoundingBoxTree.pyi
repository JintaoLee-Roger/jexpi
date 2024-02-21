from typing import overload
from edu.mines.jtk.mapping import *


class BoundingBoxTree:
    """
    A binary tree of axis-aligned bounding boxes for an array of points.
    This tree is useful when constructing a bounding volume hierarchy for
    large sets of geometric primitives such as triangles or quads.
    
    Each node in the tree contains a bounding box for a a subset of points.
    Those points are represented by a subarray of indices of point (x,y,z)
    coordinates. Point coordinates are specified when constructing a tree.
    
    The bounding box for the root node is that for the entire set of points,
    with indices 0 through n-1, where n is the total number of points in the
    tree. The tree recursively splits this bounding box in two so that each
    child represents roughly half of the points in its parent.
    
    This recursive splitting continues while splits will create child nodes
    with numbers of points not less than a specified minimum. When the total
    number of points in the tree is less than the specified minimum, then the
    tree consists of only the root node.
    
    A bounding box tree is much like a k-d tree for k=3 dimensions.
    """

    @overload
    def __init__(self, minSize: int, xyz: Float1D) -> None:
        """
        Constructs a bounding box tree for points with specified coordinates.
        The (x,y,z) coordinates are packed into the specified array such
        that (xyz[0],xyz[1],xyz[2]) are the (x,y,z) coordinates of the
        1st point, (xyz[3],xyz[4],xyz[5]) are the (x,y,z) coordinates of
        the 2nd point, and so on.
        
        Parameters
        -----------
        minSize : int
            the minimum number of points in a child node.
        xyz : Float1D
            array of packed (x,y,z) coordinates.
        """

    @overload
    def __init__(self, minSize: int, x: Float1D, y: Float1D,
                 z: Float1D) -> None:
        """
        Constructs a bounding box tree for points with specified coordinates.
        
        Parameters
        -----------
        minSize : int
            the minimum number of points in a child node.
        x : Float1D
            array of x coordinates.
        y : Float1D
            array of y coordinates.
        z : Float1D
            array of z coordinates.
        """

    def getRoot(self) -> Node:
        """
        Gets the root node of this tree.
        Returns
        --------
        output : Node
            the root node.
        """
