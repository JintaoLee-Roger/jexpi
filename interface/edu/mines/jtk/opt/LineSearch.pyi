from typing import overload
from edu.mines.jtk.mapping import *


class LineSearch:
    """
    Searches along a line for a minimum of a continuously differentiable
    function of one or more variables. Uses values f(s) of the function and
    its directional derivative f'(s) (the dot product of a search-direction
    vector and the function's gradient) to find a step s that minimizes the
    function along the line constraining the search. The search assumes that
    f'(0) &lt; 0, and searches for a positive s that minimizes f(s).
    This implementation uses Mor'e and Thuente's algorithm with guaranteed
    sufficient decrease. It iteratively searches for a step s that at each
    iteration satisfies both a sufficient-decrease condition and a curvature
    condition.
    The sufficient decrease condition (1) is
    <pre>
    f(s) &lt;= f(0) + ftolf'(0)s,
    </pre>
    and the curvature condition (2) is
    <pre>
    abs(f'(s)) &lt;= gtolabs(f'(0)),
    </pre>
    for specified non-negative tolerances ftol and gtol.
    Condition (1) ensures a sufficient decrease in the function f(s),
    provided that s is not too small. Condition (2) ensures that s is not
    too small, and usually guarantees that s is near a local minimizer of
    f. It is called a curvature condition because it implies that
    <pre>
    f'(s) - f'(0) &gt; (1-gtol)abs(f'(0)),
    </pre>
    so that the average curvature of f on the interval (0,s) is positive.
    The curvature condition (2) is especially important in a quasi-Newton
    method for function minimization, because it guarantees that a
    positive-definite quasi-Newton update is possible. If ftol is less than
    gtol and the function f(s) is bounded below, then there exists a step s
    that satisfies both conditions. If such a step cannot be found, then
    only the first sufficient-decrease condition (1) is satisfied.
    Mor'e and Thuente's algorithm initially choses an interval [sa,sb] that
    contains a minimizer of a modified function
    <pre>
    h(s) = f(s) - f(0) - ftolf'(0)s
    </pre>
    If h(s) &lt;= 0 and f'(s) &gt;= 0 for some step s, then the interval
    [a,b] is chosen so that it contains a minimizer of f.
    If no step can be found that satisfies both conditions, then the
    algorithm ends unconverged. In this case the step s satisifies only
    the sufficient-decrease condition.
    References:
    <ul><li>
    Mor'e, J.J., and Thuente, D.J., 1992, Line search algorithms with
    guaranteed sufficient decrease: Preprint MCS-P330-1092, Argonne
    National Laboratory.
    </li><li>
    Averick, B.M., and Mor'e, J.J., 1993, FORTRAN subroutines dcstep
    and dcsrch from MINPACK-2, 1993, Argonne National Laboratory and
    University of Minnesota.
    </li></ul>
    """

    def __init__(self, func: Function, stol: double, ftol: double,
                 gtol: double) -> None:
        """
        Constructs a line search with specified tolerances.
        The search ends if the search interval [slo,shi] is smaller than
        this tolerance times the upper bound shi.
        
        Parameters
        -----------
        func : Function
            Function to search.
        stol : double
            non-negative relative tolerance for an acceptable step.
        ftol : double
            non-negative tolerance for sufficient-decrease condition (1).
        gtol : double
            non-negative tolerance for curvature condition (2).
        """

    def search(self, s: double, f: double, g: double, smin: double,
               smax: double) -> Result:
        """
        Searches for a minimizing step.
        
        Parameters
        -----------
        s : double
            current estimate of a satisfactory step. Must be positive.
        f : double
            value f(0) of the function f at s = 0.
        g : double
            value f'(0) of the derivative of f at s = 0.
        smin : double
            Minimum value of s to be searched.
        smax : double
            Maximum value of s to be searched.
        
        Returns
        --------
        output : Result
            the result of the line search.
        """
