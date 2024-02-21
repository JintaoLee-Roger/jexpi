from typing import overload
from edu.mines.jtk.mapping import *

from edu.mines.jtk.dsp import *


class Pfacc:
    """
    Prime-factor complex-to-complex FFT. The FFT length nfft must be composed
    of mutually prime factors from the set {2,3,4,5,7,8,9,11,13,16}. This
    restriction implies that n cannot exceed 720720 = 579111316.
    
    References:
    <ul><li>
    Temperton, C., 1985, Implementation of a self-sorting in-place prime
    factor fft algorithm:  Journal of Computational Physics, v. 58,
    p. 283-299.
    </li><li>
    Temperton, C., 1988, A new set of minimum-add rotated rotated dft
    modules: Journal of Computational Physics, v. 75, p. 190-198.
    </li></ul>
    """
