from typing import overload
from java.awt import *
from edu.mines.jtk.mapping import *


class MaterialState:
    """
    OpenGL material state.
    
    When applied, this state enables GL_LIGHTING, always.
    """

    def __init__(self) -> None:
        """
        Constructs material state.
        """

    def hasAmbientFront(self) -> bool:
        """
        Determines whether ambient color for front faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def hasAmbientBack(self) -> bool:
        """
        Determines whether ambient color for back faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getAmbientFront(self) -> Color:
        """
        Gets the ambient color for front faces.
        Returns
        --------
        output : Color
            the ambient color.
        """

    def getAmbientBack(self) -> Color:
        """
        Gets the ambient color for back faces.
        Returns
        --------
        output : Color
            the ambient color.
        """

    def setAmbient(self, ambient: Color) -> None:
        """
        Sets the ambient color for front and back faces.
        
        Parameters
        -----------
        ambient : Color
            the ambient color.
        """

    def setAmbientFront(self, ambient: Color) -> None:
        """
        Sets the ambient color for front faces.
        
        Parameters
        -----------
        ambient : Color
            the ambient color.
        """

    def setAmbientBack(self, ambient: Color) -> None:
        """
        Sets the ambient color for back faces.
        
        Parameters
        -----------
        ambient : Color
            the ambient color.
        """

    def unsetAmbient(self) -> None:
        """
        Unsets the ambient color for front and back faces.
        """

    def unsetAmbientFront(self) -> None:
        """
        Unsets the ambient color for front faces.
        """

    def unsetAmbientBack(self) -> None:
        """
        Unsets the ambient color for back faces.
        """

    def hasDiffuseFront(self) -> bool:
        """
        Determines whether diffuse color for front faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def hasDiffuseBack(self) -> bool:
        """
        Determines whether diffuse color for back faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getDiffuseFront(self) -> Color:
        """
        Gets the diffuse color for front faces.
        Returns
        --------
        output : Color
            the diffuse color.
        """

    def getDiffuseBack(self) -> Color:
        """
        Gets the diffuse color for back faces.
        Returns
        --------
        output : Color
            the diffuse color.
        """

    def setDiffuse(self, diffuse: Color) -> None:
        """
        Sets the diffuse color for front and back faces.
        
        Parameters
        -----------
        diffuse : Color
            the diffuse color.
        """

    def setDiffuseFront(self, diffuse: Color) -> None:
        """
        Sets the diffuse color for front faces.
        
        Parameters
        -----------
        diffuse : Color
            the diffuse color.
        """

    def setDiffuseBack(self, diffuse: Color) -> None:
        """
        Sets the diffuse color for back faces.
        
        Parameters
        -----------
        diffuse : Color
            the diffuse color.
        """

    def unsetDiffuse(self) -> None:
        """
        Unsets the diffuse color for front and back faces.
        """

    def unsetDiffuseFront(self) -> None:
        """
        Unsets the diffuse color for front faces.
        """

    def unsetDiffuseBack(self) -> None:
        """
        Unsets the diffuse color for back faces.
        """

    def hasSpecularFront(self) -> bool:
        """
        Determines whether specular color for front faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def hasSpecularBack(self) -> bool:
        """
        Determines whether specular color for back faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getSpecularFront(self) -> Color:
        """
        Gets the specular color for front faces.
        Returns
        --------
        output : Color
            the specular color.
        """

    def getSpecularBack(self) -> Color:
        """
        Gets the specular color for back faces.
        Returns
        --------
        output : Color
            the specular color.
        """

    def setSpecular(self, specular: Color) -> None:
        """
        Sets the specular color for front and back faces.
        
        Parameters
        -----------
        specular : Color
            the specular color.
        """

    def setSpecularFront(self, specular: Color) -> None:
        """
        Sets the specular color for front faces.
        
        Parameters
        -----------
        specular : Color
            the specular color.
        """

    def setSpecularBack(self, specular: Color) -> None:
        """
        Sets the specular color for back faces.
        
        Parameters
        -----------
        specular : Color
            the specular color.
        """

    def unsetSpecular(self) -> None:
        """
        Unsets the specular color for front and back faces.
        """

    def unsetSpecularFront(self) -> None:
        """
        Unsets the specular color for front faces.
        """

    def unsetSpecularBack(self) -> None:
        """
        Unsets the specular color for back faces.
        """

    def hasEmissiveFront(self) -> bool:
        """
        Determines whether emissive color for front faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def hasEmissiveBack(self) -> bool:
        """
        Determines whether emissive color for back faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getEmissiveFront(self) -> Color:
        """
        Gets the emissive color for front faces.
        Returns
        --------
        output : Color
            the emissive color.
        """

    def getEmissiveBack(self) -> Color:
        """
        Gets the emissive color for back faces.
        Returns
        --------
        output : Color
            the emissive color.
        """

    def setEmissive(self, emissive: Color) -> None:
        """
        Sets the emissive color for front and back faces.
        
        Parameters
        -----------
        emissive : Color
            the emissive color.
        """

    def setEmissiveFront(self, emissive: Color) -> None:
        """
        Sets the emissive color for front faces.
        
        Parameters
        -----------
        emissive : Color
            the emissive color.
        """

    def setEmissiveBack(self, emissive: Color) -> None:
        """
        Sets the emissive color for back faces.
        
        Parameters
        -----------
        emissive : Color
            the emissive color.
        """

    def unsetEmissive(self) -> None:
        """
        Unsets the emissive color for front and back faces.
        """

    def unsetEmissiveFront(self) -> None:
        """
        Unsets the emissive color for front faces.
        """

    def unsetEmissiveBack(self) -> None:
        """
        Unsets the emissive color for back faces.
        """

    def hasShininessFront(self) -> bool:
        """
        Determines whether shininess for front faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def hasShininessBack(self) -> bool:
        """
        Determines whether shininess for back faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getShininessFront(self) -> float:
        """
        Gets the shininess for front faces.
        Returns
        --------
        output : float
            the shininess.
        """

    def getShininessBack(self) -> float:
        """
        Gets the shininess for back faces.
        Returns
        --------
        output : float
            the shininess.
        """

    def setShininess(self, shininess: float) -> None:
        """
        Sets the shininess for front and back faces.
        
        Parameters
        -----------
        shininess : float
            the shininess.
        """

    def setShininessFront(self, shininess: float) -> None:
        """
        Sets the shininess for front faces.
        
        Parameters
        -----------
        shininess : float
            the shininess.
        """

    def setShininessBack(self, shininess: float) -> None:
        """
        Sets the shininess for back faces.
        
        Parameters
        -----------
        shininess : float
            the shininess.
        """

    def unsetShininess(self) -> None:
        """
        Unsets the shininess for front and back faces.
        """

    def unsetShininessFront(self) -> None:
        """
        Unsets the shininess for front faces.
        """

    def unsetShininessBack(self) -> None:
        """
        Unsets the shininess for back faces.
        """

    def hasColorMaterialFront(self) -> bool:
        """
        Determines whether color material mode for front faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def hasColorMaterialBack(self) -> bool:
        """
        Determines whether color material mode for back faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getColorMaterialFront(self) -> int:
        """
        Gets the color material mode for front faces.
        Returns
        --------
        output : int
            the color material mode.
        """

    def getColorMaterialBack(self) -> int:
        """
        Gets the color material mode for back faces.
        Returns
        --------
        output : int
            the color material mode.
        """

    def setColorMaterial(self, mode: int) -> None:
        """
        Sets the color material mode for front and back faces.
        
        Parameters
        -----------
        mode : int
            the color material mode.
        """

    def setColorMaterialFront(self, mode: int) -> None:
        """
        Sets the color material mode for front faces.
        
        Parameters
        -----------
        mode : int
            the color material mode.
        """

    def setColorMaterialBack(self, mode: int) -> None:
        """
        Sets the color material mode for back faces.
        
        Parameters
        -----------
        mode : int
            the color material mode.
        """

    def unsetColorMaterial(self) -> None:
        """
        Unsets the color material mode for front and back faces.
        """

    def unsetColorMaterialFront(self) -> None:
        """
        Unsets the color material mode for front faces.
        """

    def unsetColorMaterialBack(self) -> None:
        """
        Unsets the color material mode for back faces.
        """

    def apply(self) -> None:
        """
    
        """

    def getAttributeBits(self) -> int:
        """
    
        """
