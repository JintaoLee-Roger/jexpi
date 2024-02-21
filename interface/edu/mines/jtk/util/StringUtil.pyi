from typing import overload
from edu.mines.jtk.mapping import *


class StringUtil:
    """
    Utilities for manipulating strings of characters.
    """

    @staticmethod
    def removeTrailingZeros(self, s: String) -> String:
        """
        Removes any trailing zeros from a string representing a float or double.
        Also removes any insignificant trailing decimal point. For example,
        converts the string "1.00" to "1"; converts the string "1.2300e-6"
        to "1.23e-6".
        
        Parameters
        -----------
        s : String
            a string representing a float or double.
        
        Returns
        --------
        output : String
            the string with insignificant trailing zeros removed.
        """
