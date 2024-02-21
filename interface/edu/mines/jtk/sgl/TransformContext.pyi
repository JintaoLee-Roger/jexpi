from typing import overload
from edu.mines.jtk.mapping import *


class TransformContext:
    """
    A traversal context with coordinate transforms.
    
    A transform context maintains transforms for converting coordinates
    among five different coordinate systems:
    <dl>
    <dt>local</dt><dd>
    the local coordinate system for a node in the scene graph. Vertex
    coordinates for a node are specified in a local system, which may
    or may not be the same as the world coordinate system. Two nodes
    with the same local vertex coordinates (or even a single node) may
    appear in different locations, corresponding to different world
    coordinates.
    </dd>
    <dt>world</dt><dd>
    the coordinate system for the world (root) node of the scene graph.
    A local-to-world transform puts all nodes in the same one world
    coordinate system. World coordinates are independent of any view
    of the world.
    </dd>
    <dt>view</dt><dd>
    a right-handed coordinate system in which the eye or camera is located
    at the origin, looking down the negative z axis, with the positive y
    axis up and the positive x axis right. A world-to-view transform
    typically pushes the world away from the camera, down the negative z
    axis. As the name implies, view coordinates depend on the view.
    </dd>
    <dt>cube</dt><dd>
    a left-handed, normalized coordinate system with six clipping planes.
    In this coordinate system,
    x = -1 and x = 1 correspond to the left and right planes,
    y = -1 and y = 1 correspond to the bottom and top planes, and
    z = -1 and z = 1 correspond to the near and far planes.
    A view-to-cube transform corresponds to a view's projection;
    e.g., perspective or orthographic.
    </dd>
    <dt>pixel</dt><dd>
    typically, a right-handed coordinate system in which x and y coordinates
    are window coordinates. For a window with width w and height h,
    x = 0 and x = w-1 correspond to the leftmost and rightmost pixels, and
    y = 0 and y = h-1 correspond to the topmost and bottommost pixels.
    The pixel z (depth) coordinate is a floating point number, where
    z = 0.0 and z = 1.0 correspond to the near and far clipping planes.
    A cube-to-pixel transform typically depends on the dimensions of the
    window in which a scene is rendered.
    </dd>
    </dl>
    
    When traversing the scenegraph, the world-to-view, view-to-cube, and
    cube-to-pixel transforms do not change. However, nodes that transform
    coordinates will push, modify, and pop the local-to-world transform,
    using the methods {@link #pushLocalToWorld(Matrix44)} and
    """

    def __init__(self, canvas: ViewCanvas) -> None:
        """
        Constructs a transform context for the specified view canvas.
        Gets its view-to-cube and cube-to-pixel transforms from the
        canvas. Gets its world-to-view transform from the view drawn
        on that canvas, and sets the local-to-world transform to the
        identity matrix.
        
        Parameters
        -----------
        canvas : ViewCanvas
            the view canvas.
        """

    def getViewCanvas(self) -> ViewCanvas:
        """
        Gets the canvas for which this transform context was constructed.
        Returns
        --------
        output : ViewCanvas
            the view canvas.
        """

    def getView(self) -> View:
        """
        Gets the view for which this transform context was constructed.
        Returns
        --------
        output : View
            the view.
        """

    def getWorld(self) -> World:
        """
        Gets the world for which this transform context was constructed.
        Returns
        --------
        output : World
            the world.
        """

    def getLocalToWorld(self) -> Matrix44:
        """
        Gets the local-to-world transform.
        Returns
        --------
        output : Matrix44
            the local-to-world transform.
        """

    def getWorldToLocal(self) -> Matrix44:
        """
        Gets the world-to-local transform.
        Returns
        --------
        output : Matrix44
            the world-to-local transform.
        """

    def getLocalToView(self) -> Matrix44:
        """
        Gets the local-to-view transform.
        Returns
        --------
        output : Matrix44
            the local-to-view transform.
        """

    def getViewToLocal(self) -> Matrix44:
        """
        Gets the view-to-local transform.
        Returns
        --------
        output : Matrix44
            the view-to-local transform.
        """

    def getLocalToCube(self) -> Matrix44:
        """
        Gets the local-to-cube transform.
        Returns
        --------
        output : Matrix44
            the local-to-cube transform.
        """

    def getCubeToLocal(self) -> Matrix44:
        """
        Gets the cube-to-local transform.
        Returns
        --------
        output : Matrix44
            the cube-to-local transform.
        """

    def getLocalToPixel(self) -> Matrix44:
        """
        Gets the local-to-pixel transform.
        Returns
        --------
        output : Matrix44
            the local-to-pixel transform.
        """

    def getPixelToLocal(self) -> Matrix44:
        """
        Gets the pixel-to-local transform.
        Returns
        --------
        output : Matrix44
            the pixel-to-local transform.
        """

    def getWorldToView(self) -> Matrix44:
        """
        Gets the world-to-view transform.
        Returns
        --------
        output : Matrix44
            the world-to-view transform.
        """

    def getViewToWorld(self) -> Matrix44:
        """
        Gets the view-to-world transform.
        Returns
        --------
        output : Matrix44
            the view-to-world transform.
        """

    def getWorldToCube(self) -> Matrix44:
        """
        Gets the world-to-cube transform.
        Returns
        --------
        output : Matrix44
            the world-to-cube transform.
        """

    def getCubeToWorld(self) -> Matrix44:
        """
        Gets the cube-to-world transform.
        Returns
        --------
        output : Matrix44
            the cube-to-world transform.
        """

    def getWorldToPixel(self) -> Matrix44:
        """
        Gets the world-to-pixel transform.
        Returns
        --------
        output : Matrix44
            the world-to-pixel transform.
        """

    def getPixelToWorld(self) -> Matrix44:
        """
        Gets the pixel-to-world transform.
        Returns
        --------
        output : Matrix44
            the pixel-to-world transform.
        """

    def getViewToCube(self) -> Matrix44:
        """
        Gets the view-to-cube transform.
        Returns
        --------
        output : Matrix44
            the view-to-cube transform.
        """

    def getCubeToView(self) -> Matrix44:
        """
        Gets the cube-to-view transform.
        Returns
        --------
        output : Matrix44
            the cube-to-view transform.
        """

    def getViewToPixel(self) -> Matrix44:
        """
        Gets the view-to-pixel transform.
        Returns
        --------
        output : Matrix44
            the view-to-pixel transform.
        """

    def getPixelToView(self) -> Matrix44:
        """
        Gets the pixel-to-view transform.
        Returns
        --------
        output : Matrix44
            the pixel-to-view transform.
        """

    def getCubeToPixel(self) -> Matrix44:
        """
        Gets the cube-to-pixel transform.
        Returns
        --------
        output : Matrix44
            the cube-to-pixel transform.
        """

    def getPixelToCube(self) -> Matrix44:
        """
        Gets the pixel-to-cube transform.
        Returns
        --------
        output : Matrix44
            the pixel-to-cube transform.
        """

    def pushLocalToWorld(self, transform: Matrix44) -> None:
        """
        Saves the local-to-world transform before appending a transform.
        The specified transform matrix is post-multiplied with the current
        local-to-world transform, such that the specified transform is applied
        first when transforming local coordinates to world coordinates.
        
        Parameters
        -----------
        transform : Matrix44
            the transform to append.
        """

    def popLocalToWorld(self) -> None:
        """
        Restores the most recently saved (pushed) local-to-world transform.
        Discards the current local-to-world transform.
        """
