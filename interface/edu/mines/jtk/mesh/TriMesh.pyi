from typing import overload
from edu.mines.jtk.mapping import *


class TriMesh:
    """
    A triangular mesh.
    
    Each tri in the mesh references three nodes. Depending on the context,
    these three nodes are labelled as 0, 1, and 2, or A, B, and C, in
    counter-clockwise (CCW) order. Here is a picture:
    <pre><code>
    2(C)
    / \
    /    \
    0(A)------- 1(B)
    </code></pre>
    Each tri has up to three neighbors (nabors), corresponding to the three
    edges of the tri. Tris on the convex hull of the mesh have one or more
    null nabors. Each nabor is labelled by the node opposite its edge. For
    example, the tri nabor 0 (or A) is opposite the node 0 (or A).
    
    Nodes are constructed with float coordinates that are stored internally
    as perturbed doubles. This perturbation minimizes the likelihood that
    three or more nodes are exactly co-linear, or that four or more nodes
    lie exactly on the circumcircle of any tri in the mesh. Only the least
    significant bits of the double coordinates are altered, so that casting
    the perturbed doubles to floats always yields the float coordinates
    with which nodes are constructed.
    """

    def __init__(self) -> None:
        """
        Constructs an empty mesh.
        """

    def getNodePropertyMap(self, name: String) -> NodePropertyMap:
        """
        Gets the node property map with the specified name.
        If this mesh does not have a node property map with the specified
        name, this method creates one.
        
        Parameters
        -----------
        name : String
            the property map name.
        
        Returns
        --------
        output : NodePropertyMap
            the node property map.
        """

    def hasNodePropertyMap(self, name: String) -> bool:
        """
        Determines whether this mesh has a node property map with specified name.
        
        Parameters
        -----------
        name : String
            the property map name.
        
        Returns
        --------
        output : bool
            true, if this mesh has the map; false, otherwise.
        """

    def getNodePropertyMapNames(self) -> String1D:
        """
        Returns the names of the node property maps.
        Returns
        --------
        output : String1D
            an array containing the names of the property maps
        """

    def addNodeListener(self, nl: NodeListener) -> None:
        """
        Adds the specified node listener.
        
        Parameters
        -----------
        nl : NodeListener
            the node listener.
        """

    def removeNodeListener(self, nl: NodeListener) -> None:
        """
        Removes the specified node listener.
        
        Parameters
        -----------
        nl : NodeListener
            the node listener.
        """

    def addTriListener(self, tl: TriListener) -> None:
        """
        Adds the specified tri listener.
        
        Parameters
        -----------
        tl : TriListener
            the tri listener.
        """

    def removeTriListener(self, tl: TriListener) -> None:
        """
        Removes the specified tri listener.
        
        Parameters
        -----------
        tl : TriListener
            the tri listener.
        """

    def countNodes(self) -> int:
        """
        Returns the number of nodes in the mesh.
        Returns
        --------
        output : int
            the number of nodes.
        """

    def countTris(self) -> int:
        """
        Returns the number of tris in the mesh.
        Returns
        --------
        output : int
            the number of tris.
        """

    def getVersion(self) -> long:
        """
        Gets the version number for the mesh. The version number is incremented
        whenever the mesh changes. Therefore, this number can be used to lazily
        determine if the mesh has changed. Comparing version numbers may in
        some applications serve as a cheap alternative to adding node and tri
        listeners to the mesh.
        Returns
        --------
        output : long
            the version number.
        """

    def addNode(self, node: Node) -> bool:
        """
        Adds a node to the mesh, if the mesh does not already contain
        a node with the same (x,y) coordinates.
        
        Parameters
        -----------
        node : Node
            the node to add.
        
        Returns
        --------
        output : bool
            true, if the node was added; false, otherwise.
        """

    def removeNode(self, node: Node) -> bool:
        """
        Removes a node from the mesh, if the node is in the mesh.
        
        Parameters
        -----------
        node : Node
            the node to remove.
        
        Returns
        --------
        output : bool
            true, if the node was (in the mesh and) removed; false, otherwise.
        """

    def moveNode(self, node: Node, x: float, y: float) -> bool:
        """
        Moves a node in the mesh to the specified (x,y) coordinates.
        Roughly equivalent to (but potentially more efficient than)
        first removing and then adding the node to the mesh at the
        specified coordinates. However, if the node is not in the mesh,
        then it will be moved, but not added to the mesh. Also, if the
        specified coordinates are already occupied by another node in
        the mesh, then the specified node is not moved.
        
        Parameters
        -----------
        node : Node
            a node in the mesh.
        x : float
            the x coordinate of the moved node.
        y : float
            the y coordinate of the moved node.
        
        Returns
        --------
        output : bool
            true, if the node was moved; false, otherwise.
        """

    def findNodeNearest(self, x: float, y: float) -> Node:
        """
        Finds the node nearest to the point with specified coordinates.
        
        Parameters
        -----------
        x : float
            the x coordinate.
        y : float
            the y coordinate.
        
        Returns
        --------
        output : Node
            the nearest node.
        """

    def findEdge(self, na: Node, nb: Node) -> Edge:
        """
        Finds an edge of a tri in the mesh that references the specified nodes.
        The nodes may be specified in any order. However, if not null,
        the returned edge always has a mate, and either the returned
        edge or its mate references the specified nodes in the specified
        order.
        If no such edge exists in this mesh, returns null.
        
        Parameters
        -----------
        na : Node
            a node.
        nb : Node
            a node.
        
        Returns
        --------
        output : Edge
            an edge of a tri that references the specified nodes.
        """

    @overload
    def findTri(self, node: Node) -> Tri:
        """
        Returns a tri that references the specified node.
        or null, if the node is not in the mesh or the mesh
        has no tris.
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : Tri
            a tri that references the specified node;
        """

    @overload
    def findTri(self, na: Node, nb: Node) -> Tri:
        """
        Returns a tri that references the specified nodes.
        or null, if a node is not in the mesh or the mesh
        has no tris.
        
        Parameters
        -----------
        na : Node
            a node.
        nb : Node
            a node.
        
        Returns
        --------
        output : Tri
            a tri that references the specified nodes;
        """

    @overload
    def findTri(self, na: Node, nb: Node, nc: Node) -> Tri:
        """
        Returns a tri that references the specified nodes.
        or null, if a node is not in the mesh or the mesh
        has no tris.
        
        Parameters
        -----------
        na : Node
            a node.
        nb : Node
            a node.
        nc : Node
            a node.
        
        Returns
        --------
        output : Tri
            a tri that references the specified nodes;
        """

    def locatePoint(self, x: float, y: float) -> PointLocation:
        """
        Locates a point with specified coordinates.
        
        Parameters
        -----------
        x : float
            the x coordinate.
        y : float
            the y coordinate.
        
        Returns
        --------
        output : PointLocation
            the {@link PointLocation}.
        """

    def getNodes(self) -> NodeIterator:
        """
        Gets an iterator for all nodes in the mesh.
        Returns
        --------
        output : NodeIterator
            the iterator.
        """

    def getTris(self) -> TriIterator:
        """
        Gets an iterator for all tris in the mesh.
        Returns
        --------
        output : TriIterator
            the iterator.
        """

    def getEdgesOnHull(self) -> EdgeIterator:
        """
        Gets an iterator for all edges on the hull of the mesh.
        Returns
        --------
        output : EdgeIterator
            the iterator.
        """

    @overload
    def getNodeNabors(self, node: Node) -> Node1D:
        """
        Gets an array of node nabors of the specified node.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        
        Returns
        --------
        output : Node[]
            the array of nabors.
        """

    @overload
    def getNodeNabors(self, node: Node, nabors: NodeList) -> None:
        """
        Appends the node nabors of the specified node to the specified list.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        nabors : NodeList
            the list to which nabors are appended.
        """

    @overload
    def getNodeNabors(self, node: Node, stepMax: int) -> NodeStepList:
        """
        Finds all node nabors that are within the specified maximum
        number of steps of the specified node. Also, determines the
        number of steps from the specified node to each nabor node.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        stepMax : int
            the maximum number of steps; must not exceed 256.
        
        Returns
        --------
        output : NodeStepList
            a list of nodes with corresponding steps.
        """

    @overload
    def getTriNabors(self, node: Node) -> Tri1D:
        """
        Gets an array of tri nabors of the specified node.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        
        Returns
        --------
        output : Tri[]
            the array of nabors.
        """

    @overload
    def getTriNabors(self, node: Node, nabors: TriList) -> None:
        """
        Appends the tri nabors of the specified node to the specified list.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        nabors : TriList
            the list to which nabors are appended.
        """

    @overload
    def getTriNabors(self, edge: Edge) -> Tri1D:
        """
        Gets an array of tri nabors of the specified edge.
        
        Parameters
        -----------
        edge : Edge
            the edge for which to get nabors.
        
        Returns
        --------
        output : Tri[]
            the array of nabors.
        """

    @overload
    def getTriNabors(self, edge: Edge, nabors: TriList) -> None:
        """
        Appends the tri nabors of the specified edge to the specified list.
        
        Parameters
        -----------
        edge : Edge
            the edge for which to get nabors.
        nabors : TriList
            the list to which nabors are appended.
        """

    @overload
    def getEdgeNabors(self, node: Node) -> Edge1D:
        """
        Gets a new array containing the edge nabors of the specified node.
        The edges are stored in CCW order, and all are directed towards the
        specified node. (In other words, node B of each edge nabor is the
        specified node.) Their corresponding edge mates are not stored.
        The array length equals the number of nabors.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        
        Returns
        --------
        output : Edge[]
            the array of edge nabors.
        """

    @overload
    def getEdgeNabors(self, node: Node, nabors: EdgeList) -> None:
        """
        Stores the edge nabors of the specified node in the specified array.
        The edges are stored in CCW order, and all are directed towards the
        specified node. (In other words, node B of each edge nabor is the
        specified node.) Their corresponding edge mates are not stored.
        
        This method is the most efficient way to get the nabors, because it
        does not create a new array. However, it throws an exception if the
        specified array has insufficient length to store all of the nabors.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        nabors : EdgeList
            the array in which to store the nabors.
        """

    def setOuterBox(self, xmin: float, ymin: float, xmax: float,
                    ymax: float) -> None:
        """
        Sets and enables the outer box for this mesh.
        Tris with circumcircles entirely within the specified box
        are <em>inner</em> tris. All other tris are outer tris.
        An inner node or edge has one or more inner tri nabors;
        an outer node or edge has no inner tri nabors.
        
        The outer box is typically set to be slightly larger than the
        bounding box of the convex hull of the mesh, so that outer tris
        lie near the convex hull. These outer tris tend to have poor
        quality, and are often ignored in iterations over tris.
        
        Parameters
        -----------
        xmin : float
            minimum x coordinate of box.
        ymin : float
            minimum y coordinate of box.
        xmax : float
            maximum x coordinate of box.
        ymax : float
            maximum y coordinate of box.
        """

    def enableOuterBox(self) -> None:
        """
        Enables outer box testing.
        With outer box testing enabled, tris are either inner or outer.
        By default, outer box testing is disabled.
        """

    def disableOuterBox(self) -> None:
        """
        Disables outer box testing, without altering the outer box.
        With outer box testing disabled, all tris are inner.
        By default, outer box testing is disabled.
        """

    @overload
    def isInner(self, node: Node) -> bool:
        """
        Determines whether the specified node is an inner node.
        
        Parameters
        -----------
        node : Node
            a node.
        
        Returns
        --------
        output : bool
            true, if inner; false, otherwise.
        """

    @overload
    def isOuter(self, node: Node) -> bool:
        """
        Determines whether the specified node is an outer node.
        
        Parameters
        -----------
        node : Node
            a node.
        
        Returns
        --------
        output : bool
            true, if outer; false, otherwise.
        """

    @overload
    def isInner(self, tri: Tri) -> bool:
        """
        Determines whether the specified tri is an inner tri.
        
        Parameters
        -----------
        tri : Tri
            a tri.
        
        Returns
        --------
        output : bool
            true, if inner; false, otherwise.
        """

    @overload
    def isOuter(self, tri: Tri) -> bool:
        """
        Determines whether the specified tri is an outer tri.
        
        Parameters
        -----------
        tri : Tri
            a tri.
        
        Returns
        --------
        output : bool
            true, if outer; false, otherwise.
        """

    @overload
    def isInner(self, edge: Edge) -> bool:
        """
        Determines whether the specified edge is an inner edge.
        
        Parameters
        -----------
        edge : Edge
            an edge.
        
        Returns
        --------
        output : bool
            true, if inner; false, otherwise.
        """

    @overload
    def isOuter(self, edge: Edge) -> bool:
        """
        Determines whether the specified edge is an outer edge.
        
        Parameters
        -----------
        edge : Edge
            an edge.
        
        Returns
        --------
        output : bool
            true, if outer; false, otherwise.
        """

    @overload
    def mark(self, node: Node) -> None:
        """
        Marks the specified node (red). Marks are used during iterations
        over nodes. Because nodes (e.g., those nodes adjacent to a
        particular node) are linked in an unordered structure, such
        iterations are often performed by recursively visiting nodes,
        and marks are used to tag nodes that have already been visited.
        
        Parameters
        -----------
        node : Node
            the node to mark (red).
        """

    @overload
    def markRed(self, node: Node) -> None:
        """
        Marks the specified node red.
        This is equivalent to simply marking the node.
        
        Parameters
        -----------
        node : Node
            the node to mark red.
        """

    @overload
    def markBlue(self, node: Node) -> None:
        """
        Marks the specified node blue.
        
        Parameters
        -----------
        node : Node
            the node to mark blue.
        """

    @overload
    def isMarked(self, node: Node) -> bool:
        """
        Determines whether the specified node is marked (red).
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : bool
            true, if the node is marked (red); false, otherwise.
        """

    @overload
    def isMarkedRed(self, node: Node) -> bool:
        """
        Determines whether the specified node is marked red.
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : bool
            true, if the node is marked red; false, otherwise.
        """

    @overload
    def isMarkedBlue(self, node: Node) -> bool:
        """
        Determines whether the specified node is marked blue.
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : bool
            true, if the node is marked blue; false, otherwise.
        """

    def clearNodeMarks(self) -> None:
        """
        Clears all node marks, so that no node is marked. This can usually
        be accomplished without iterating over all nodes in the mesh.
        """

    @overload
    def mark(self, tri: Tri) -> None:
        """
        Marks the specified tri (red). Marks are used during iterations
        over tris. Because tris (e.g., those tris containing a particular
        node) are linked in an unordered structure, such iterations are
        often performed by recursively visiting tris, and marks are used
        to tag tris that have already been visited.
        
        Parameters
        -----------
        tri : Tri
            the tri to mark (red).
        """

    @overload
    def markRed(self, tri: Tri) -> None:
        """
        Marks the specified tri red.
        This is equivalent to simply marking the tri.
        
        Parameters
        -----------
        tri : Tri
            the tri to mark red.
        """

    @overload
    def markBlue(self, tri: Tri) -> None:
        """
        Marks the specified tri blue.
        
        Parameters
        -----------
        tri : Tri
            the tri to mark blue.
        """

    @overload
    def isMarked(self, tri: Tri) -> bool:
        """
        Determines whether the specified tri is marked (red).
        
        Parameters
        -----------
        tri : Tri
            the tri.
        
        Returns
        --------
        output : bool
            true, if the tri is marked (red); false, otherwise.
        """

    @overload
    def isMarkedRed(self, tri: Tri) -> bool:
        """
        Determines whether the specified tri is marked red.
        
        Parameters
        -----------
        tri : Tri
            the tri.
        
        Returns
        --------
        output : bool
            true, if the tri is marked red; false, otherwise.
        """

    @overload
    def isMarkedBlue(self, tri: Tri) -> bool:
        """
        Determines whether the specified tri is marked blue.
        
        Parameters
        -----------
        tri : Tri
            the tri.
        
        Returns
        --------
        output : bool
            true, if the tri is marked blue; false, otherwise.
        """

    def clearTriMarks(self) -> None:
        """
        Clears all tri marks, so that no tri is marked. This can usually
        be accomplished without iterating over all tris in the mesh.
        """

    def validate(self) -> None:
        """
        Validates the internal consistency of the mesh.
        """

    def findNodeNearestSlow(self, x: float, y: float) -> Node:
        """
        Finds the node nearest to the point with specified coordinates.
        This method appears to be 2-3 times slower than findNodeNearest,
        but it is a lot of code, so we make it private for now.
        (Currently unused.)
        
        Parameters
        -----------
        x : float
            x-coordinate.
        y : float
            y-coordinate.
        
        Returns
        --------
        output : Node
            the node nearest the coordinates.
        """
