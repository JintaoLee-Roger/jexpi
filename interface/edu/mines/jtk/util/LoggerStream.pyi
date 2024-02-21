from typing import overload
from edu.mines.jtk.mapping import *


class LoggerStream:
    """
    Wrap a Logger as a PrintStream.
    """

    def __init__(self, logger: Logger, level: Level) -> None:
        """
        Wrap a Logger as a PrintStream .
        """

    def flush(self) -> None:
        """
    
        """

    @overload
    def println(self) -> None:
        """
    
        """

    @overload
    def println(self, x: Object) -> None:
        """
    
        """

    @overload
    def println(self, x: String) -> None:
        """
    
        """

    def close(self) -> None:
        """
    
        """

    def checkError(self) -> bool:
        """
    
        """

    @staticmethod
    def main(self, args: String1D) -> None:
        """
        test code
        """
