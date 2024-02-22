from typing import overload
from java.awt import *
from edu.mines.jtk.mapping import *


class BlendState:
    """
    OpenGL blend state.
    """

    def __init__(self) -> None:
        """
        Constructs blend state.
        """

    def hasColor(self) -> bool:
        """
        Determines whether blend color is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getColor(self) -> Color:
        """
        Gets the blend color.
        Returns
        --------
        output : Color
            the blend color.
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the blend color.
        
        Parameters
        -----------
        color : Color
            the blend color.
        """

    def unsetColor(self) -> None:
        """
        Unsets the blend color.
        """

    def hasEquation(self) -> bool:
        """
        Determines whether blend equation is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getEquation(self) -> int:
        """
        Gets the blend equation.
        Returns
        --------
        output : int
            the blend equation.
        """

    def setEquation(self, mode: int) -> None:
        """
        Sets the blend equation.
        
        Parameters
        -----------
        mode : int
            the blend equation.
        """

    def unsetEquation(self) -> None:
        """
        Unsets the blend equation.
        """

    def hasBlendFunction(self) -> bool:
        """
        Determines whether blend function is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getSfactor(self) -> int:
        """
        Gets the blend function sfactor.
        Returns
        --------
        output : int
            the blend function sfactor.
        """

    def getDfactor(self) -> int:
        """
        Gets the blend function dfactor.
        Returns
        --------
        output : int
            the blend function dfactor.
        """

    def setFunction(self, sfactor: int, dfactor: int) -> None:
        """
        Sets the blend function.
        
        Parameters
        -----------
        sfactor : int
            the source factor.
        dfactor : int
            the destination factor.
        """

    def unsetFunction(self) -> None:
        """
        Unsets the blend function.
        """

    def apply(self) -> None:
        """
    
        """

    def getAttributeBits(self) -> int:
        """
    
        """
