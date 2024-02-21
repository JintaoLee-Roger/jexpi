from typing import overload
from edu.mines.jtk.mapping import *


class ParameterConvertException:
    """
    Exception thrown by Parameter when it cannot convert a
    parameter value to some specified type.
    """

    @overload
    def __init__(self) -> None:
        """
    
        """

    @overload
    def __init__(self, s: String) -> None:
        """
    
        """
