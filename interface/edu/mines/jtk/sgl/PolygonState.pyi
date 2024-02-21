from typing import overload
from edu.mines.jtk.mapping import *


class PolygonState:
    """
    OpenGL polygon state.
    """

    def __init__(self) -> None:
        """
        Constructs polygon state.
        """

    def hasCullFace(self) -> bool:
        """
        Determines whether cull face mode is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getCullFace(self) -> int:
        """
        Gets the cull face mode.
        Returns
        --------
        output : int
            the cull face mode.
        """

    def setCullFace(self, mode: int) -> None:
        """
        Sets the cull face mode.
        
        Parameters
        -----------
        mode : int
            the cull face mode.
        """

    def unsetCullFace(self) -> None:
        """
        Unsets the cull face mode.
        """

    def hasFrontFace(self) -> bool:
        """
        Determines whether front face mode is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getFrontFace(self) -> int:
        """
        Gets the front face mode.
        Returns
        --------
        output : int
            the front face mode.
        """

    def setFrontFace(self, mode: int) -> None:
        """
        Sets the front face mode.
        
        Parameters
        -----------
        mode : int
            the front face mode.
        """

    def unsetFrontFace(self) -> None:
        """
        Unsets the front face mode.
        """

    def hasPolygonModeFront(self) -> bool:
        """
        Determines whether polygon mode for front faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def hasPolygonModeBack(self) -> bool:
        """
        Determines whether polygon mode for back faces is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getPolygonModeFront(self) -> int:
        """
        Gets the polygon mode for front faces.
        Returns
        --------
        output : int
            the polygon mode.
        """

    def getPolygonModeBack(self) -> int:
        """
        Gets the polygon mode for back faces.
        Returns
        --------
        output : int
            the polygon mode.
        """

    def setPolygonMode(self, mode: int) -> None:
        """
        Sets the polygon mode for front and back faces.
        
        Parameters
        -----------
        mode : int
            the polygon mode.
        """

    def setPolygonModeFront(self, mode: int) -> None:
        """
        Sets the polygon mode for front faces.
        
        Parameters
        -----------
        mode : int
            the polygon mode.
        """

    def setPolygonModeBack(self, mode: int) -> None:
        """
        Sets the polygon mode for back faces.
        
        Parameters
        -----------
        mode : int
            the polygon mode.
        """

    def unsetPolygonMode(self) -> None:
        """
        Unsets the polygon mode for front and back faces.
        """

    def unsetPolygonModeFront(self) -> None:
        """
        Unsets the polygon mode for front faces.
        """

    def unsetPolygonModeBack(self) -> None:
        """
        Unsets the polygon mode for back faces.
        """

    def hasPolygonOffset(self) -> bool:
        """
        Determines whether polygon offset is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getPolygonOffsetFactor(self) -> float:
        """
        Gets the polygon offset factor.
        Returns
        --------
        output : float
            the polygon offset factor.
        """

    def getPolygonOffsetUnits(self) -> float:
        """
        Gets the polygon offset units.
        Returns
        --------
        output : float
            the polygon offset units.
        """

    def setPolygonOffset(self, factor: float, units: float) -> None:
        """
        Sets the polygon offset.
        
        Parameters
        -----------
        factor : float
            the polygon offset factor.
        units : float
            the polygon offset units.
        """

    def unsetPolygonOffset(self) -> None:
        """
        Unsets the polygon offset.
        """

    def hasPolygonOffsetFill(self) -> bool:
        """
        Determines whether polygon offset fill is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getPolygonOffsetFill(self) -> bool:
        """
        Gets the polygon offset fill.
        Returns
        --------
        output : bool
            the polygon offset fill.
        """

    def setPolygonOffsetFill(self, fill: bool) -> None:
        """
        Sets the polygon offset fill.
        
        Parameters
        -----------
        fill : bool
            the polygon offset fill.
        """

    def unsetPolygonOffsetFill(self) -> None:
        """
        Unsets the polygon offset fill.
        """

    def hasPolygonOffsetLine(self) -> bool:
        """
        Determines whether polygon offset line is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getPolygonOffsetLine(self) -> bool:
        """
        Gets the polygon offset line.
        Returns
        --------
        output : bool
            the polygon offset line.
        """

    def setPolygonOffsetLine(self, line: bool) -> None:
        """
        Sets the polygon offset line.
        
        Parameters
        -----------
        line : bool
            the polygon offset line.
        """

    def unsetPolygonOffsetLine(self) -> None:
        """
        Unsets the polygon offset line.
        """

    def hasPolygonOffsetPoint(self) -> bool:
        """
        Determines whether polygon offset point is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getPolygonOffsetPoint(self) -> bool:
        """
        Gets the polygon offset point.
        Returns
        --------
        output : bool
            the polygon offset point.
        """

    def setPolygonOffsetPoint(self, point: bool) -> None:
        """
        Sets the polygon offset point.
        
        Parameters
        -----------
        point : bool
            the polygon offset point.
        """

    def hasPolygonStipple(self) -> bool:
        """
        Determines whether polygon stipple is set.
        Returns
        --------
        output : bool
            true, if set; false, otherwise.
        """

    def getPolygonStipple(self) -> Byte1D:
        """
        Gets the polygon stipple.
        Returns
        --------
        output : Byte1D
            the polygon stipple.
        """

    def setPolygonStipple(self, mask: Byte1D) -> None:
        """
        Sets the polygon stipple.
        
        Parameters
        -----------
        mask : Byte1D
            the polygon stipple.
        """

    def unsetPolygonStipple(self) -> None:
        """
        Unsets the polygon stipple.
        """

    def apply(self) -> None:
        """
    
        """

    def getAttributeBits(self) -> int:
        """
    
        """
