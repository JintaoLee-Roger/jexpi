from typing import overload
from edu.mines.jtk.mapping import *


class Monitor:
    """
    Implement this interface to receive notifications of progress
    """

    def initReport(self, initFraction: double) -> None:
        """
        Initialize the fraction of the work that was
        completed when the process started.
        If not called, then assumed to be 0.

        Parameters
        -----------
        initFraction :  double
            Fraction of work done when process started, from 0 to 1.
        """

    def report(self, fraction: double) -> None:
        """
        This method will be called with the current fraction
        of work done.  Values range from 0 at the beginning
        to 1 when all work is done.

        Parameters
        -----------
        fraction :  double
            Fraction of work done so far, from 0 to 1. This value must equal 
            or exceed all values previously passed to this method or to initReport.
        """

    def isCanceled(self) -> bool:
        """
        If true, then any further progress should be cancelled.

        Returns
        -----------
        output :  bool
            true, when any requested work should be interrupted.
            False, if progress is expected to run to completion.
        """
