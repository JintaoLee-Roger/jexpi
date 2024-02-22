from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class Group:
    """
    A node in the scene graph that may contain node children.
    """

    def addChild(self, child: Node) -> None:
        """
        Adds the specified child node to this group's list of children. If the
        node is already a child of this group, then this method does nothing.
        
        The child must not be a world (root) node, because a world has no
        parents. Also, if this group is in a world, the child must not already
        be in a different world. A node cannot be in more than one world at a
        time; it must be removed from one world before it can be added to another.
        
        Parameters
        -----------
        child : Node
            the child node.
        """

    def removeChild(self, child: Node) -> None:
        """
        Removes the specified child node from this group's list of children. If
        the node is not a child of this group, then this method does nothing.
        
        Parameters
        -----------
        child : Node
            the child node.
        """

    def countChildren(self) -> int:
        """
        Returns the number of children in this group.
        Returns
        --------
        output : int
            the number of children.
        """

    def getChildren(self) -> Iterator:
        """
        Gets an iterator for the children in this group.
        Returns
        --------
        output : Iterator
            the iterator.
        """

    def pick(self, pc: PickContext) -> None:
        """
        Picks this group. This implementation simply applies the pick process
        to its children.
        
        Parameters
        -----------
        pc : PickContext
            the pick context.
        """
