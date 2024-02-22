from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class SequenceView:
    """
    A view of a sequence of samples of a function f(x) of one variable x.
    This view renders each sample with a filled circle centered on the
    sample value and a vertical line drawn from that sample value to the
    origin. In other words, this view draws a sequence as lollipops with
    different heights that correspond to sample values.
    """

    @overload
    def __init__(self, f: Float1D) -> None:
        """
        Constructs a sequence view with specified values f(x).
        Uses default sampling of x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Float1D
            array of sampled function values f(x).
        """

    @overload
    def __init__(self, sx: Sampling, f: Float1D) -> None:
        """
        Constructs a sequence view with specified sampling and values f(x).
        
        Parameters
        -----------
        sx : Sampling
            the sampling of the variable x.
        f : Float1D
            array of sampled function values f(x).
        """

    @overload
    def set(self, f: Float1D) -> None:
        """
        Sets default sampling and specified function values f(x).
        The default sampling is x = 0, 1, 2, ....
        
        Parameters
        -----------
        f : Float1D
            array of sampled function values f(x).
        """

    @overload
    def set(self, sx: Sampling, f: Float1D) -> None:
        """
        Sets specified sampling and function values.
        
        Parameters
        -----------
        sx : Sampling
            the sampling of the variable x.
        f : Float1D
            array of sampled function values f(x).
        """

    def getSampling(self) -> Sampling:
        """
        Gets the sampling.
        Returns
        --------
        output : Sampling
            the sampling.
        """

    def getFunction(self) -> Float1D:
        """
        Gets a copy of the array of function values.
        Returns
        --------
        output : Float1D
            array of sampled function values f(x).
        """

    def setZero(self, zero: Zero) -> None:
        """
        Sets the visibility of function value zero in this view.
        The default visibility is ALWAYS.
        
        Parameters
        -----------
        zero : Zero
            the visibility of function value zero.
        """

    def setColor(self, color: Color) -> None:
        """
        Sets the color used to paint the sequence.
        The default color is the tile foreground color.
        That default is used if the specified color is null.
        
        Parameters
        -----------
        color : Color
            the color; null, for tile foreground color.
        """

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """
