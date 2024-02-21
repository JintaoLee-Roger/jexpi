from typing import overload
from edu.mines.jtk.mapping import *


class TetMesh:
    """
    A tetrahedral mesh.
    
    Each tet in the mesh references four nodes. Depending on the context,
    these four nodes are labelled as 0, 1, 2, and 3, or A, B, C, D. The
    nodes are ordered such that 1, 2, and 3 (or B, C, and D) are in
    counter-clockwise (CCW) order as viewed from node 0 (or A).
    Here is a picture:
    <pre><code>
    2(C)
    /|\
    / |  \
    0(A)---|--- 3(D)
    \  |  /
    \ | /
    \|/
    1(B)
    </code></pre>
    Each tet has up to four neighbors (nabors), corresponding to the four
    faces of the tet. Tets on the convex hull of the mesh have one or more
    null nabors. Each nabor is labelled by the node opposite its face. For
    example, the tet nabor 0 (or A) is opposite the node 0 (or A).
    
    Faces and edges of each tet are enumerated as follows.
    The four oriented faces of each tet are ABC|D, BDC|A, CDA|B,
    and DBA|C, where the fourth node in each group is referenced
    by the tet, but not the face, and is left of the plane
    defined by the first three nodes.
    Likewise, the six directed edges of each tet are AB|CD, AC|DB,
    AD|BC, BC|AD, BD|CA, and CD|AB, where the third and fourth
    nodes in each group are referenced by the tet, but not the
    edge, and the fourth node is left of the plane defined by the
    first three nodes.
    
    Nodes are constructed with float coordinates that are stored internally
    as perturbed doubles. This perturbation minimizes the likelihood that
    four or more nodes are exactly co-planar, or that five or more nodes
    lie exactly on the circumsphere of any tet in the mesh. Only the least
    significant bits of the double coordinates are altered, so that casting
    the perturbed doubles to floats always yields the float coordinates
    with which nodes are constructed.
    
    A tet mesh is serializable. When written to an object output stream,
    a tet mesh writes its nodes and tets so that any references to them
    from serialized objects not in the mesh will remain valid.
    
    While mesh nodes and tets are serializable alone, most of their state
    is serialized only when the entire mesh is serialized.
    
    Listeners to a tet mesh are not serialized. When a tet mesh is read
    from an object input stream, it will have no listeners.
    """

    def __init__(self) -> None:
        """
        Constructs an empty mesh.
        """

    def countNodes(self) -> int:
        """
        Returns the number of nodes in the mesh.
        Returns
        --------
        output : int
            the number of nodes.
        """

    def countTets(self) -> int:
        """
        Returns the number of tets in the mesh.
        Returns
        --------
        output : int
            the number of tets.
        """

    def getVersion(self) -> long:
        """
        Gets the version number for the mesh. The version number is incremented
        whenever the mesh changes. Therefore, this number can be used to lazily
        determine if the mesh has changed since the version number was last got.
        Comparing version numbers may in some applications serve as a cheap
        alternative to adding node and tet listeners to the mesh.
        Returns
        --------
        output : long
            the version number.
        """

    def addNode(self, node: Node) -> bool:
        """
        Adds a node to the mesh, if the mesh does not already contain
        a node with the same (x,y,z) coordinates.
        
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

    def moveNode(self, node: Node, x: float, y: float, z: float) -> bool:
        """
        Moves a node in the mesh to the specified (x,y,z) coordinates.
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
        z : float
            the z coordinate of the moved node.
        
        Returns
        --------
        output : bool
            true, if the node was moved; false, otherwise.
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

    def findEdge(self, na: Node, nb: Node) -> Edge:
        """
        Finds an edge of a tet in the mesh that references the specified nodes.
        The nodes may be specified in any order.
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
            an edge of a tet that references the specified nodes.
        """

    def findFace(self, na: Node, nb: Node, nc: Node) -> Face:
        """
        Finds a face of a tet in the mesh that references the specified nodes.
        The nodes may be specified in any order. However, if not null,
        the returned face always has a mate, and either the returned
        face or its mate references the specified nodes in the specified
        order.
        If no such face exists in this mesh, returns null.
        
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
        output : Face
            a face of a tet that references the specified nodes.
        """

    @overload
    def findTet(self, node: Node) -> Tet:
        """
        Returns a tet that references the specified node.
        or null, if the node is not in the mesh or the mesh
        has no tets.
        
        Parameters
        -----------
        node : Node
            the node.
        
        Returns
        --------
        output : Tet
            a tet that references the specified node;
        """

    @overload
    def findTet(self, na: Node, nb: Node) -> Tet:
        """
        Returns a tet that references the specified nodes.
        or null, if a node is not in the mesh or the mesh
        has no tets.
        
        Parameters
        -----------
        na : Node
            a node.
        nb : Node
            a node.
        
        Returns
        --------
        output : Tet
            a tet that references the specified nodes;
        """

    @overload
    def findTet(self, na: Node, nb: Node, nc: Node) -> Tet:
        """
        Returns a tet that references the specified nodes.
        or null, if a node is not in the mesh or the mesh
        has no tets.
        
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
        output : Tet
            a tet that references the specified nodes;
        """

    @overload
    def findTet(self, na: Node, nb: Node, nc: Node, nd: Node) -> Tet:
        """
        Returns a tet that references the specified nodes.
        or null, if a node is not in the mesh or the mesh
        has no tets.
        
        Parameters
        -----------
        na : Node
            a node.
        nb : Node
            a node.
        nc : Node
            a node.
        nd : Node
            a node.
        
        Returns
        --------
        output : Tet
            a tet that references the specified nodes;
        """

    def locatePoint(self, x: float, y: float, z: float) -> PointLocation:
        """
        Locates a point with specified coordinates.
        
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

    def getTets(self) -> TetIterator:
        """
        Gets an iterator for all tets in the mesh.
        Returns
        --------
        output : TetIterator
            the iterator.
        """

    def getEdges(self) -> EdgeIterator:
        """
        Gets an iterator for all edges in the mesh.
        Returns
        --------
        output : EdgeIterator
            the iterator.
        """

    def getTetsInPlane(self, a: double, b: double, c: double,
                       d: double) -> TetIterator:
        """
        Gets an iterator for all tets in the mesh that intersect a plane.
        The equation for the specified plane is ax+by+cz+d = 0.
        
        Parameters
        -----------
        a : double
            the coefficient a in the equation for the plane.
        b : double
            the coefficient b in the equation for the plane.
        c : double
            the coefficient c in the equation for the plane.
        d : double
            the coefficient d in the equation for the plane.
        
        Returns
        --------
        output : TetIterator
            the iterator.
        """

    def getNodesNearestPlane(self, a: double, b: double, c: double,
                             d: double) -> NodeIterator:
        """
        Gets an iterator for all nodes in the mesh that are nearest to a plane.
        The equation for the specified plane is ax+by+cz+d = 0.
        
        Nodes nearest the plane are those with Voronoi polyhedra that intersect
        the plane. In other words, a node is nearest the plane if there exists
        some point in the plane that is nearer to that node than to all other
        nodes in the mesh.
        
        Parameters
        -----------
        a : double
            the coefficient a in the equation for the plane.
        b : double
            the coefficient b in the equation for the plane.
        c : double
            the coefficient c in the equation for the plane.
        d : double
            the coefficient d in the equation for the plane.
        
        Returns
        --------
        output : NodeIterator
            the iterator.
        """

    def findTetInPlane(self, a: double, b: double, c: double,
                       d: double) -> Tet:
        """
        Finds a tet that intersects the specified plane ax+by+cz+d = 0.
        
        Parameters
        -----------
        a : double
            the coefficient a in the equation for the plane.
        b : double
            the coefficient b in the equation for the plane.
        c : double
            the coefficient c in the equation for the plane.
        d : double
            the coefficient d in the equation for the plane.
        
        Returns
        --------
        output : Tet
            the tet; null if none intersects the plane.
        """

    def getFacesOnHull(self) -> FaceIterator:
        """
        Gets an iterator for all faces on the hull of the mesh.
        Returns
        --------
        output : FaceIterator
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
    def getTetNabors(self, node: Node) -> Tet1D:
        """
        Gets an array of tet nabors of the specified node.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        
        Returns
        --------
        output : Tet[]
            the array of nabors.
        """

    @overload
    def getTetNabors(self, node: Node, nabors: TetList) -> None:
        """
        Appends the tet nabors of the specified node to the specified list.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        nabors : TetList
            the list to which nabors are appended.
        """

    @overload
    def getTetNabors(self, edge: Edge) -> Tet1D:
        """
        Gets an array of tet nabors of the specified edge.
        
        Parameters
        -----------
        edge : Edge
            the edge for which to get nabors.
        
        Returns
        --------
        output : Tet[]
            the array of nabors.
        """

    @overload
    def getTetNabors(self, edge: Edge, nabors: TetList) -> None:
        """
        Appends the tet nabors of the specified edge to the specified list.
        
        Parameters
        -----------
        edge : Edge
            the edge for which to get nabors.
        nabors : TetList
            the list to which nabors are appended.
        """

    @overload
    def getTetNabors(self, face: Face) -> Tet1D:
        """
        Gets an array of tet nabors of the specified face.
        
        Parameters
        -----------
        face : Face
            the face for which to get nabors.
        
        Returns
        --------
        output : Tet[]
            the array of nabors.
        """

    @overload
    def getTetNabors(self, face: Face, nabors: TetList) -> None:
        """
        Appends the tet nabors of the specified face to the specified list.
        
        Parameters
        -----------
        face : Face
            the face for which to get nabors.
        nabors : TetList
            the list to which nabors are appended.
        """

    @overload
    def getEdgeNabors(self, node: Node) -> Edge1D:
        """
        Gets an array of edge nabors of the specified node.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        
        Returns
        --------
        output : Edge[]
            the array of nabors.
        """

    @overload
    def getEdgeNabors(self, node: Node, nabors: EdgeList) -> None:
        """
        Appends the edge nabors of the specified node to the specified list.
        
        Parameters
        -----------
        node : Node
            the node for which to get nabors.
        nabors : EdgeList
            the list to which nabors are appended.
        """

    @overload
    def getFaceNabors(self, edge: Edge) -> Face1D:
        """
        Gets an array of face nabors of the specified edge.
        The edge is directed, and the faces are stored in CCW order, as
        viewed from a point towards which the edge is directed. Only those
        faces aligned with the edge are stored. Specifically, their mates
        are not stored.
        
        Parameters
        -----------
        edge : Edge
            the edge for which to get nabors.
        
        Returns
        --------
        output : Face[]
            the array of nabors.
        """

    @overload
    def getFaceNabors(self, edge: Edge, nabors: FaceList) -> None:
        """
        Appends the face nabors of the specified edge to the specified list.
        The edge is directed, and the faces are stored in CCW order, as
        viewed from a point towards which the edge is directed. Only those
        faces aligned with the edge are stored. Specifically, their mates
        are not stored.
        
        Parameters
        -----------
        edge : Edge
            the edge for which to get nabors.
        nabors : FaceList
            the list to which nabors are appended.
        """

    def setOuterBox(self, xmin: float, ymin: float, zmin: float, xmax: float,
                    ymax: float, zmax: float) -> None:
        """
        Sets and enables the outer box for this mesh.
        Tets with circumspheres entirely within the specified box
        are <em>inner</em> tets. All other tets are outer tets.
        An inner node, edge, or face has one or more inner tet nabors;
        an outer node, edge, or face has no inner tet nabors.
        
        The outer box is typically set to be slightly larger than the
        bounding box of the convex hull of the mesh, so that outer tets
        lie near the convex hull. These outer tets tend to have poor
        quality, and are often ignored in iterations over tets.
        
        Parameters
        -----------
        xmin : float
            minimum x coordinate of box.
        ymin : float
            minimum y coordinate of box.
        zmin : float
            minimum z coordinate of box.
        xmax : float
            maximum x coordinate of box.
        ymax : float
            maximum y coordinate of box.
        zmax : float
            maximum z coordinate of box.
        """

    def enableOuterBox(self) -> None:
        """
        Enables outer box testing.
        With outer box testing enabled, tets are either inner or outer.
        By default, outer box testing is disabled.
        """

    def disableOuterBox(self) -> None:
        """
        Disables outer box testing, without altering the outer box.
        With outer box testing disabled, all tets are inner.
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
    def isInner(self, tet: Tet) -> bool:
        """
        Determines whether the specified tet is an inner tet.
        
        Parameters
        -----------
        tet : Tet
            a tet.
        
        Returns
        --------
        output : bool
            true, if inner; false, otherwise.
        """

    @overload
    def isOuter(self, tet: Tet) -> bool:
        """
        Determines whether the specified tet is an outer tet.
        
        Parameters
        -----------
        tet : Tet
            a tet.
        
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
    def isInner(self, face: Face) -> bool:
        """
        Determines whether the specified face is an inner face.
        
        Parameters
        -----------
        face : Face
            a face.
        
        Returns
        --------
        output : bool
            true, if inner; false, otherwise.
        """

    @overload
    def isOuter(self, face: Face) -> bool:
        """
        Determines whether the specified face is an outer face.
        
        Parameters
        -----------
        face : Face
            a face.
        
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
    def unmark(self, node: Node) -> None:
        """
        Unmarks the specified node.
        
        Parameters
        -----------
        node : Node
            the node to unmark.
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
    def mark(self, tet: Tet) -> None:
        """
        Marks the specified tet (red). Marks are used during iterations
        over tets. Because tets (e.g., those tets containing a particular
        node) are linked in an unordered structure, such iterations are
        often performed by recursively visiting tets, and marks are used
        to tag tets that have already been visited.
        
        Parameters
        -----------
        tet : Tet
            the tet to mark (red).
        """

    @overload
    def markRed(self, tet: Tet) -> None:
        """
        Marks the specified tet red.
        This is equivalent to simply marking the tet.
        
        Parameters
        -----------
        tet : Tet
            the tet to mark red.
        """

    @overload
    def markBlue(self, tet: Tet) -> None:
        """
        Marks the specified tet blue.
        
        Parameters
        -----------
        tet : Tet
            the tet to mark blue.
        """

    @overload
    def unmark(self, tet: Tet) -> None:
        """
        Unmarks the specified tet.
        
        Parameters
        -----------
        tet : Tet
            the tet to unmark.
        """

    @overload
    def isMarked(self, tet: Tet) -> bool:
        """
        Determines whether the specified tet is marked (red).
        
        Parameters
        -----------
        tet : Tet
            the tet.
        
        Returns
        --------
        output : bool
            true, if the tet is marked (red); false, otherwise.
        """

    @overload
    def isMarkedRed(self, tet: Tet) -> bool:
        """
        Determines whether the specified tet is marked red.
        
        Parameters
        -----------
        tet : Tet
            the tet.
        
        Returns
        --------
        output : bool
            true, if the tet is marked red; false, otherwise.
        """

    @overload
    def isMarkedBlue(self, tet: Tet) -> bool:
        """
        Determines whether the specified tet is marked blue.
        
        Parameters
        -----------
        tet : Tet
            the tet.
        
        Returns
        --------
        output : bool
            true, if the tet is marked blue; false, otherwise.
        """

    def clearTetMarks(self) -> None:
        """
        Clears all tet marks, so that no tet is marked. This can usually
        be accomplished without iterating over all tets in the mesh.
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

    def addTetListener(self, tl: TetListener) -> None:
        """
        Adds the specified tet listener.
        
        Parameters
        -----------
        tl : TetListener
            the tet listener.
        """

    def removeTetListener(self, tl: TetListener) -> None:
        """
        Removes the specified tet listener.
        
        Parameters
        -----------
        tl : TetListener
            the tet listener.
        """

    def validate(self) -> None:
        """
        Validates the internal consistency of the mesh.
        """

    def findNodeNearestSlow(self, x: float, y: float, z: float) -> Node:
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
        z : float
            z-coordinate.
        
        Returns
        --------
        output : Node
            the node nearest to the point {x,y,z}.
        """
