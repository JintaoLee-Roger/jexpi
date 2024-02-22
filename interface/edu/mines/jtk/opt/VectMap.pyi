from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class VectMap:
    """
    A VectContainer implemented as an unsynchronized Map.
    Keys will be returned in the order of insertion.
    """

    def __init__(self, cloneContents: bool) -> None:
        """
        Specify whether contents are copied or not.
        methods will clone the passed Vect.
        
        Parameters
        -----------
        cloneContents : bool
            If true, all put and get
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

    def clone(self) -> VectMap:
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
