from typing import overload
from edu.mines.jtk.mapping import *


class LinearTransformWrapper:
    """
    Wrap a LinearTransform as a non-linear Transform,
    """

    def __init__(self, linearTransform: LinearTransform) -> None:
        """
        Constructor.
        """

    def forwardNonlinear(self, data: Vect, model: VectConst) -> None:
        """
    
        """

    def forwardLinearized(self, data: Vect, model: VectConst,
                          modelReference: VectConst) -> None:
        """
    
        """

    def addTranspose(self, data: VectConst, model: Vect,
                     modelReference: VectConst) -> None:
        """
    
        """

    def inverseHessian(self, model: Vect, modelReference: VectConst) -> None:
        """
    
        """

    def adjustRobustErrors(self, dataError: Vect) -> None:
        """
    
        """
