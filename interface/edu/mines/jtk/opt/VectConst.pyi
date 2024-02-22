
from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class VectConst:
    """
    Vector operations that do not change the state of the vector
    """

    def dot(self, other: VectConst) -> double:
        """
        Return the Cartesian dot product of this vector with another
        vector (not including any inverse covariance).
        [Feel free to normalize by the number of elements in the array,
        if the inverse convariance is defined consistently.]
        
        Parameters
        -----------
        other : VectConst
            The vector to be dotted.
        
        Returns
        --------
        output : double
            The dot product.
        """
    def magnitude(self) -> double:
        """
        This is the dot product of the vector with
        itself premultiplied by the inverse covariance.
        If the inverse covariance is an identity, then
        the result is just the dot product with itself.
        Equivalently,
        <pre>
        Vect vect = (Vect) this.clone();
        vect.multiplyInverseCovariance();
        return this.dot(vect);
        </pre>
        But you can usually avoid the clone.
        Returns
        --------
        output : double
            magnitude of vector.
        """
    def clone(self) -> Vect:
        """
    
        """