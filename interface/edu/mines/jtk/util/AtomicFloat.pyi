from typing import overload
from edu.mines.jtk.mapping import *


class AtomicFloat:
    """
    A float value that may be updated atomically. An atomic float works like
    an atomic integer. (See {@link java.util.concurrent.atomic.AtomicInteger}.)
    For example, an atomic float might be used for parallel computation of the
    dot product of two vectors of floats.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an atomic float with initial value zero.
        """

    @overload
    def __init__(self, value: float) -> None:
        """
        Constructs an atomic float with specified initial value.
        
        Parameters
        -----------
        value : float
            the initial value.
        """

    def get(self) -> float:
        """
        Gets the current value of this float.
        Returns
        --------
        output : float
            the current value.
        """

    def set(self, value: float) -> None:
        """
        Sets the value of this float.
        
        Parameters
        -----------
        value : float
            the new value.
        """

    def getAndSet(self, value: float) -> float:
        """
        Atomically sets the value of this float and returns its old value.
        
        Parameters
        -----------
        value : float
            the new value.
        
        Returns
        --------
        output : float
            the old value.
        """

    def compareAndSet(self, expect: float, update: float) -> bool:
        """
        Atomically sets this float to the specified updated value
        if the current value equals the specified expected value.
        value was not equal to the expected value.
        
        Parameters
        -----------
        expect : float
            the expected value.
        update : float
            the updated value.
        
        Returns
        --------
        output : bool
            true, if successfully set; false, if the current
        """

    def weakCompareAndSet(self, expect: float, update: float) -> bool:
        """
        Atomically sets this float to the specified updated value
        if the current value equals the specified expected value.
        
        My fail spuriously, and does not provide ordering guarantees, so
        is only rarely useful.
        value was not equal to the expected value.
        
        Parameters
        -----------
        expect : float
            the expected value.
        update : float
            the updated value.
        
        Returns
        --------
        output : bool
            true, if successfully set; false, if the current
        """

    def getAndIncrement(self) -> float:
        """
        Atomically increments by one the value of this float.
        Returns
        --------
        output : float
            the previous value of this float.
        """

    def getAndDecrement(self) -> float:
        """
        Atomically decrements by one the value of this float.
        Returns
        --------
        output : float
            the previous value of this float.
        """

    def getAndAdd(self, delta: float) -> float:
        """
        Atomically adds a specified value to the value of this float.
        
        Parameters
        -----------
        delta : float
            the value to add.
        
        Returns
        --------
        output : float
            the previous value of this float.
        """

    def incrementAndGet(self) -> float:
        """
        Atomically increments by one the value of this float.
        Returns
        --------
        output : float
            the updated value of this float.
        """

    def decrementAndGet(self) -> float:
        """
        Atomically decrements by one the value of this float.
        Returns
        --------
        output : float
            the updated value of this float.
        """

    def addAndGet(self, delta: float) -> float:
        """
        Atomically adds a specified value to the value of this float.
        
        Parameters
        -----------
        delta : float
            the value to add.
        
        Returns
        --------
        output : float
            the updated value of this float.
        """

    def toString(self) -> String:
        """
    
        """

    def intValue(self) -> int:
        """
    
        """

    def longValue(self) -> long:
        """
    
        """

    def floatValue(self) -> float:
        """
    
        """

    def doubleValue(self) -> double:
        """
    
        """
