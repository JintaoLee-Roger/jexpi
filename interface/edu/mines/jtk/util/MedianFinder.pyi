from typing import overload
from edu.mines.jtk.mapping import *


class MedianFinder:
    """
    Computes medians or weighted medians.
    
    The weighted median of n values x[i] is the value x that minimizes
    the following function:
    <pre>
    n-1
    f(x) = sum w[i]abs(x-x[i])
    i=0
    </pre>
    Here, the x[.] are values for which the median is to be computed,
    the w[.] are positive weights, and x is the desired weighted median.
    The function f(x) is convex and piecewise linear, so at least one
    (but no more than two) of the specified values x[i] minimizes the
    function f(x).
    
    To find a minimum, we define sums of weights w[.] for which x[.]
    is less than, equal to, and greater than x:
    <pre>
    wl(x) = sum of w[i] for x[i] &lt; x
    wm(x) = sum of w[i] for x[i] = x
    wr(x) = sum of w[i] for x[i] &gt; x
    </pre>
    and then define the left and right derivatives of f(x):
    <pre>
    dl(x) = wl(x)-wm(x)-wr(x) &lt;= 0
    dr(x) = wl(x)+wm(x)-wr(x) &gt;= 0
    </pre>
    These inequality conditions are necessary and sufficient for x
    to minimize f(x), that is, for x to be the weighted median.
    
    When either dl(x) = 0 or dr(x) = 0, then the function f(x) has
    zero slope between two values x[i] that both minimize f(x), and
    the weighted median is then computed to be the average of those
    two minimizing values. For example, such an average is always
    computed when the number of values x[.] is even and all weights
    w[.] are equal.
    
    Computational complexity for both the median and the weighted
    median is O(n), where n is the number of values x[.] (and weights
    w[.]). In benchmark tests for large n, the cost of a median is
    about 16 times more costly than a simple mean, and the cost of a
    weighted median is about 1.5 times more costly than an unweighted
    median.
    """

    def __init__(self, n: int) -> None:
        """
        Constructs a median finder.
        
        Parameters
        -----------
        n : int
            number of values for which to compute medians.
        """

    @overload
    def findMedian(self, x: Float1D) -> float:
        """
        Returns the median of the specified array of values.
        
        Parameters
        -----------
        x : Float1D
            array of values.
        
        Returns
        --------
        output : float
            the median.
        """

    @overload
    def findMedian(self, w: Float1D, x: Float1D) -> float:
        """
        Returns the weighted median of the specified array of values.
        
        Parameters
        -----------
        w : Float1D
            array of positive weights.
        x : Float1D
            array of values.
        
        Returns
        --------
        output : float
            the weighted median.
        """
