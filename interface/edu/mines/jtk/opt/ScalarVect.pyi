from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class ScalarVect:
    """
    Implements a Vect by wrapping a single double
    """

    @overload
    def __init__(self, value: double, variance: double) -> None:
        """
        Specify the initial value
        will divide the scalar by this number.
        Pass a value of 1 if you do not care.
        
        Parameters
        -----------
        value : double
            The initial value of the wrapped scalar
        variance : double
            The method multiplyInverseCovariance()
        """

    @overload
    def __init__(self) -> None:
        """
        To be used with init()
        """

    def init(self, value: double, variance: double) -> None:
        """
        Initialize the Vect.
        will divide the scalar by this number.
        Pass a value of 1 if you do not care.
        
        Parameters
        -----------
        value : double
            The initial value of the wrapped scalar .
        variance : double
            The method multiplyInverseCovariance()
        """

    def get(self) -> double:
        """
        Get the value of the scalar.
        Returns
        --------
        output : double
            The wrapped scalar.
        """

    def set(self, value: double) -> None:
        """
        Set the value of the scalar.
        
        Parameters
        -----------
        value : double
            The new value of the wrapped scalar.
        """

    def clone(self) -> ScalarVect:
        """
    
        """

    def dot(self, other: VectConst) -> double:
        """
    
        """

    def toString(self) -> String:
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
