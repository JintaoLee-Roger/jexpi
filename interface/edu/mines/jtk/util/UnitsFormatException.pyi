from typing import overload
from edu.mines.jtk.mapping import *


class UnitsFormatException:
    """
    Exception thrown by Units for a malformed units definition.
    """

    @overload
    def __init__(self) -> None:
        """
    
        """

    @overload
    def __init__(self, s: String) -> None:
        """
    
        """
