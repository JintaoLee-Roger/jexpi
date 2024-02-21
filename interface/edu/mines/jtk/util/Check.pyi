from typing import overload
from edu.mines.jtk.mapping import *


class Check:
    """
    Facilitates checks for common conditions. Methods in this class throw
    appropriate exceptions when specified conditions are not satisfied.
    """

    @staticmethod
    def argument(self, condition: bool, message: String) -> None:
        """
        Ensures that the specified condition for an argument is true.
        
        Parameters
        -----------
        condition : bool
            the condition.
        message : String
            a description of the condition.
        """

    @staticmethod
    def state(self, condition: bool, message: String) -> None:
        """
        Ensures that the specified condition of state is true.
        
        Parameters
        -----------
        condition : bool
            the condition.
        message : String
            a description of the condition.
        """

    @overload
    @staticmethod
    def index(self, n: int, i: int) -> None:
        """
        Ensures that the specified zero-based index is in bounds.
        
        Parameters
        -----------
        n : int
            the smallest positive number that is not in bounds.
        i : int
            the index.
        """

    @overload
    @staticmethod
    def index(self, a: Byte1D, i: int) -> None:
        """
        Ensures that the specified array index is in bounds.
        
        Parameters
        -----------
        a : Byte1D
            the array.
        i : int
            the index.
        """

    @overload
    @staticmethod
    def index(self, a: Short1D, i: int) -> None:
        """
        Ensures that the specified array index is in bounds.
        
        Parameters
        -----------
        a : Short1D
            the array.
        i : int
            the index.
        """

    @overload
    @staticmethod
    def index(self, a: Int1D, i: int) -> None:
        """
        Ensures that the specified array index is in bounds.
        
        Parameters
        -----------
        a : Int1D
            the array.
        i : int
            the index.
        """

    @overload
    @staticmethod
    def index(self, a: Long1D, i: int) -> None:
        """
        Ensures that the specified array index is in bounds.
        
        Parameters
        -----------
        a : Long1D
            the array.
        i : int
            the index.
        """

    @overload
    @staticmethod
    def index(self, a: Float1D, i: int) -> None:
        """
        Ensures that the specified array index is in bounds.
        
        Parameters
        -----------
        a : Float1D
            the array.
        i : int
            the index.
        """

    @overload
    @staticmethod
    def index(self, a: Double1D, i: int) -> None:
        """
        Ensures that the specified array index is in bounds.
        
        Parameters
        -----------
        a : Double1D
            the array.
        i : int
            the index.
        """
