from typing import overload
from edu.mines.jtk.mapping import *


class ParameterSetFormatException:
    """
    Exception thrown when the format of a parameter set is not valid.
    """

    @overload
    def __init__(self) -> None:
        """
    
        """

    @overload
    def __init__(self, s: String) -> None:
        """
    
        """
