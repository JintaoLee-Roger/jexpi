from typing import overload
from edu.mines.jtk.mapping import *


class RandomFloat:
    """
    Pseudo-random float generator. Compared with the standard Java class
    Random, this class generates generates random floats more quickly and
    perhaps more randomly (certainly with greater periodicity).
    The uniform generator was
    adapted from subroutine uni in "Numerical Methods and Software",
    D. Kahaner, C. Moler, S. Nash, Prentice Hall, 1988.  This book references,
    Marsaglia G., "Comments on the perfect uniform random number generator",
    Unpublished notes, Wash S. U.  According to the reference, this random
    number generator "passes all known tests and has a period that is ...
    approximately 10^19".
    The normal (Gaussian) generator was
    adapted from subroutine rnor in "Numerical Methods and Software", D.
    Kahaner, C. Moler, S. Nash, Prentice Hall, 1988.  Subroutine rnor,
    in turn, is adapted from a paper by Marsaglia G. and Tsang, W. W., 1984,
    A fast, easily implemented method for sampling from decreasing or symmetric
    unimodal density functions:  SIAM J. Sci. Stat. Comput., v. 5, no. 2,
    p. 349-359.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a random float generator with default seed.
        """

    @overload
    def __init__(self, seed: int) -> None:
        """
        Constructs a random float generator.
        
        Parameters
        -----------
        seed : int
            the seed with which to initialize the generator.
        """

    def uniform(self) -> float:
        """
        Gets a pseudo-random float from a uniform [0,1) distribution.
        The float is between 0.0f (inclusive) and 1.0f (exclusive).
        Returns
        --------
        output : float
            the pseudo-random float.
        """

    def normal(self) -> float:
        """
        Gets a pseudo-random float from a normal (Gaussian) distribution.
        The N(0,1) distribution has zero mean and unit variance.
        Returns
        --------
        output : float
            the pseudo-random float.
        """

    def setSeed(self, seed: int) -> None:
        """
        Seeds the random number generator.
        Different seeds yield different sequences of random numbers.
        
        Parameters
        -----------
        seed : int
            the seed.
        """
