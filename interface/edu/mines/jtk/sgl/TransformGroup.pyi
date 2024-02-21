from typing import overload
from edu.mines.jtk.mapping import *


class TransformGroup:
    """
    A group node that transforms the coordinates for its children.
    """

    def __init__(self, transform: Matrix44) -> None:
        """
        Constructs a new transform group with specified transform.
        
        Parameters
        -----------
        transform : Matrix44
            the transform; copied, not referenced.
        """

    def getTransform(self) -> Matrix44:
        """
        Gets the transform for this group.
        Returns
        --------
        output : Matrix44
            the transform; by copy, not by reference.
        """

    def setTransform(self, transform: Matrix44) -> None:
        """
        Sets the transform for this group.
        
        Parameters
        -----------
        transform : Matrix44
            the transform; by copy, not by reference.
        """
