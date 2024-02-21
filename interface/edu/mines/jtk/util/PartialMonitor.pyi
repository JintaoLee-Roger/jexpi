from typing import overload
from edu.mines.jtk.mapping import *


class PartialMonitor:
    """
    Wrap an existing Monitor with a partial range.
    Note that only makes sense to call initReport()
    with the first wrapper used.
    """

    def __init__(self, wrapped: Monitor, begin: double, end: double) -> None:
        """
        An existing Monitor will be wrapped for progress in a limited range.
        corresponding to a 0 reported to this monitor.
        corresponding to a 1 reported to this monitor.
        
        Parameters
        -----------
        wrapped : Monitor
            The wrapped monitor.
        begin : double
            The first value to be updated to the wrapped monitor,
        end : double
            The last value to be updated to the wrapped monitor
        """

    def report(self, fraction: double) -> None:
        """
    
        """

    def isCanceled(self) -> bool:
        """
    
        """

    def initReport(self, initFraction: double) -> None:
        """
    
        """
