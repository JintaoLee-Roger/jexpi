from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class Transform:
    """
    Implement a non-linear transform and its linearizations
    for a non-linear optimization.
    """

    def forwardNonlinear(self, data: Vect, model: VectConst) -> None:
        """
        Non-linear transform: data = f(model).
        
        Parameters
        -----------
        data : Vect
            Output.  Initial values are ignored.
        model : VectConst
            Input. Unchanged.
        """

    def forwardLinearized(self, data: Vect, model: VectConst,
                          modelReference: VectConst) -> None:
        """
        A linearized approximation of the forward transform
        for a small perturbation (model) to a reference model (modelReference).
        The output data must be a linear function of the model perturbation.
        Linearized transform:
        data = F model ~= f(model + modelReference) - f(modelReference)
        [Do not add results to the existing model.]
        
        Parameters
        -----------
        data : Vect
            Output.  Initial values are ignored.
        model : VectConst
            Perturbation to reference model.
        modelReference : VectConst
            The reference model for the linearized operator.
        """

    def addTranspose(self, data: VectConst, model: Vect,
                     modelReference: VectConst) -> None:
        """
        The transpose of the linearized approximation of the forward transform
        for a small perturbation (model) to a reference model (modelReference):
        model = F' data.  Add the result to the existing model.
        [This transpose assumes a simple dot product, without the
        inverse covariance.  I.e. data'F model = F' data model,
        for any arbitrary data or model.]
        
        Parameters
        -----------
        data : VectConst
            Input for transpose operation.
        model : Vect
            Output.  The transpose will be added to this vector.
        modelReference : VectConst
            The reference model for the linearized operator.
        """

    def inverseHessian(self, model: Vect, modelReference: VectConst) -> None:
        """
        To speed convergence multiple a model by an approximate inverse
        Hessian.  An empty implementation is equivalent to an identity
        and is also okay.
        The Hessian is equivalent to multiplying once by the linearized
        forward operation and then by the transpose.  Your approximate
        inverse can greatly speed convergence by trying to diagonalize
        this Hessian, or at least balancing the diagonal.
        If this operation depends only on the model, then you may
        prefer to implement Vect.postCondition() on the model.
        
        Parameters
        -----------
        model : Vect
            The model to be multiplied.
        modelReference : VectConst
            The reference model for the linearized operators.
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
