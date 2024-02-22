from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class MouseConstrained:
    """
    A constrained mouse. Classes that extend this abstract base class are
    used to convert mouse events, with mouse pixel coordinates, to points
    in a local coordinate system. The constraint is necessary, because
    mouse pixel coordinates are two-dimensional, whereas local coordinates
    are three-dimensional.
    """

    def __init__(self, localToPixel: Matrix44) -> None:
        """
        Constructs a constrained mouse.
        
        Parameters
        -----------
        localToPixel : Matrix44
            the transform from local to pixel coordinates.
        """

    def getPoint(self, event: MouseEvent) -> Point3:
        """
        Gets the point in local coordinates corresponding to the specified event.
        
        Parameters
        -----------
        event : MouseEvent
            the mouse event.
        
        Returns
        --------
        output : Point3
            the point, in local coordinates.
        """
