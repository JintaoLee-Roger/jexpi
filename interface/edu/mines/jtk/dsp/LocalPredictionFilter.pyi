from typing import overload
from edu.mines.jtk.mapping import *


class LocalPredictionFilter:
    """
    Local prediction filtering.
    
    <em>Warning: not yet completed or optimized for performance.</em>
    """

    def __init__(self, sigma: double) -> None:
        """
        Construct a prediction filter with specified Gaussian window half-width.
        
        Parameters
        -----------
        sigma : double
            the Gaussian window half-width; must not be less than 1.
        """

    def apply(self, lag1: Int1D, lag2: Int1D, f: Float2D,
              g: Float2D) -> Float3D:
        """
    
        """

    def applyPef(self, lag1: Int1D, lag2: Int1D, f: Float2D,
                 g: Float2D) -> None:
        """
    
        """
