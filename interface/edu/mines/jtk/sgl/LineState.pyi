from typing import overload
from edu.mines.jtk.mapping import *


class LineState:
    """
    OpenGL line state.
    """

    def __init__(self) -> None:
        """
        Constructs line state.
        """

    def hasSmooth(self) -> bool:
        """
        Determines whether line smooth is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getSmooth(self) -> bool:
        """
        Gets the line smooth.
        Returns
        --------
        output : bool
            the line smooth.
        """

    def setSmooth(self, smooth: bool) -> None:
        """
        Sets the line smooth.
        
        Parameters
        -----------
        smooth : bool
            the smooth.
        """

    def unsetSmooth(self) -> None:
        """
        Unsets the line smooth.
        """

    def hasStipple(self) -> bool:
        """
        Determines whether line stipple is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getStippleFactor(self) -> int:
        """
        Gets the line stipple factor.
        Returns
        --------
        output : int
            the line stipple factor.
        """

    def getStipplePattern(self) -> short:
        """
        Gets the line stipple pattern.
        Returns
        --------
        output : short
            the line stipple pattern.
        """

    def setStipple(self, factor: int, pattern: short) -> None:
        """
        Sets the line stipple.
        
        Parameters
        -----------
        factor : int
            the stipple factor.
        pattern : short
            the stipple pattern.
        """

    def unsetStipple(self) -> None:
        """
        Unsets the line stipple.
        """

    def hasWidth(self) -> bool:
        """
        Determines whether line width is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getWidth(self) -> float:
        """
        Gets the line width.
        Returns
        --------
        output : float
            the line width.
        """

    def setWidth(self, width: float) -> None:
        """
        Sets the line width.
        
        Parameters
        -----------
        width : float
            the width.
        """

    def unsetWidth(self) -> None:
        """
        Unsets the line width.
        """

    def apply(self) -> None:
        """
    
        """

    def getAttributeBits(self) -> int:
        """
    
        """
