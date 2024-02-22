from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class TransformQuadratic:
    """
    For a linearized transform, implement the Gauss-Newton
    """

    def __init__(self, data: VectConst, referenceModel: VectConst,
                 perturbModel: VectConst, transform: Transform,
                 dampOnlyPerturbation: bool) -> None:
        """
        Wrap known data, reference mode, and transform
        """

    def getTransposePrecision(self) -> int:
        """
        Run a few tests to ensure that transpose satisfies definition.
        """

    def multiplyHessian(self, x: Vect) -> None:
        """
        Multiply by Hessian <code> H = F'NF + M </code>
        """

    def inverseHessian(self, x: Vect) -> None:
        """
    
        """

    def getB(self) -> Vect:
        """
        Return gradient term of quadratic.
        """

    def evalFullObjectiveFunction(self, m: VectConst) -> double:
        """
        Evaluate the full objective function without approximation.
        """

    def dispose(self) -> None:
        """
        Free up internal cached vectors
        """
