from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *


class TensorsView:
    """
    A view of a 2D metric tensor field. A metric tensor corresponds to a
    symmetric positive-definite 2x2 matrix, and is displayed as an ellipse.
    Ellipses are drawn for only a uniformly sampled subset of the tensors.
    """

    @overload
    def __init__(self, et: EigenTensors2) -> None:
        """
        Constructs a view of the specified tensors.
        
        Parameters
        -----------
        et : EigenTensors2
            the tensors.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, et: EigenTensors2) -> None:
        """
        Constructs a view of the specified tensors.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension.
        s2 : Sampling
            sampling of 2nd dimension.
        et : EigenTensors2
            the tensors.
        """

    def set(self, et: EigenTensors2) -> None:
        """
        Sets the tensors for this view.
        
        Parameters
        -----------
        et : EigenTensors2
            the tensors.
        """

    def setOrientation(self, orientation: Orientation) -> None:
        """
        Sets the orientation of (x1,x2) axes.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation.
        """

    def getOrientation(self) -> Orientation:
        """
        Gets the orientation of (x1,x2) axes.
        Returns
        --------
        output : Orientation
            the orientation.
        """

    @overload
    def setEllipsesDisplayed(self, ne: int) -> None:
        """
        Sets the number of ellipses displayed along the larger dimension.
        Ellipses are displayed for only a subset of the sampled tensors.
        The specified number of ellipses roughly equals the number that
        will be displayed along the axis with the largest number of tensors.
        
        The sizes of the ellipses are chosen so that they never overlap.
        Therefore, this parameter indirectly determines the size of the
        the ellipses drawn. One can display either a large number of small
        ellipses or a smaller number of larger ellipses.
        
        The default number is 20.
        
        Calling this method overrides any ellipse samplings specified
        previously by calling the method
        {@link #setEllipsesDisplayed(Sampling,Sampling)}.
        
        Parameters
        -----------
        ne : int
            the number of ellipses displayed along the larger dimension.
        """

    @overload
    def setEllipsesDisplayed(self, e1: Sampling, e2: Sampling) -> None:
        """
        Sets the samplings of ellipses displayed. The specified ellipse
        samplings are typically a subset of the samplings of the tensors
        for this view.
        
        Calling this method with non-null samplings overrides any number
        of ellipses specified previously by calling the method
        {@link #setEllipsesDisplayed(int)}.
        
        Parameters
        -----------
        e1 : Sampling
            ellipse sampling in 1st dimension.
        e2 : Sampling
            ellipse sampling in 2nd dimension.
        """

    def setScale(self, scale: double) -> None:
        """
        Sets the scale factor for ellipse size.
        
        Parameters
        -----------
        scale : double
            the scale factor.
        """

    def setLineWidth(self, width: float) -> None:
        """
        Sets the line width.
        The default width is zero, for the thinnest lines.
        
        Parameters
        -----------
        width : float
            the line width.
        """

    def setLineColor(self, color: Color) -> None:
        """
        Sets the line color.
        The default line color is the tile foreground color.
        That default is used if the specified line color is null.
        
        Parameters
        -----------
        color : Color
            the line color; null, for tile foreground color.
        """

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """
