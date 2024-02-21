from typing import overload
from edu.mines.jtk.mapping import *


class PointState:
    """
    OpenGL point state.
    """

    def __init__(self) -> None:
        """
        Constructs point state.
        """

    def hasSmooth(self) -> bool:
        """
        Determines whether point smooth is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getSmooth(self) -> bool:
        """
        Gets the point smooth.
        Returns
        --------
        output : bool
            the point smooth.
        """

    def setSmooth(self, smooth: bool) -> None:
        """
        Sets the point smooth.
        
        Parameters
        -----------
        smooth : bool
            the smooth.
        """

    def unsetSmooth(self) -> None:
        """
        Unsets the point smooth.
        """

    def hasSize(self) -> bool:
        """
        Determines whether point size is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getSize(self) -> float:
        """
        Gets the point size.
        Returns
        --------
        output : float
            the point size.
        """

    def setSize(self, size: float) -> None:
        """
        Sets the point size.
        
        Parameters
        -----------
        size : float
            the size.
        """

    def unsetSize(self) -> None:
        """
        Unsets the point size.
        """

    def apply(self) -> None:
        """
    
        """

    def getAttributeBits(self) -> int:
        """
    
        """
