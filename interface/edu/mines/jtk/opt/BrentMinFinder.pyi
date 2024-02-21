from typing import overload
from edu.mines.jtk.mapping import *


class BrentMinFinder:
    """
    Brent's algorithm for finding the minimum of a function of one variable.
    Searches an interval [a,b] for an argument x that minimizes a function
    f(x).
    
    Brent's algorithm uses a combination of golden section search and
    successive parabolic interpolation. Convergence is never much slower
    than that for a Fibonacci search. If the function f(x) has a continuous
    second derivative that is positive at the minimum (which is not at the
    endpoints a or b, then convergence is superlinear, and usually of the
    order of about 1.324.
    
    Let xmin be the argument x that results from a search for the minimum.
    That search is terminated when the difference between xmin and the
    true minimizing argument x is less than a specified tolerance. The
    function f(x) is never evaluated at two points closer together than
    EPSabs(xmin)+tol/3, where EPS is approximately 1.0e-8, the square
    root of machine epsilon for IEEE double precision arithmetic, and
    tol is a specified tolerance.
    
    If f(x) is a unimodal function and if the computed values of f(x) are
    always unimodal for arguments x separated by at least EPSabs(x)+tol/3,
    then xmin approximates the global minimum of f(x) on the interval [a,b]
    with an error less than 3EPSabs(xmin)+tol. If f(x) is not unimodal,
    then xmin may approximate a local, but perhaps not global, minimum to
    the same accuracy.
    
    This implementation is adapted from the Fortran function FMIN, by
    Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods
    for Mathematical Computations, Prentice Hall. That Fortran function is,
    in turn, a translation of the Algol 60 program by Brent, R., 1973,
    Algorithms for Minimization Without Derivatives, Prentice Hall.
    """

    def __init__(self, f: Function) -> None:
        """
        Constructs a min finder for the specified function.
        
        Parameters
        -----------
        f : Function
            the function to be minimized.
        """

    def f(self, x: double) -> double:
        """
        Returns the function value f(x) for the specified argument x.
        
        Parameters
        -----------
        x : double
            the argument at which to evaluate f(x).
        
        Returns
        --------
        output : double
            the function value f(x).
        """

    def findMin(self, a: double, b: double, tol: double) -> double:
        """
        Returns an x in the specified interval for which f(x) is a minimum.
        
        Parameters
        -----------
        a : double
            the smallest value of x in the interval.
        b : double
            the largest value of x in the interval.
        tol : double
            the search tolerance; see notes above.
        
        Returns
        --------
        output : double
            x for which f(x) is a minimum.
        """
