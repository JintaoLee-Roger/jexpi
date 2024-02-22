
from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class VectContainer(Vect):
    """
    Treat an indexed collection of Vects as a new Vect.
    Defined as an interface to allow both in-memory and cached
    implementations.
    """

    def put(self, index: int, vect: Vect) -> None:
        """
        Save a vect for the specified index.
        Integers need not be consecutive.  Use any valid integer.
        
        Parameters
        -----------
        index : int
            A unique integer for the requested vect.
        vect : Vect
            Vect for specified index.
        """
    def get(self, index: int) -> Vect:
        """
        Get a vect for the specified index.
        Integers need not be consecutive.
        
        Parameters
        -----------
        index : int
            A unique integer for the requested vect.
        
        Returns
        --------
        output : Vect
            Vect associated with this index, or null if none.
        """
    def size(self) -> int:
        """
        Returns the number of unique indices in this container.
        Returns
        --------
        output : int
            number of unique indices
        """
    def containsKey(self, index: int) -> bool:
        """
        Returns true if this container has a vect for the specified index.
        
        Parameters
        -----------
        index : int
            Check for a Vect with this index.
        
        Returns
        --------
        output : bool
            True if index has been assigned to a vect.
        """
    def getKeys(self) -> Int1D:
        """
        Return a set of all indices that have been assigned to a value.
        Return in the order of preferred access.
        Returns
        --------
        output : Int1D
            all indices that have been assigned Vect.
        """
    def clone(self) -> VectContainer:
        """
    
        """