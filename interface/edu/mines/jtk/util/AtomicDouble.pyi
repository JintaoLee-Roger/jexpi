from typing import overload
from edu.mines.jtk.mapping import *


class AtomicDouble:
    """
    A double value that may be updated atomically. An atomic double works like
    an atomic integer. (See {@link java.util.concurrent.atomic.AtomicInteger}.)
    For example, an atomic double might be used for parallel computation of the
    dot product of two vectors of doubles.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an atomic double with initial value zero.
        """

    @overload
    def __init__(self, value: double) -> None:
        """
        Constructs an atomic double with specified initial value.
        
        Parameters
        -----------
        value : double
            the initial value.
        """

    def get(self) -> double:
        """
        Gets the current value of this double.
        Returns
        --------
        output : double
            the current value.
        """

    def set(self, value: double) -> None:
        """
        Sets the value of this double.
        
        Parameters
        -----------
        value : double
            the new value.
        """

    def getAndSet(self, value: double) -> double:
        """
        Atomically sets the value of this double and returns its old value.
        
        Parameters
        -----------
        value : double
            the new value.
        
        Returns
        --------
        output : double
            the old value.
        """

    def compareAndSet(self, expect: double, update: double) -> bool:
        """
        Atomically sets this double to the specified updated value
        if the current value equals the specified expected value.
        value was not equal to the expected value.
        
        Parameters
        -----------
        expect : double
            the expected value.
        update : double
            the updated value.
        
        Returns
        --------
        output : bool
            true, if successfully set; false, if the current
        """

    def weakCompareAndSet(self, expect: double, update: double) -> bool:
        """
        Atomically sets this double to the specified updated value
        if the current value equals the specified expected value.
        
        My fail spuriously, and does not provide ordering guarantees, so
        is only rarely useful.
        value was not equal to the expected value.
        
        Parameters
        -----------
        expect : double
            the expected value.
        update : double
            the updated value.
        
        Returns
        --------
        output : bool
            true, if successfully set; false, if the current
        """

    def getAndIncrement(self) -> double:
        """
        Atomically increments by one the value of this double.
        Returns
        --------
        output : double
            the previous value of this double.
        """

    def getAndDecrement(self) -> double:
        """
        Atomically decrements by one the value of this double.
        Returns
        --------
        output : double
            the previous value of this double.
        """

    def getAndAdd(self, delta: double) -> double:
        """
        Atomically adds a specified value to the value of this double.
        
        Parameters
        -----------
        delta : double
            the value to add.
        
        Returns
        --------
        output : double
            the previous value of this double.
        """

    def incrementAndGet(self) -> double:
        """
        Atomically increments by one the value of this double.
        Returns
        --------
        output : double
            the updated value of this double.
        """

    def decrementAndGet(self) -> double:
        """
        Atomically decrements by one the value of this double.
        Returns
        --------
        output : double
            the updated value of this double.
        """

    def addAndGet(self, delta: double) -> double:
        """
        Atomically adds a specified value to the value of this double.
        
        Parameters
        -----------
        delta : double
            the value to add.
        
        Returns
        --------
        output : double
            the updated value of this double.
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
