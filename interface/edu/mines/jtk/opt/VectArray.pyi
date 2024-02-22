from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class VectArray:
    """
    A VectContainer implemented as an array, with sequential indices.
    """

    def __init__(self, size: int) -> None:
        """
        Specify the number of sequential indices.
        """

    def put(self, index: int, vect: Vect) -> None:
        """
    
        """

    def get(self, index: int) -> Vect:
        """
    
        """

    def size(self) -> int:
        """
    
        """

    def containsKey(self, index: int) -> bool:
        """
    
        """

    def getKeys(self) -> Int1D:
        """
    
        """

    def dot(self, other: VectConst) -> double:
        """
    
        """

    def clone(self) -> VectArray:
        """
    
        """

    def dispose(self) -> None:
        """
    
        """

    def multiplyInverseCovariance(self) -> None:
        """
    
        """

    def constrain(self) -> None:
        """
    
        """

    def postCondition(self) -> None:
        """
    
        """

    def add(self, scaleThis: double, scaleOther: double,
            other: VectConst) -> None:
        """
    
        """

    def project(self, scaleThis: double, scaleOther: double,
                other: VectConst) -> None:
        """
    
        """

    def magnitude(self) -> double:
        """
    
        """
