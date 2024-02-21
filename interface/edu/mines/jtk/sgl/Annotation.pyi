from typing import overload
from edu.mines.jtk.mapping import *


class Annotation:
    """
    An annotation. An annotation is fixed-scale text that anchors to a point
    in space and always faces the camera regardless of the scene's rotation.
    """

    @overload
    def __init__(self, p: Point3) -> None:
        """
        Constructs an empty annotation at a point in space.
        Note: The coordinate is in the world context.
        
        Parameters
        -----------
        p : Point3
            a point.
        """

    @overload
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Constructs an empty annotation at a point in space.
        Note: The coordinate is in the world context.
        
        Parameters
        -----------
        x : float
            a x-coordinate.
        y : float
            a y-coordinate.
        z : float
            a z-coordinate.
        """

    @overload
    def __init__(self, x: float, y: float, z: float, text: String) -> None:
        """
        Constructs an annotation at a point in space.
        Note: The coordinate is in the world context.
        
        Parameters
        -----------
        x : float
            a x-coordinate.
        y : float
            a y-coordinate.
        z : float
            a z-coordinate.
        text : String
            the text for this annotation.
        """

    @overload
    def __init__(self, p: Point3, text: String) -> None:
        """
        Constructs an annotation at a point in space.
        Note: The coordinate is in the world context.
        
        Parameters
        -----------
        p : Point3
            a point.
        text : String
            the text for this annotation.
        """

    def setFont(self, font: Font) -> None:
        """
        Sets the font of this annotation.
        
        Parameters
        -----------
        font : Font
            a font.
        """

    def getFont(self) -> Font:
        """
        Gets the font for this annotation.
        Returns
        --------
        output : Font
            the font.
        """

    def setAlignment(self, alignment: Alignment) -> None:
        """
        Sets the alignment for this annotation.
        The default alignment is to the East (right) of the anchor.
        
        Parameters
        -----------
        alignment : Alignment
            an alignment.
        """

    def getAlignment(self) -> Alignment:
        """
        Gets the alignment for this annotation.
        Returns
        --------
        output : Alignment
            the alignment.
        """

    def setText(self, text: String) -> None:
        """
        Sets the text for this annotation.
        
        Parameters
        -----------
        text : String
            some text.
        """

    def getText(self) -> String:
        """
        Gets the text for this annotation.
        Returns
        --------
        output : String
            the text.
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the color for this annotation.
        The default color is white.
        
        Parameters
        -----------
        color : Color
            a color.
        """

    def getColor(self) -> Color:
        """
        Gets this annotation's color.
        Returns
        --------
        output : Color
            the color.
        """

    def toString(self) -> String:
        """
    
        """

    def equals(self, o: Object) -> bool:
        """
    
        """

    def hashCode(self) -> int:
        """
    
        """
