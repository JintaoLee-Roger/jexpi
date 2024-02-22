from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class World:
    """
    A world is a root node in the scene graph. A world is a group that
    cannot be a child of any other group. To be viewed, a node must be
    part of a world.
    
    A world maintains a list of views in which it is drawn. When a world
    must be redrawn, it requests a repaint of its views.
    
    A world maintains a set of selected nodes. The selected set of a world is
    updated when (1) a node is added/removed to/from a world or any group that
    is part of a world, or (2) a node in a world is selected or deselected.
    """

    def countViews(self) -> int:
        """
        Returns the number of views of this world.
        Returns
        --------
        output : int
            the number of views.
        """

    def getViews(self) -> Iterator:
        """
        Gets an iterator for the views of this world.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def countSelected(self) -> int:
        """
        Returns the number of selected nodes in this world.
        Returns
        --------
        output : int
            the number of selected nodes.
        """

    def getSelected(self) -> Iterator:
        """
        Gets an iterator for selected nodes in this world.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def clearSelected(self) -> None:
        """
        Deselects all selected nodes in this world.
        """

    def clearSelectedExcept(self, nodeToIgnore: Selectable) -> None:
        """
        Deselects all selected nodes in this world, except the specified node.
        Typically, this method is called to deselect any other nodes that may
        be currently selected, before selecting the specified node.
        node will not be changed.
        
        Parameters
        -----------
        nodeToIgnore : Selectable
            the node to ignore. The selected state of this
        """

    def dirtyDraw(self) -> None:
        """
        Marks dirty the drawing of this world. Calling this method causes
        a repaint of all view canvases in which this world may be drawn.
        """

    def dirtyBoundingSphere(self) -> None:
        """
        Marks dirty the bounding sphere of this world.
        """

    def repaint(self) -> None:
        """
        Requests a repaint of all view canvases of all views of this world.
        """

    def getWorld(self) -> World:
        """
        Gets the world for this node. This implementation overrides that
        in {@link Node#getWorld()} to simply return this world.
        Returns
        --------
        output : World
            this world.
        """
