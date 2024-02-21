from typing import overload
from edu.mines.jtk.mapping import *


class CleanHandler:
    """
    An alternative to ConsoleHandler.  Uses CleanFormatter
    """

    def __init__(self) -> None:
        """
        Construct a new CleanHandler.
        """

    @staticmethod
    def addGlobalLogFile(self, fileName: String) -> None:
        """
        All CleanHandlers will also log to this file.
        """

    def publish(self, record: LogRecord) -> None:
        """
    
        """

    def close(self) -> None:
        """
    
        """

    def flush(self) -> None:
        """
    
        """

    @staticmethod
    def testLogger(self) -> None:
        """
        Call this from your code to test each type of log message
        """

    @staticmethod
    def main(self, args: String1D) -> None:
        """
        Test code
        
        Parameters
        -----------
        args : String1D
            command line
        """

    @staticmethod
    def setDefaultHandler(self) -> None:
        """
        If the user has not specified a java property for the global
        """

    @staticmethod
    def overrideExistingHandlers(self, level: Level) -> None:
        """
        Override any previously specified Handlers with the CleanHandler, and set Level.
        """
