from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class Tensors2:
    """
    An interface for 2D tensors used in anisotropic 2D image processing. 
    Each tensor is a symmetric positive-semidefinite 2-by-2 matrix:
    <pre><code>
    A = |a11 a12|
        |a12 a22|
    </code></pre>

    @author Dave Hale, Colorado School of Mines
    @version 2008.07.28
    """

    def getTensor(i1: int, i2: int, a: Float1D) -> None:
        """
        Gets tensor elements for specified indices.

        Parameters
        -----------
        i1 : int 
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        a : Float1D
            array {a11,a12,a22} of tensor elements.
        """
