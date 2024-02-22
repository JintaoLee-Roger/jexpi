from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class AxisAlignedPanel:
    """
    An axis-aligned panel is a special child of an axis-aligned frame.
    Nodes that draw themselves in an axis-aligned frame typically extend
    this abstract class, which handles some node responsibilities, such
    as picking and computing the node's bounding sphere.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a panel with null frame.
        """

    @overload
    def __init__(self, frame: AxisAlignedFrame) -> None:
        """
        Constructs a panel with specified frame.
        
        Parameters
        -----------
        frame : AxisAlignedFrame
            the frame.
        """

    def getFrame(self) -> AxisAlignedFrame:
        """
        Gets the frame for this panel.
        Returns
        --------
        output : AxisAlignedFrame
            the frame; null, if none.
        """

    def setFrame(self, frame: AxisAlignedFrame) -> None:
        """
        Sets the frame for this panel. If the frame is not null and this panel
        has a non-null constraint, then this method sets the constraint of its
        frame accordingly.
        
        Parameters
        -----------
        frame : AxisAlignedFrame
            the frame; null, if none.
        """

    def getBoxConstraint(self) -> BoxConstraint:
        """
        Gets the box constraint for this panel. This implementation simply
        returns null, for no constraint. Panels that extend this class may
        override this method to return a more appropriate constraint.
        Returns
        --------
        output : BoxConstraint
            the box constraint; null, if none.
        """

    def pick(self, pc: PickContext) -> None:
        """
        Picks this panel. This implementation delegates picking to its frame;
        or; if not in a frame, this implementation does nothing.
        
        Panels that extend this class and that precisely fill their quad
        frame when drawn may simply inherit this implementation.
        """
