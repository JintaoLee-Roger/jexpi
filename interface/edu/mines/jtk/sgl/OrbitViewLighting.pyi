from typing import overload
from edu.mines.jtk.mapping import *


class OrbitViewLighting:
    """
    Lighting for {@link edu.mines.jtk.sgl.OrbitView}.
    There are three light sources available within the JTK, and
    each light can be individually positioned in the canvas and have color
    properties assigned. Furthermore, each light can be defined to be one of
    two types:
    <ol>
    <li>
    Directional light (default): the light source placed at an infinite
    distance and all light rays are parallel.
    </li>
    <li>
    Positional light: the light source is positioned in the frustum and
    light rays extend spherically in all directions.
    </li>
    </ol>
    The default scene lighting matches the previously-hardwired lighting
    setup used by the JTK, that is a single <em>directional</em> light
    positioned at <code>(-0.1,-0.1, 0.0)</code> with black ambient light, and
    white specular and diffuse lights. This light is considered to be
    the "primary light".
    """

    def __init__(self) -> None:
        """
        Constructs an OrbitView Lighting
        """

    @overload
    def toggleLight(self, i: int) -> None:
        """
        Toggles a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2]
        """

    @overload
    def toggleLight(self) -> None:
        """
        Toggles the primary light source.
        """

    def setLight(self, i: int, isOn: bool) -> None:
        """
        Sets the state of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2]
        isOn : bool
            true, if light is on; false, otherwise.
        """

    @overload
    def isLightOn(self) -> bool:
        """
        Determines if the primary light source is on.
        Returns
        --------
        output : bool
            true, if light source is on; false, otherwise.
        """

    @overload
    def isLightOn(self, i: int) -> bool:
        """
        Determines if a light source is on.
        
        Parameters
        -----------
        i : int
            a light source [0-2]
        
        Returns
        --------
        output : bool
            true, if light is on; false, otherwise.
        """

    @overload
    def setAmbient(self, rgba: Float1D) -> None:
        """
        Sets the ambient color of the primary light source.
        
        Parameters
        -----------
        rgba : Float1D
            array[4] of color components.
        """

    @overload
    def setAmbient(self, i: int, rgba: Float1D) -> None:
        """
        Sets the ambient color of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        rgba : Float1D
            array[4] of color components.
        """

    @overload
    def getAmbient(self) -> Float1D:
        """
        Gets the ambient color of the primary light source.
        Returns
        --------
        output : Float1D
            ambient color of the primary light source.
        """

    @overload
    def getAmbient(self, i: int) -> Float1D:
        """
        Gets the ambient color of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        
        Returns
        --------
        output : Float1D
            ambient color of the light source.
        """

    @overload
    def setSpecular(self, rgba: Float1D) -> None:
        """
        Sets the specular color of the primary light source.
        
        Parameters
        -----------
        rgba : Float1D
            array[4] of color components.
        """

    @overload
    def setSpecular(self, i: int, rgba: Float1D) -> None:
        """
        Sets the specular color of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        rgba : Float1D
            specular color of a light source.
        """

    @overload
    def getSpecular(self) -> Float1D:
        """
        Gets the specular color of the primary light source.
        Returns
        --------
        output : Float1D
            the specular color of the primary light source.
        """

    @overload
    def getSpecular(self, i: int) -> Float1D:
        """
        Gets the specular color of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        
        Returns
        --------
        output : Float1D
            specular color of a light source.
        """

    @overload
    def setDiffuse(self, rgba: Float1D) -> None:
        """
        Sets the diffuse color of the primary light source.
        
        Parameters
        -----------
        rgba : Float1D
            diffuse color of the primary light source.
        """

    @overload
    def setDiffuse(self, i: int, rgba: Float1D) -> None:
        """
        Sets the diffuse color of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        rgba : Float1D
            diffuse color of a light source.
        """

    @overload
    def getDiffuse(self) -> Float1D:
        """
        Gets the diffuse color of the primary light source.
        Returns
        --------
        output : Float1D
            diffuse color of the primary light source.
        """

    @overload
    def getDiffuse(self, i: int) -> Float1D:
        """
        Gets the diffuse color of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        
        Returns
        --------
        output : Float1D
            diffuse color of a light source.
        """

    @overload
    def setAmbientAndDiffuse(self, rgba: Float1D) -> None:
        """
        Sets the ambient and diffuse colors of the primary light source.
        
        Parameters
        -----------
        rgba : Float1D
            array[4] of color components.
        """

    @overload
    def setAmbientAndDiffuse(self, i: int, rgba: Float1D) -> None:
        """
        Sets the ambient and diffuse colors of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        rgba : Float1D
            array[4] of color components.
        """

    @overload
    def setPosition(self, lx: float, ly: float, lz: float) -> None:
        """
        Sets the position of the primary light source.
        
        Parameters
        -----------
        lx : float
            the x-coordinate.
        ly : float
            the y-coordinate.
        lz : float
            the z-coordinate.
        """

    @overload
    def setPosition(self, pos: Float1D) -> None:
        """
        Sets the position of the primary light source.
        
        Parameters
        -----------
        pos : Float1D
            array[3] of (x,y,z) coordinates.
        """

    @overload
    def getPosition(self) -> Float1D:
        """
        Gets the position of the primary light source.
        Returns
        --------
        output : Float1D
            the (x,y,z,w) coordinates of the primary light source.
        """

    @overload
    def setPosition(self, i: int, lx: float, ly: float, lz: float) -> None:
        """
        Sets the position of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        lx : float
            the x-coordinate.
        ly : float
            the y-coordinate.
        lz : float
            the z-coordinate.
        """

    @overload
    def setPosition(self, i: int, pos: Float1D) -> None:
        """
        Sets the position of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        pos : Float1D
            array[4] containing (x,y,z,w) coordinates.
        """

    @overload
    def getPosition(self, i: int) -> Float1D:
        """
        Gets the position of a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        
        Returns
        --------
        output : Float1D
            the (x,y,z,w) position of the light source.
        """

    @overload
    def setLightSourceType(self, type: LightSourceType) -> None:
        """
        Sets the {@link LightSourceType} for the primary light source.
        
        Parameters
        -----------
        type : LightSourceType
            a {@link LightSourceType}.
        """

    @overload
    def setLightSourceType(self, i: int, type: LightSourceType) -> None:
        """
        Sets the {@link LightSourceType} for a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        type : LightSourceType
            a {@link LightSourceType}.
        """

    @overload
    def getLightSourceType(self) -> LightSourceType:
        """
        Gets the {@link LightSourceType} for the primary light source.
        Returns
        --------
        output : LightSourceType
            the {@link LightSourceType}.
        """

    @overload
    def getLightSourceType(self, i: int) -> LightSourceType:
        """
        Gets the {@link LightSourceType} for a light source.
        
        Parameters
        -----------
        i : int
            a light source [0-2].
        
        Returns
        --------
        output : LightSourceType
            a {@link LightSourceType}.
        """

    def draw(self) -> None:
        """
    
        """

    def equals(self, o: Object) -> bool:
        """
    
        """

    def hashCode(self) -> int:
        """
    
        """
