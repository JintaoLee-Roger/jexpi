from typing import overload
from edu.mines.jtk.mapping import *


class Stopwatch:
    """
    A timer that works like a stopwatch. A stopwatch can be started and
    stopped. A stopwatch is either running or not running. Stopwatch time
    can be read in either state, and that time can be reset to zero.
    
    Stopwatch time is elapsed (wall-clock) time, not process or CPU time.
    Stopwatch time resolution is one nanosecond. In other words, a
    stopwatch cannot measure a time difference less than one nanosecond.
    On the other hand, the granularity of the stopwatch depends on the
    underlying operating system and may be larger.
    """

    def start(self) -> None:
        """
        Starts this stopwatch. If the stopwatch is running, does nothing.
        """

    def stop(self) -> None:
        """
        Stops this stopwatch. If the stopwatch is not running, does nothing.
        """

    def reset(self) -> None:
        """
        Stops this stopwatch and resets the time to zero.
        """

    def restart(self) -> None:
        """
        Resets and starts this stopwatch.
        """

    def time(self) -> double:
        """
        Returns the stopwatch time, in seconds. Does not start or stop.
        Returns
        --------
        output : double
            the time, in seconds.
        """
