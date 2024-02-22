from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *
from edu.mines.jtk.opt import *


class Quadratic:
    """
    Define a second-order quadratic operation on a Vector
    0.5 x'Hx + b'x
    where H is a positive semidefinite quadratic and b is a
    linear gradient.
    """

    def multiplyHessian(self, x: Vect) -> None:
        """
        Multiply vector by the quadratic Hessian H.
        Perform the operation in-place.
        
        Parameters
        -----------
        x : Vect
            Vector to be multiplied and modified.
        """

    def inverseHessian(self, x: Vect) -> None:
        """
        Multiply vector by an approximate inverse of the Hessian.
        Perform the operation in-place.  This method is
        useful to speed convergence.
        An empty implementation is equivalent to an identity.
        
        Parameters
        -----------
        x : Vect
            Vector to be multiplied and modified.
        """

    def getB(self) -> Vect:
        """
        Get the linear gradient term b of the quadratic expression.
        The recipient receives a unique copy that must be disposed.
        Returns
        --------
        output : Vect
            The vector b where the quadratic is x'Hx + b'x
        """
