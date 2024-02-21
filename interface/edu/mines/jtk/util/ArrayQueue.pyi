from typing import overload
from edu.mines.jtk.mapping import *


class ArrayQueue:
    """
    A first-in-first-out (FIFO) queue implemented with an array.
    
    This array-based implementation is optimized for performance. Entries
    can be added/removed to/from the queue in amortized constant time.
    The cost of adding/removing N entries to/from the queue is O(N), and
    the constant factor is less than that for an implementation based on
    {@link java.util.LinkedList}.
    
    For queues that contain at least a small number of entries, the length
    of the array used to implement the queue is less than twice the maximum
    number of entries in the queue. Furthermore, this length is always less
    than three times the number of entries in the queue.
    Therefore, this implementation requires less memory than one based on
    {@link java.util.LinkedList}.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a queue with default capacity.
        """

    @overload
    def __init__(self, capacity: int) -> None:
        """
        Constructs a queue with the specified initial capacity.
        The capacity is the number of entries that the queue can hold without
        increasing the length of the array used to implement the queue.
        
        This constructor may be used to reduce the cost of adding a large
        number of entries to the queue, when that number of entries is known
        in advance.
        
        Parameters
        -----------
        capacity : int
            the initial capacity.
        """

    def add(self, e: E) -> None:
        """
        Adds the specified entry to the back of the queue.
        Before addition, if the size of the queue equals its capacity,
        then the capacity of the queue is doubled.
        
        Parameters
        -----------
        e : E
            the entry.
        """

    def first(self) -> E:
        """
        Returns (but does not remove) the entry from the front of the queue.
        Returns
        --------
        output : E
            the entry.
        """

    def remove(self) -> E:
        """
        Removes and returns the entry from the front of the queue.
        After removal, if the size of the queue is less than one third
        its capacity, then the capacity is set to be twice that size.
        (Note that the capacity shrinks more slowly than it grows.)
        Returns
        --------
        output : E
            the entry.
        """

    def isEmpty(self) -> bool:
        """
        Determines whether the queue is empty.
        Returns
        --------
        output : bool
            true, if empty; false, otherwise.
        """

    def ensureCapacity(self, capacity: int) -> None:
        """
        Ensures that the capacity of the queue is not less than the
        specified value.
        The capacity is the number of entries that the queue can hold without
        increasing the length of the array used to implement the queue.
        
        This method may be used to reduce the cost of adding a large number
        of entries to the queue, when that number of entries is known in
        advance.
        
        Parameters
        -----------
        capacity : int
            the capacity.
        """

    def size(self) -> int:
        """
        Returns the number of entries in the queue.
        Returns
        --------
        output : int
            the number of entries.
        """

    def trimToSize(self) -> None:
        """
        Sets the capacity of the queue equal to its current size.
        This eliminates any wasted space in the array used to implement
        the queue.
        """
