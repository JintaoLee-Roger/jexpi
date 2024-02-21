from typing import overload
from edu.mines.jtk.mapping import *


class LogMonitor:
    """
    Report progress to default Logger
    """

    def __init__(self, prefix: String, logger: Logger) -> None:
        """
        Progress will be reported to this Logger.
        then check arguments but do nothing.
        
        Parameters
        -----------
        prefix : String
            Prefix this string to every report.
        logger : Logger
            Send to this Logger.  If null,
        """

    def initReport(self, initFraction: double) -> None:
        """
    
        """

    def report(self, fraction: double) -> None:
        """
    
        """

    def isCanceled(self) -> bool:
        """
    
        """

    def cancel(self) -> None:
        """
        Interrupt any further work.  Causes isCancelled() to return true.
        """

    @staticmethod
    def getProgressReport(self, startTime: long, currentTime: long,
                          fraction: double, initFraction: double) -> String:
        """
        Get a user-viewable String describing the progress
        and completion time.
        when work started.
        
        Parameters
        -----------
        startTime : long
            Time in milliseconds when work began.
        currentTime : long
            Current time in milliseconds.
        fraction : double
            Current fraction of total progress, between 0 and 1.
        initFraction : double
            Initial fraction of total progress, between 0 and 1,
        
        Returns
        --------
        output : String
            Progress report as a string.
        """

    @staticmethod
    def main(self, argv: String1D) -> None:
        """
        run tests
        
        Parameters
        -----------
        argv : String1D
            command line
        """
