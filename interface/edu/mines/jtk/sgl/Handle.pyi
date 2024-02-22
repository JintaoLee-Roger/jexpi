from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Handle:
    """
    A handle for manipulating other nodes. A handle is a special type of node,
    because its size in pixel coordinates is constant. A handle has the same
    pixel dimensions in all views (all contexts) in which it is rendered. This
    property makes handles suitable for selecting and dragging with a mouse or
    other pointing device.
    
    A handle maintains its constant pixel size by applying a context-dependent
    scaling to its children. A handle is much like a transform group, one that
    augments a specified transform with a context-dependent scaling.
    
    A consequence of this constant-size-in-pixels property is that a handle's
    bounding sphere in local coordinates must be infinite. A bounding sphere
    cannot be context-dependent, and the only sphere that is guaranteed to
    bound a handle in any context in which it appears is the infinite sphere.
    
    By convention, the geometry of a handle's node children is centered at the
    point (0,0,0). A handle first scales the bounding sphere of its children
    so that the radius of that sphere transforms to the handle pixel size. The
    handle then applies a specified transform to position and orient its
    children within its local coordinate system.
    
    A handle is a group node, because the child leaf nodes of each handle
    subclass are typically shared by instances of that subclass. Then, any
    changes to the shared node children are conveniently reflected in all
    handles of that class. Often a handle subclass has a single leaf node
    child.
    """

    @overload
    def __init__(self, transform: Matrix44) -> None:
        """
        Constructs a handle with specified transform matrix.
        
        Parameters
        -----------
        transform : Matrix44
            the transform matrix.
        """

    @overload
    def __init__(self, p: Point3) -> None:
        """
        Constructs a handle with specified center location.
        
        Parameters
        -----------
        p : Point3
            the center point.
        """

    @overload
    def __init__(self, x: double, y: double, z: double) -> None:
        """
        Constructs a handle with specified center coordinates.
        
        Parameters
        -----------
        x : double
            the center x coordinate.
        y : double
            the center y coordinate.
        z : double
            the center z coordinate.
        """

    @staticmethod
    def getSize(self) -> double:
        """
        Gets the size in pixels of all handles.
        Returns
        --------
        output : double
            the size.
        """

    @staticmethod
    def setSize(self, size: double) -> None:
        """
        Sets the size in pixels of all handles. Because handle size is not
        associated with any particular handle or world, this method does
        force a repaint of any view canvases in which handles appear.
        
        Parameters
        -----------
        size : double
            the size.
        """

    def getTransform(self) -> Matrix44:
        """
        Gets the view-independent transform matrix for this handle.
        This transform does not include the view-dependent scaling that is
        applied to the handle's geometry <em>before</em> the transform.
        Returns
        --------
        output : Matrix44
            the transform.
        """

    def setTransform(self, transform: Matrix44) -> None:
        """
        Sets the view-independent transform matrix for this handle.
        This transform does not include the view-dependent scaling that is
        applied to the handle's geometry <em>before</em> the transform.
        
        Parameters
        -----------
        transform : Matrix44
            the transform.
        """

    def getLocation(self) -> Point3:
        """
        Gets the view-independent location of the center of this handle.
        Returns
        --------
        output : Point3
            the center point.
        """

    @overload
    def setLocation(self, p: Point3) -> None:
        """
        Sets the view-independent location of the center of this handle.
        This method conveniently sets the handle transform to a pure
        translation to the specified center point.
        
        Parameters
        -----------
        p : Point3
            the center point.
        """

    @overload
    def setLocation(self, x: double, y: double, z: double) -> None:
        """
        Sets the view-independent location of the center of this handle.
        This method conveniently sets the handle transform to a pure
        translation to the center point with specified coordinates.
        
        Parameters
        -----------
        x : double
            the center x coordinate.
        y : double
            the center y coordinate.
        z : double
            the center z coordinate.
        """
