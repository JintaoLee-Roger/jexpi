from typing import overload
from edu.mines.jtk.mapping import *


class SimpleFrame:
    """
    A simple frame for 3D graphics.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a simple frame with default parameters.
        Axes orientation defaults to x-right, y-out and z-down.
        """

    @overload
    def __init__(self, ao: AxesOrientation) -> None:
        """
        Constructs a simple frame with specified axes orientation.
        
        Parameters
        -----------
        ao : AxesOrientation
            the axes orientation.
        """

    @overload
    def __init__(self, world: World) -> None:
        """
        Constructs a simple frame with the specified world.
        
        Parameters
        -----------
        world : World
            the world view.
        """

    @overload
    def __init__(self, world: World, ao: AxesOrientation) -> None:
        """
        Constructs a simple frame with the specified world and orientation.
        
        Parameters
        -----------
        world : World
            the world view.
        ao : AxesOrientation
            the axes orientation.
        """

    def getModeManager(self) -> ModeManager:
        """
        Gets the mode manager for this simple frame.
        Returns
        --------
        output : ModeManager
            the mode manager.
        """

    def getJToolBar(self) -> JToolBar:
        """
        Gets the JToolBar for this simple frame.
        Returns
        --------
        output : JToolBar
            the JToolBar.
        """

    @overload
    @staticmethod
    def asTriangles(self, xyz: Float1D) -> SimpleFrame:
        """
        Returns a new simple frame with a triangle group.
        Triangles will be constructed as vertex normals.
        
        Parameters
        -----------
        xyz : Float1D
            array of packed vertex coordinates.
        
        Returns
        --------
        output : SimpleFrame
            a simple frame.
        """

    @overload
    @staticmethod
    def asTriangles(self, vn: bool, xyz: Float1D) -> SimpleFrame:
        """
        Returns a new simple frame with a triangle group.
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for triangle normals.
        xyz : Float1D
            array of packed vertex coordinates.
        
        Returns
        --------
        output : SimpleFrame
            the simple frame.
        """

    @overload
    @staticmethod
    def asTriangles(self, xyz: Float1D, rgb: Float1D) -> SimpleFrame:
        """
        Returns a new simple frame with a triangle group.
        Triangles will be constructed as vertex normals.
        
        Parameters
        -----------
        xyz : Float1D
            array of packed vertex coordinates.
        rgb : Float1D
            array of packed color coordinates.
        
        Returns
        --------
        output : SimpleFrame
            the simple frame.
        """

    @overload
    @staticmethod
    def asTriangles(self, vn: bool, sx: Sampling, sy: Sampling,
                    z: Float2D) -> SimpleFrame:
        """
        Returns a new simple frame with a triangle group.
        
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
    @staticmethod
    def asTriangles(self, vn: bool, sx: Sampling, sy: Sampling, z: Float2D,
                    r: Float2D, g: Float2D, b: Float2D) -> SimpleFrame:
        """
        Returns a new simple frame with a triangle group.
        
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
    @staticmethod
    def asTriangles(self, vn: bool, xyz: Float1D, rgb: Float1D) -> SimpleFrame:
        """
        Returns a new simple frame with a triangle group.
        
        Parameters
        -----------
        vn : bool
            true, for vertex normals; false, for triangle normals
        xyz : Float1D
            array of packed vertex coordinates.
        rgb : Float1D
            array of packed color coordinates.
        
        Returns
        --------
        output : SimpleFrame
            the simple frame.
        """

    @overload
    @staticmethod
    def asTriangles(self, tg: TriangleGroup) -> SimpleFrame:
        """
        Returns a new simple frame with a triangle group.
        
        Parameters
        -----------
        tg : TriangleGroup
            a triangle group.
        
        Returns
        --------
        output : SimpleFrame
            the simple frame.
        """

    @overload
    @staticmethod
    def asImagePanels(self, f: Float3D) -> SimpleFrame:
        """
        Returns a new simple frame with an image panel group.
        
        Parameters
        -----------
        f : Float3D
            a 3D array.
        
        Returns
        --------
        output : SimpleFrame
            the simple frame.
        """

    @overload
    @staticmethod
    def asImagePanels(self, s1: Sampling, s2: Sampling, s3: Sampling,
                      f: Float3D) -> SimpleFrame:
        """
        Returns a new simple frame with an image panel group.
        
        Parameters
        -----------
        s1 : Sampling
            sampling in the 1st dimension (Z).
        s2 : Sampling
            sampling in the 2nd dimension (Y).
        s3 : Sampling
            sampling in the 3rd dimension (X).
        f : Float3D
            a 3D array.
        
        Returns
        --------
        output : SimpleFrame
            the simple frame.
        """

    @overload
    @staticmethod
    def asImagePanels(self, ipg: ImagePanelGroup) -> SimpleFrame:
        """
        Returns a new simple frame with an image panel group.
        
        Parameters
        -----------
        ipg : ImagePanelGroup
            an image panel group.
        
        Returns
        --------
        output : SimpleFrame
            the simple frame.
        """

    @overload
    def addTriangles(self, xyz: Float1D) -> TriangleGroup:
        """
        Adds a triangle group with specified vertex coordinates.
        
        Parameters
        -----------
        xyz : Float1D
            array of packed vertex coordinates.
        
        Returns
        --------
        output : TriangleGroup
            the triangle group.
        """

    @overload
    def addTriangles(self, xyz: Float1D, rgb: Float1D) -> TriangleGroup:
        """
        Adds a triangle group with specified vertex coordinates and colors.
        
        Parameters
        -----------
        xyz : Float1D
            array of packed vertex coordinates.
        rgb : Float1D
            array of packed color components.
        
        Returns
        --------
        output : TriangleGroup
            the triangle group.
        """

    @overload
    def addTriangles(self, sx: Sampling, sy: Sampling,
                     z: Float2D) -> TriangleGroup:
        """
        Adds a triangle group for a sampled function z = f(x,y).
        
        Parameters
        -----------
        sx : Sampling
            sampling of x coordinates; may be non-uniform.
        sy : Sampling
            sampling of y coordinates; may be non-uniform.
        z : Float2D
            array[nx][ny] of z coordinates z = f(x,y).
        """

    @overload
    def addTriangles(self, tg: TriangleGroup) -> TriangleGroup:
        """
        Adds a triangle group to a simple frame from a given triangle group.
        
        Parameters
        -----------
        tg : TriangleGroup
            a triangle group.
        
        Returns
        --------
        output : TriangleGroup
            the attached triangle group.
        """

    @overload
    def addImagePanels(self, f: Float3D) -> ImagePanelGroup:
        """
        Adds an image panel group to a simple frame from a given 3D array
        
        Parameters
        -----------
        f : Float3D
            a 3D array.
        
        Returns
        --------
        output : ImagePanelGroup
            the image panel group.
        """

    @overload
    def addImagePanels(self, s1: Sampling, s2: Sampling, s3: Sampling,
                       f: Float3D) -> ImagePanelGroup:
        """
        Adds an image panel group to a simple frame from given samplings and
        a 3D array.
        
        Parameters
        -----------
        s1 : Sampling
            sampling in the 1st dimension (Z).
        s2 : Sampling
            sampling in the 2nd dimension (Y).
        s3 : Sampling
            sampling in the 3rd dimension (X).
        f : Float3D
            a 3D array.
        
        Returns
        --------
        output : ImagePanelGroup
            the image panel group.
        """

    @overload
    def addImagePanels(self, ipg: ImagePanelGroup) -> ImagePanelGroup:
        """
        Adds an image panel group to a simple frame from a given image panel
        group.
        
        Parameters
        -----------
        ipg : ImagePanelGroup
            an image panel group.
        
        Returns
        --------
        output : ImagePanelGroup
            the attached image panel group.
        """

    def getViewCanvas(self) -> ViewCanvas:
        """
        Gets the view canvas for this frame.
        Returns
        --------
        output : ViewCanvas
            the view canvas.
        """

    def getOrbitView(self) -> OrbitView:
        """
        Gets the orbit view for this frame.
        Returns
        --------
        output : OrbitView
            the orbit view.
        """

    def getWorld(self) -> World:
        """
        Gets the world for this frame.
        Returns
        --------
        output : World
            the world.
        """

    @overload
    def setWorldSphere(self, p: Point3, r: int) -> None:
        """
        Sets the bounding sphere of the frame with a given center point and
        radius.
        
        Parameters
        -----------
        p : Point3
            the center point.
        r : int
            the radius.
        """

    @overload
    def setWorldSphere(self, x: double, y: double, z: double,
                       r: double) -> None:
        """
        Sets the bounding sphere of the frame with a given center x, y, z and
        radius.
        
        Parameters
        -----------
        x : double
            the center X-coordinate.
        y : double
            the center Y-coordinate.
        z : double
            the center Z-coordinate.
        r : double
            the radius.
        """

    @overload
    def setWorldSphere(self, xmin: double, ymin: double, zmin: double,
                       xmax: double, ymax: double, zmax: double) -> None:
        """
        Sets the bounding sphere of the frame.
        
        Parameters
        -----------
        xmin : double
            the minimum x coordinate.
        ymin : double
            the minimum y coordinate.
        zmin : double
            the minimum z coordinate.
        xmax : double
            the maximum x coordinate.
        ymax : double
            the maximum y coordinate.
        zmax : double
            the maximum z coordinate.
        """

    @overload
    def setWorldSphere(self, bs: BoundingSphere) -> None:
        """
        Sets the bounding sphere of the frame.
        
        Parameters
        -----------
        bs : BoundingSphere
            the bounding sphere.
        """

    def paintToFile(self, fileName: String) -> None:
        """
        Paints the view canvas to an image in a file with specified name.
        Uses the file suffix to determine the format of the image.
        
        Parameters
        -----------
        fileName : String
            name of the file to contain the image.
        """
