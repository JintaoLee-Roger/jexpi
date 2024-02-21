from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class Tensors3:
    """
    An interface for 3D tensors used in anisotropic 3D image processing. 
    Each tensor is a symmetric positive-semidefinite 3-by-3 matrix:
    <pre><code>
        |a11 a12 a13|
    A = |a12 a22 a23|
        |a13 a23 a33|
    </code></pre>

    @author Dave Hale, Colorado School of Mines
    @version 2008.07.28
    """

    def getTensor(i1: int, i2: int, i3: int, a: Float1D) -> None:
        """
        Gets tensor elements for specified indices.

        Parameters
        -----------
        i1 : int 
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3nd dimension.
        a : Float1D
            array {a11,a12,a13,a22,a23,a33} of tensor elements.
        """
