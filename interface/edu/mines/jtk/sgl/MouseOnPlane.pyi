from typing import overload
from edu.mines.jtk.mapping import *


class MouseOnPlane:
    """
    A mouse constrained by a plane. Constrained points (in local coordinates)
    lie on a constraint plane that contains a specified origin point and is
    parallel to a specified plane.
    
    Given a mouse event with pixel (x,y) coordinates, a mouse-on-plane computes
    a constrained point. When the mouse pixel coordinates equal those used to
    construct the mouse-on-plane, the constrained point equals the specified
    origin point.
    """

    def __init__(self, event: MouseEvent, origin: Point3, plane: Plane,
                 localToPixel: Matrix44) -> None:
        """
        Constructs a mouse constrained by a plane. The constraint plane contains
        the specified origin point and is parallel to the specified plane. The
        origin point is typically near, but not necessarily on, the specified
        plane.
        
        Parameters
        -----------
        event : MouseEvent
            the initial mouse event.
        origin : Point3
            the origin point, in local coordinates.
        plane : Plane
            the plane, in local coordinates.
        localToPixel : Matrix44
            the transform from local to pixel coordinates.
        """

    def getPoint(self, event: MouseEvent) -> Point3:
        """
        Gets the constrained point in local coordinates for the specified event.
        The constrained point lies in the constraint plane that contains the
        origin point.
        
        Parameters
        -----------
        event : MouseEvent
            the mouse event.
        
        Returns
        --------
        output : Point3
            the constrained point, in local coordinates.
        """
