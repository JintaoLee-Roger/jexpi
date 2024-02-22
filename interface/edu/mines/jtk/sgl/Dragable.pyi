from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Dragable:
    """
    An interface implemented by nodes that can be dragged with a mouse.
    """

    def dragBegin(self, dc: DragContext) -> None:
        """
        Begins dragging.
        
        Parameters
        -----------
        dc : DragContext
            the drag context.
        """

    def drag(self, dc: DragContext) -> None:
        """
        During dragging, this method is called when the mouse moves.
        
        Parameters
        -----------
        dc : DragContext
            the drag context.
        """

    def dragEnd(self, dc: DragContext) -> None:
        """
        Ends dragging.
        
        Parameters
        -----------
        dc : DragContext
            the drag context.
        """
