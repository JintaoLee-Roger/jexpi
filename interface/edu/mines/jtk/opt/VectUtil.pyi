from typing import overload
from edu.mines.jtk.mapping import *


class VectUtil:
    """
    Implements convenience methods for Vect.
    """

    @staticmethod
    def scale(self, v: Vect, scalar: double) -> None:
        """
        Scale a vector by a scalar constant.
        
        Parameters
        -----------
        v : Vect
            Vector to scale.
        scalar : double
            Factor to scale the vector.
        """

    @staticmethod
    def zero(self, v: Vect) -> None:
        """
        Set the magnitude of this vector to zero, so that this.dot(this) == 0.
        
        Parameters
        -----------
        v : Vect
            Vector to zero
        """

    @staticmethod
    def copy(self, to: Vect, froms: VectConst) -> None:
        """
        Copy the state of one vector onto another.
        with the state of from.
        
        Parameters
        -----------
        to : Vect
            Vector whose state should be initialized
        froms : VectConst
            Vector whose state should be copied.
        """

    @staticmethod
    def cloneZero(self, v: VectConst) -> Vect:
        """
        Clone a vector and initialized to zero, so that
        out.dot(out) == 0.
        
        Parameters
        -----------
        v : VectConst
            Vect to clone
        
        Returns
        --------
        output : Vect
            A cloned copy of the vector set to zero magnitude.
        """

    @staticmethod
    def areSame(self, v1: VectConst, v2: VectConst) -> bool:
        """
        See if two vectors are the same.  Useful for test code.
        floating precision.
        
        Parameters
        -----------
        v1 : VectConst
            First vector
        v2 : VectConst
            Second vector
        
        Returns
        --------
        output : bool
            true if vectors appear to be the same, within
        """

    @staticmethod
    def test(self, vect: VectConst) -> None:
        """
        Exercise all methods of Vect.
        Should be initialized to random non-zero values.
        A vector of zero magnitude will fail.
        
        Parameters
        -----------
        vect : VectConst
            An instance of a Vect to test.
        """

    @overload
    @staticmethod
    def getTransposePrecision(self, data: VectConst, model: VectConst,
                              transform: LinearTransform) -> int:
        """
        Return the number of significant digits in the dot product
        when calculated with and without the transpose.
        
        Parameters
        -----------
        data : VectConst
            Nonzero sample data
        model : VectConst
            A nonzero sample model.
        transform : LinearTransform
            The transform to test.
        
        Returns
        --------
        output : int
            number of digits in precision.
        """

    @overload
    @staticmethod
    def getTransposePrecision(self, data: VectConst, model: VectConst,
                              transform: Transform) -> int:
        """
        Return the number of significant digits in the dot product
        when calculated with and without the transpose.
        
        Parameters
        -----------
        data : VectConst
            Nonzero sample data
        model : VectConst
            A nonzero sample model.
        transform : Transform
            The transform to test.
        
        Returns
        --------
        output : int
            number of digits in precision.
        """
