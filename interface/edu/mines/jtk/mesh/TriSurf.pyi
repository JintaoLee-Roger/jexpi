from typing import overload
from edu.mines.jtk.mapping import *


class TriSurf:
    """
    A 3-D triangulated manifold oriented surface, possibly with boundary.
    
    This class currently enables construction of a surface from a set of
    points, using the algorithm of Cohen-Steiner and Da, 2002, A greedy
    Delaunay based surface reconstruction algorithm: The Visual Computer,
    v. 20, p. 4-16.
    """

    def addNode(self, node: Node) -> bool:
        """
        Adds the specified node to this surface, if not already present.
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : bool
            true, if node was added; false, otherwise.
        """

    def addNodes(self, nodes: Node1D) -> bool:
        """
        Adds the specified nodes to this surface, if not already present.
        
        Parameters
        -----------
        nodes : Node[]
            the nodes.
        
        Returns
        --------
        output : bool
            true, if all nodes were added; false, otherwise.
        """

    def removeNode(self, node: Node) -> bool:
        """
        Removes the specified node from this surface, if present.
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : bool
            true, if node was removed; false, otherwise.
        """

    def removeNodes(self, nodes: Node1D) -> bool:
        """
        Removes the specified nodes from this surface, if present.
        
        Parameters
        -----------
        nodes : Node[]
            the nodes.
        
        Returns
        --------
        output : bool
            true, if all nodes were removed; false, otherwise.
        """

    def countNodes(self) -> int:
        """
        Returns the number of nodes in the surface.
        Returns
        --------
        output : int
            the number of nodes.
        """

    @overload
    def countFaces(self) -> int:
        """
        Returns the number of faces in the surface.
        Returns
        --------
        output : int
            the number of faces.
        """

    def getNodes(self) -> NodeIterator:
        """
        Gets an iterator for all nodes in this surface.
        Returns
        --------
        output : NodeIterator
            the iterator.
        """

    @overload
    def getFaces(self) -> FaceIterator:
        """
        Gets an iterator for all faces in this surface.
        Returns
        --------
        output : FaceIterator
            the iterator.
        """

    def findNodeNearest(self, x: float, y: float, z: float) -> Node:
        """
        Finds the node nearest to the point with specified coordinates.
        
        Parameters
        -----------
        x : float
            the x coordinate.
        y : float
            the y coordinate.
        z : float
            the z coordinate.
        
        Returns
        --------
        output : Node
            the nearest node.
        """

    @overload
    def getFaceNabors(self, node: Node) -> Face1D:
        """
        Gets an array of face nabors of the specified node.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        
        Returns
        --------
        output : Face[]
            the array of nabors.
        """

    @overload
    def getFaceNabors(self, node: Node, nabors: FaceList) -> None:
        """
        Appends the face nabors of the specified node to the specified list.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        nabors : FaceList
            the list to which nabors are appended.
        """

    @overload
    def findFace(self, node: Node) -> Face:
        """
        Returns a face that references the specified node.
        the node is not in the surface or the surface has no faces.
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : Face
            a face that references the specified node; or null, if
        """

    @overload
    def findFace(self, node1: Node, node2: Node) -> Face:
        """
        Returns a face that references the specified nodes.
        if a node is not in the surface or the surface has no faces.
        
        Parameters
        -----------
        node1 : Node
            a node.
        node2 : Node
            a node.
        
        Returns
        --------
        output : Face
            a face that references the specified nodes; or null,
        """

    @overload
    def findFace(self, node1: Node, node2: Node, node3: Node) -> Face:
        """
        Returns a face that references the specified nodes.
        if a node is not in the surface or the surface has no faces.
        
        Parameters
        -----------
        node1 : Node
            a node.
        node2 : Node
            a node.
        node3 : Node
            a node.
        
        Returns
        --------
        output : Face
            a face that references the specified nodes; or null,
        """

    def findEdge(self, nodeA: Node, nodeB: Node) -> Edge:
        """
        Returns a directed edge AB that references the specified nodes.
        or null, if nodes A and B are not adjacent in the surface.
        
        Parameters
        -----------
        nodeA : Node
            a node.
        nodeB : Node
            a node.
        
        Returns
        --------
        output : Edge
            a directed edge that references the specified nodes;
        """
