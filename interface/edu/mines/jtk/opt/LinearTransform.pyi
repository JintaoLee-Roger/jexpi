from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class LinearTransform:
    """
    Define methods applying a linear transform and its transpose
    """

    def forward(self, data: Vect, model: VectConst) -> None:
        """
        Apply the linear transform data = F model
        Zero the current data, and do not add.

        Parameters
        -----------
        data : Vect
            Output after linear transform
        model : VectConst
            Input for linear transform
        """

    def addTranspose(self, data: VectConst, model: Vect) -> None:
        """
        Apply the transpose of a linear transform model = F' data
        Add to existing data.

        Parameters
        -----------
        data : VectConst
            Input for transpose.
        model : Vect
            Output after linear transform.
        """

    def inverseHessian(self, model: Vect) -> None:
        """
        To speed convergence multiple a model by an approximate inverse
        Hessian.  An empty implementation is equivalent to an identity
        and is also okay.
        The Hessian is equivalent to multiplying once by the
        forward operation and then by the transpose.  Your approximate
        inverse can greatly speed convergence by trying to diagonalize
        this Hessian, or at least balancing the diagonal.

        Parameters
        -----------
        model : Vect
            The model to be multiplied.
        """

    def adjustRobustErrors(self, dataError: Vect) -> None:
        """
        Apply any robust trimming of outliers, or
        scale all errors for an approximate L1 norm when squared.
        This method should do nothing if you want a standard
        least-squares solution.
        Do not change the overall variance of the errors more than necessary.
     
        Parameters
        -----------
        dataError : Vect
            This is the original data minus the modeled data.
        """
