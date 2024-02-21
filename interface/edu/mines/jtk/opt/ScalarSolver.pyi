from typing import overload
from edu.mines.jtk.mapping import *


class ScalarSolver:
    """
    Search a single variable for a value that minimizes a function
    """

    def __init__(self, function: Function) -> None:
        """
        Constructor
        
        Parameters
        -----------
        function : Function
            Objective function to be minimized.
        """

    def solve(self, scalarMin: double, scalarMax: double, okError: double,
              okFraction: double, numberIterations: int,
              monitor: Monitor) -> double:
        """
        Minimize a function of scalar and return the optimum value.
        fraction of the range: dscalar/(scalarMax-scalarMin) &lt;= okError,
        where dscalar is the error bound on the returned value of scalar.
        this fraction of the minimum possible range for scalar:
        dscalar &lt;= okFraction(scalar-scalarMin),
        where dscalar is the error bound on the returned value of scalar.
        than 6.  The optimization performs at least 6 iterations --
        the minimum necessary for a genuinely parabolic function.
        I recommend at least 20.
        
        Parameters
        -----------
        scalarMin : double
            The minimum value allowed for the argument scalar.
        scalarMax : double
            The maximum value allowed for the argument scalar.
        okError : double
            The unknown error in scalar should be less than this
        okFraction : double
            The error in scalar should be less than
        numberIterations : int
            The maximum number of iterations if greater
        monitor : Monitor
            For reporting progress.  Ignored if null.
        
        Returns
        --------
        output : double
            The optimum value minimizing the function.
        """
