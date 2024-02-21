from typing import overload
from edu.mines.jtk.mapping import *


class StringParser:
    """
    Parse a string containing zero or more string literals.
    """

    def __init__(self, s: String) -> None:
        """
        Construct a string parser for the specified string.
        
        Parameters
        -----------
        s : String
            string to parse.
        """

    def hasMoreStrings(self) -> bool:
        """
        Determine whether the parser has more strings.
        Returns
        --------
        output : bool
            true, if more strings; false, otherwise.
        """

    def nextString(self) -> String:
        """
        Get the next string.
        Returns
        --------
        output : String
            next string.
        """
