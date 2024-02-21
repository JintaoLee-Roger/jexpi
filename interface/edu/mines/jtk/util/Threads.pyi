
from typing import overload
from edu.mines.jtk.mapping import *


class Threads:
    """
    Utilities for working with multiple threads.
    """

    @staticmethod
    def getAvailableProcessors(self) -> int:
        """
        Gets the number of available processors (cores).
        Returns
        --------
        output : int
            the number of available processors (cores).
        """
    @overload
    @staticmethod
    def makeArray(self) -> Thread[]:
        """
        Returns a new array for threads. The length of the array equals the
        number of available processors (or cores).
        
        Note that this method does not actually construct any threads.
        Returns
        --------
        output : Thread[]
            the array.
        """
    @overload
    @staticmethod
    def makeArray(self, multiple: double) -> Thread[]:
        """
        Returns a new array for threads. The length of the array is greater
        than zero and is proportional to the number of available processors
        (or cores).
        
        Note that this method does not actually construct any threads.
        
        Parameters
        -----------
        multiple : double
            desired number of threads per processor (or core).
        
        Returns
        --------
        output : Thread[]
            the array, with length for at least one thread.
        """
    @staticmethod
    def startAndJoin(self, threads: Thread[]) -> None:
        """
        Starts and joins all threads in the specified array.
        
        Parameters
        -----------
        threads : Thread[]
            array of threads.
        """