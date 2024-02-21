from typing import overload
from edu.mines.jtk.mapping import *


class BrentZeroFinder:
    """
    Brent's algorithm for finding a zero of a function of one variable.
    Searches an interval [a,b] for an argument x for which a function
    f(x) = 0.
    
    This algorithm uses a combination of bisection and inverse linear and/or
    quadratic interpolation. Convergence is never much slower than that for
    bisection. If f(x) has a continuous second derivative near a simple zero,
    then the algorithm will tend towards superlinear convergence of order at
    least 1.618.
    
    Let xzero be the argument x that results from a search for the zero.
    That search is terminated when the difference between xzero and the
    true zeroing argument x is less than tol+4EPSabs(xzero), where
    tol is a specified tolerance and EPS is DBL_EPSILON (approximately
    1.0e-16), machine epsilon for IEEE double precision arithmetic.
    
    This implementation is adapted from the Fortran subroutine ZEROIN, by
    Forsythe, G.E., Malcolm, M.A., and Moler, C.B. 1977, Computer Methods
    for Mathematical Computations, Prentice Hall. That Fortran function is,
    in turn, a translation of the Algol 60 program by Brent, R., 1973,
    Algorithms for Minimization Without Derivatives, Prentice Hall.
    """

    def __init__(self, f: Function) -> None:
        """
        Constructs a zero finder for the specified function.
        
        Parameters
        -----------
        f : Function
            the function.
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

    @overload
    def findZero(self, a: double, b: double, tol: double) -> double:
        """
        Finds a zero within the specified search interval [a,b].
        The function values f(a) and f(b) must not have the same sign.
        
        Parameters
        -----------
        a : double
            the lower limit of the search interval.
        b : double
            the upper limit of the search interval.
        tol : double
            the accuracy with which to find the zero.
        
        Returns
        --------
        output : double
            the abscissa x for which f(x) is approximately zero.
        """

    @overload
    def findZero(self, a: double, fa: double, b: double, fb: double,
                 tol: double) -> double:
        """
        Finds a zero within the specified search interval [a,b], beginning
        with specified function values f(a) and f(b), which must not have
        the same sign.
        
        Parameters
        -----------
        a : double
            the lower limit of the search interval.
        fa : double
            the function f(x) evaluated at x = a.
        b : double
            the upper limit of the search interval.
        fb : double
            the function f(x) evaluated at x = b.
        tol : double
            the accuracy with which to find the zero.
        
        Returns
        --------
        output : double
            the abscissa x for which f(x) is approximately zero.
        """
