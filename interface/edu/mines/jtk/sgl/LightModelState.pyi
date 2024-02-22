from typing import overload
from java.awt import *
from edu.mines.jtk.mapping import *


class LightModelState:
    """
    OpenGL light model state.
    """

    def __init__(self) -> None:
        """
        Constructs light model state.
        """

    def hasAmbient(self) -> bool:
        """
        Determines whether the ambient color attribute is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getAmbient(self) -> Color:
        """
        Gets the ambient color attribute.
        Returns
        --------
        output : Color
            the ambient color.
        """

    def setAmbient(self, color: Color) -> None:
        """
        Sets the ambient color attribute.
        
        Parameters
        -----------
        color : Color
            the ambient color.
        """

    def unsetAmbient(self) -> None:
        """
        Unsets the ambient color attribute.
        """

    def hasColorControl(self) -> bool:
        """
        Determines whether the color control attribute is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getColorControl(self) -> int:
        """
        Gets the color control attribute.
        Returns
        --------
        output : int
            the color control.
        """

    def setColorControl(self, control: int) -> None:
        """
        Sets the color control attribute.
        
        Parameters
        -----------
        control : int
            the color control.
        """

    def unsetColorControl(self) -> None:
        """
        Unsets the color control attribute.
        """

    def hasLocalViewer(self) -> bool:
        """
        Determines whether the local viewer attribute is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getLocalViewer(self) -> bool:
        """
        Gets the local viewer attribute.
        Returns
        --------
        output : bool
            the local viewer.
        """

    def setLocalViewer(self, local: bool) -> None:
        """
        Sets the local viewer attribute.
        
        Parameters
        -----------
        local : bool
            the local viewer.
        """

    def unsetLocalViewer(self) -> None:
        """
        Unsets the local viewer attribute.
        """

    def hasTwoSide(self) -> bool:
        """
        Determines whether the two-sided lighting attribute is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getTwoSide(self) -> bool:
        """
        Gets the two-sided lighting attribute.
        Returns
        --------
        output : bool
            the two-sided lighting.
        """

    def setTwoSide(self, local: bool) -> None:
        """
        Sets the two-sided lighting attribute.
        
        Parameters
        -----------
        local : bool
            the two-sided lighting.
        """

    def unsetTwoSide(self) -> None:
        """
        Unsets the two-sided lighting attribute.
        """

    def apply(self) -> None:
        """
    
        """

    def getAttributeBits(self) -> int:
        """
    
        """
