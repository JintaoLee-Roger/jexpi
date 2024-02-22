from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Node:
    """
    A node in the scene graph.
    
    A node has zero or more parents. Because the number of parents can
    be greater than one, the scene graph forms a directed acyclic graph
    (DAG). However, the DAG has a single root node, called a {@link World}.
    A node can be moved from one world to another, but cannot exist in more
    than one world at a time.
    
    A world maintains a selected set of nodes within it. Only nodes that
    implement the marker interface {@link Selectable} can be selected.
    For convenience, the methods of that interface are implemented in this
    abstract base class. Classes that extend this abstract base class may
    override the method {@link #selectedChanged()}, typically to modify
    the appearance of selected nodes.
    
    Nodes are drawn in what is called the <em>draw process</em>. The draw
    process is applied to a node in three steps by calling the methods
    {@link #drawBegin(DrawContext)},
    {@link #draw(DrawContext)}, and
    {@link #drawEnd(DrawContext)}, in that order. The actual drawing occurs
    in the method {@link #draw(DrawContext)}. Think of the other two methods
    as like opening and closing braces. They might save and restore OpenGL
    state, or otherwise push and pop state required for drawing. Nodes must
    not leak OpenGL state set while drawing.
    
    To facilitate drawing and picking, all nodes have a bounding sphere.
    Ideally, this bounding sphere is the smallest sphere that contains the
    node's geometry. Nodes with bounding spheres that do not intersect a
    view's frustum will be culled, and not drawn or picked within that
    view. Bounding spheres are specified in local coordinates.
    """

    def isSelected(self) -> bool:
        """
        Determines whether this node is currently selected. Only nodes that
        implement the marker interface {@link Selectable} can be selected.
        Returns
        --------
        output : bool
            true, if selected; false, otherwise.
        """

    def setSelected(self, selected: bool) -> None:
        """
        Sets the selected state for this node. Only nodes that implement the
        marker interface {@link Selectable} can be selected. This method does
        nothing if this node is not selectable.
        
        Classes that extend this abstract base class may override the method
        {@link #selectedChanged()}, typically to alter the appearance of a
        node that has been selected or deselected.
        
        Parameters
        -----------
        selected : bool
            true, for selected; false, otherwise.
        """

    def countParents(self) -> int:
        """
        Returns the number of parents of this node.
        Returns
        --------
        output : int
            the number of parents.
        """

    def getParents(self) -> Iterator:
        """
        Gets an iterator for the parents of this node.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def getWorld(self) -> World:
        """
        Gets the world for this node.
        Returns
        --------
        output : World
            the world; null, if this node is not currently in a world.
        """

    def dirtyDraw(self) -> None:
        """
        Marks dirty the drawing of this node. Calling this method causes
        a repaint of all view canvases in which this node may be rendered.
        """

    def getBoundingSphere(self, finite: bool) -> BoundingSphere:
        """
        Gets the bounding sphere for this node. If a finite bounding sphere
        is specified, then any infinite bounding sphere is replaced by an
        empty bounding sphere, so that the returned sphere is always finite.
        
        Parameters
        -----------
        finite : bool
            true, to force bounding sphere to be finite.
        
        Returns
        --------
        output : BoundingSphere
            the bounding sphere.
        """

    def dirtyBoundingSphere(self) -> None:
        """
        Marks dirty the bounding sphere of this node (and any parent nodes).
        If dirty when the method {@link #getBoundingSphere(boolean)}
        is next called, this node's bounding sphere will be recomputed.
        """

    def getStates(self) -> StateSet:
        """
        Gets the OpenGL states for this node.
        Returns
        --------
        output : StateSet
            the OpenGL states.
        """

    def setStates(self, states: StateSet) -> None:
        """
        Sets the OpenGL states for this node.
        
        Parameters
        -----------
        states : StateSet
            the OpenGL states.
        """

    def pick(self, pc: PickContext) -> None:
        """
        Picks this node. This implementation does nothing. Implementations
        of this method in classes that extend this class may test the pick
        segment for intersection with node geometry. If an intersection is
        found, then a pick result should be added to the context.
        
        Parameters
        -----------
        pc : PickContext
            the pick context.
        """
