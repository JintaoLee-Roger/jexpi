from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *


class TimeHeap3:
    """
    A min- or max-heap of times sampled in a 3D array.
    Such a heap is typically used in fast marching methods. It enhances
    a conventional heap by maintaining a map of heap entries in a 3D array
    of indices. Given array indices (i1,i2,i3), this index map enables O(1)
    access to heap entries. Such fast access is required as times in the
    heap are reduced while marching.
    
    Depending on the type of heap, min or max, the entry with either the
    smallest or largest time is stored at the top (root) of the heap. This
    entry can be accessed with complexity O(1) and removed with complexity
    O(log N), where N is the number of entries in the heap. Complexity for
    inserting new entries or reducing the times for existing entries is
    O(log N).
    """

    def __init__(self, type: Type, n1: int, n2: int, n3: int) -> None:
        """
        Constructs a heap with specified type and array dimensions.
        
        Parameters
        -----------
        type : Type
            the type of heap.
        n1 : int
            number of samples in 1st dimension.
        n2 : int
            number of samples in 2nd dimension.
        n3 : int
            number of samples in 3rd dimension.
        """

    def getType(self) -> Type:
        """
        Gets the type of this heap.
        Returns
        --------
        output : Type
            the type.
        """

    def getN1(self) -> int:
        """
        Gets the number of samples in the 1st dimension.
        Returns
        --------
        output : int
            the number of samples.
        """

    def getN2(self) -> int:
        """
        Gets the number of samples in the 2nd dimension.
        Returns
        --------
        output : int
            the number of samples.
        """

    def getN3(self) -> int:
        """
        Gets the number of samples in the 3rd dimension.
        Returns
        --------
        output : int
            the number of samples.
        """

    @overload
    def insert(self, i1: int, i2: int, i3: int, time: float) -> None:
        """
        Inserts a new entry into this heap with specified time and indices.
        The heap must not already contain an entry with those indices.
        
        Parameters
        -----------
        i1 : int
            the sample index in 1st dimension.
        i2 : int
            the sample index in 2nd dimension.
        i3 : int
            the sample index in 2nd dimension.
        time : float
            the time.
        """

    @overload
    def insert(self, i1: int, i2: int, i3: int, time: float,
               mark: int) -> None:
        """
        Inserts a new entry into this heap with specified time and indices.
        The heap must not already contain an entry with those indices.
        
        Parameters
        -----------
        i1 : int
            the sample index in 1st dimension.
        i2 : int
            the sample index in 2nd dimension.
        i3 : int
            the sample index in 2nd dimension.
        time : float
            the time.
        mark : int
            a mark to associate with the new entry.
        """

    def reduce(self, i1: int, i2: int, i3: int, time: float) -> None:
        """
        Reduces the time of the entry in this heap with specified indices.
        This heap must already contain an entry with those indices, and
        the specified time must be less than the time for that entry.
        
        Parameters
        -----------
        i1 : int
            the sample index in 1st dimension.
        i2 : int
            the sample index in 2nd dimension.
        i3 : int
            the sample index in 2nd dimension.
        time : float
            the reduced time.
        """

    def remove(self) -> Entry:
        """
        Removes and returns the heap entry with smallest/largest time.
        The heap must not be empty.
        """

    def contains(self, i1: int, i2: int, i3: int) -> bool:
        """
        Determines whether this help contains an entry with the specified indices.
        
        Parameters
        -----------
        i1 : int
            the sample index in 1st dimension.
        i2 : int
            the sample index in 2nd dimension.
        i3 : int
            the sample index in 3rd dimension.
        
        Returns
        --------
        output : bool
            true, if in the heap; false, otherwise.
        """

    def clear(self) -> None:
        """
        Removes all entries from this heap.
        """

    def size(self) -> int:
        """
        Returns the number of entries in this heap.
        """

    def isEmpty(self) -> bool:
        """
        Returns true if this heap is empty; false, otherwise.
        """

    def dump(self) -> None:
        """
        Dumps this heap to standard output; leading spaces show level in tree.
        """

    @staticmethod
    def main(self, args: String1D) -> None:
        """
    
        """
