from typing import overload
from edu.mines.jtk.mapping import *


class XmlUtil:
    """
    Utilities for XML formatting.
    """

    @staticmethod
    def quoteAttributeValue(self, s: String) -> String:
        """
        Quotes an XML attribute value.
        Replaces special characters and XML entities.
        Encloses string in double or single quotes, depending on what's inside.
        
        Parameters
        -----------
        s : String
            attribute value to be quoted.
        
        Returns
        --------
        output : String
            quoted attribute value.
        """

    @staticmethod
    def quoteCharacterData(self, s: String) -> String:
        """
        Quotes character data.
        Replaces special characters and XML entities.
        Encloses string in double quotes if it contains whitespace.
        
        Parameters
        -----------
        s : String
            character data to be quoted.
        
        Returns
        --------
        output : String
            quoted character data.
        """
