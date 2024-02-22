from typing import overload
from java.awt import *
from edu.mines.jtk.mapping import *


class ColorState:
    """
    OpenGL color state.
    """

    def __init__(self) -> None:
        """
        Constructs color state.
        """

    def hasColor(self) -> bool:
        """
        Determines whether current color is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getColor(self) -> Color:
        """
        Gets the current color.
        Returns
        --------
        output : Color
            the current color.
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the current color.
        
        Parameters
        -----------
        color : Color
            the current color.
        """

    def unsetColor(self) -> None:
        """
        Unsets the current color.
        """

    def hasShadeModel(self) -> bool:
        """
        Determines whether shade model is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getShadeModel(self) -> int:
        """
        Gets the shade model.
        Returns
        --------
        output : int
            the shade model.
        """

    def setShadeModel(self, shadeModel: int) -> None:
        """
        Sets the shade model.
        
        Parameters
        -----------
        shadeModel : int
            the shade model.
        """

    def unsetShadeModel(self) -> None:
        """
        Unsets the shade model.
        """

    def apply(self) -> None:
        """
    
        """

    def getAttributeBits(self) -> int:
        """
    
        """
