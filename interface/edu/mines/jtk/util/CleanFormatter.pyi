from typing import overload
from edu.mines.jtk.mapping import *


class CleanFormatter:
    """
    Format log messages without any extras.
    """

    @staticmethod
    def setWarningPrefix(self, prefix: String) -> None:
        """
        Prefix a string to all warnings or severe errors
        """

    def format(self, record: LogRecord) -> String:
        """
    
        """

    @staticmethod
    def prependToLines(self, prepend: String, lines: String) -> String:
        """
        Prepend a string to every line of text in a String
        """
