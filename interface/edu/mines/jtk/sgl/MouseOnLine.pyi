from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class MouseOnLine:
    """
    A mouse constrained by a line. Constrained points (in local coordinates)
    lie on a line through a specified origin point and parallel to a specified
    vector.
    
    Given a mouse event with pixel (x,y) coordinates, a mouse-on-line computes
    a constrained point. When the mouse pixel coordinates equal those used to
    construct the mouse-on-line, the constrained point equals the specified
    origin point.
    """

    def __init__(self, event: MouseEvent, origin: Point3, vector: Vector3,
                 localToPixel: Matrix44) -> None:
        """
        Constructs a mouse constrained by a line. The line of constraint
        contains the specified origin point and is parallel to the specified
        vector.
        
        Parameters
        -----------
        event : MouseEvent
            the mouse event.
        origin : Point3
            the origin point, in local coordinates.
        vector : Vector3
            the vector parallel to the line of constraint.
        localToPixel : Matrix44
            the transform from local to pixel coordinates.
        """

    def getPoint(self, event: MouseEvent) -> Point3:
        """
        Gets the point in local coordinates for the specified event.
        
        Parameters
        -----------
        event : MouseEvent
            the mouse event.
        
        Returns
        --------
        output : Point3
            the point, in local coordinates.
        """
