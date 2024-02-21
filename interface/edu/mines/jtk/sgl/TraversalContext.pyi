
from typing import overload
from edu.mines.jtk.mapping import *


class TraversalContext:
    """
    A context for scene graph traversal. A traversal context maintains
    a current node and a list of its parent nodes. Because nodes in the
    scene graph may have multiple parents, a node may become current at
    more than time during a traversal, each time with a different list
    of parent nodes.
    """

    def countNodes(self) -> int:
        """
        Returns the number of current and parent nodes in this traversal.
        Returns
        --------
        output : int
            the number of nodes.
        """
    @overload
    def getNode(self) -> Node:
        """
        Gets the current node in this traversal.
        Returns
        --------
        output : Node
            the current node.
        """
    @overload
    def getNode(self, index: int) -> Node:
        """
        Gets the node in this traversal with specified index. If count is the
        number of nodes returned by the method {@link #countNodes()}, then the
        current node has index count-1, and the root node has index zero.
        
        If the specified index is negative, then count is added to the index.
        Therefore, the index -1 will get the current node, the index -2 will
        get its parent node, and so on.
        
        Parameters
        -----------
        index : int
            the index.
        
        Returns
        --------
        output : Node
            the node.
        """
    def getNodes(self) -> Node1D:
        """
        Gets an array of nodes representing the state of this traversal.
        Nodes in the array are ordered from parent to child. The last node
        in the array is the current node, the next to last node is the
        current node's parent, and so on.
        Returns
        --------
        output : Node[]
            the array of nodes.
        """
    def pushNode(self, node: Node) -> None:
        """
        Saves the current node, and then makes the specified node current.
        
        Parameters
        -----------
        node : Node
            the new current node.
        """
    def popNode(self) -> None:
        """
        Restores the most recently saved (pushed) node.
        Discards the current node.
        """