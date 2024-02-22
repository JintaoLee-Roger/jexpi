
from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class DrawList:
    """
    A list of arrays of nodes (and their parents) to be drawn.
    
    Each leaf node to be drawn is represented in this list by an array of
    nodes. The last node in each array is the leaf node to be drawn, the
    next to last node is that leaf node's parent, and so on. The first node
    in each array is the root node of the scene graph.
    
    Conceptually, this list draws each array of nodes as follows. Starting
    with the first (top) node, and working from top to bottom, this list
    calls {@link Node#drawBegin(DrawContext)} for each node in the array.
    It then calls {@link Node#draw(DrawContext)} for the last (bottom) node.
    Finally, starting with that last node, and working from bottom to top,
    it calls {@link Node#drawEnd(DrawContext)} for each node in the array.
    
    In practice, at least some parent nodes are likely to be the same from
    one array to the next. For example, the first (top) node is likely to
    be the same in all arrays of nodes. Therefore, during drawing, this
    list avoids any redundant calls to {@link Node#drawEnd(DrawContext)}
    and {@link Node#drawBegin(DrawContext)}.
    """

    def append(self, nodes: Node1D) -> None:
        """
        Appends the specified array of nodes to this draw list.
        
        Parameters
        -----------
        nodes : Node[]
            the array of nodes; referenced, not copied.
        """
    def draw(self, dc: DrawContext) -> None:
        """
        Draws all nodes in this list.
        
        Parameters
        -----------
        dc : DrawContext
            the draw context.
        """