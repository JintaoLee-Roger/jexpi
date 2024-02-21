
from typing import overload
from edu.mines.jtk.mapping import *


class RTree:
    """
    A tree of bounded objects with methods for fast updates and queries.
    An R-tree's entries are bounded objects with min/max coordinates in N
    dimensions, where N is a parameter specified when constructing an R-tree.
    We refer to these N-dimensional bounds as <em>boxes</em>.
    
    An R-tree facilitates a variety of queries, such as a search for all
    objects with bounds that overlap a specified box, or a search for the
    k objects nearest to a specified point. An R-tree is also dynamic;
    objects may be efficiently added and removed from the tree at any time.
    
    An R-tree uses the N-dimensional coordinate bounds of each object to
    build a hierarchy (a tree) of internal nodes. Each node contains a list
    of child nodes or objects. Each node maintains bounds that tightly
    contain its children. The R-tree attempts to minimize any overlap of
    these internal nodes, so that objects can be quickly found, added, or
    removed.
    
    An R-tree is a set; it contains no duplicate objects. Specifically, an
    R-tree contains no objects b1 and b2 such that b1.equals(b2). Also, an
    R-tree contains no null objects.
    
    To reduce memory consumption, an object's bounds are not stored in the
    R-tree. These bounds may be either computed on demand or cached by the
    object itself. However, while an object is in an R-tree, it should not
    be changed in any way that would affect its equality comparison or its
    bounds. The result of such a change is undefined.
    
    References:
    <ul><li>
    Guttman A., 1984, R-trees - a dynamic index structure for spatial
    searching: Proceedings of the ACM, SIGMOD, p. 47-57.
    </li><li>
    Roussopoulos, N., Kelley, S., and Vincent, F., 1995, Nearest neighbor
    queries: Proceedings of the ACM, SIGMOD, p. 71-79.
    </li><li>
    Cheung, K.L., and Fu, A.W.C., 1998, Enhanced nearest neighbor search
    on the R-tree: SIGMOD Record, v. 27, n. 3, p. 16-21.
    </li></ul>
    """

    @overload
    def __init__(self, ndim: int, nmin: int, nmax: int) -> None:
        """
        Constructs an R-tree with specified parameters.
        equals the number of min/max coordinates per object.
        must not be less than one or greater than nmax/2.
        must not be less than 4.
        
        Parameters
        -----------
        ndim : int
            the number of dimensions per object;
        nmin : int
            the minimum number of objects per node;
        nmax : int
            the maximum number of objects per node;
        """
    @overload
    def __init__(self, ndim: int, nmin: int, nmax: int, boxer: Boxer) -> None:
        """
        Constructs an R-tree with specified parameters.
        equals the number of min/max coordinates per object.
        must not be less than one or greater than nmax/2.
        must not be less than 4.
        objects added to this tree.
        
        Parameters
        -----------
        ndim : int
            the number of dimensions per object;
        nmin : int
            the minimum number of objects per node;
        nmax : int
            the maximum number of objects per node;
        boxer : Boxer
            the {@link Boxer} used to compute the bounds of
        """
    def size(self) -> int:
        """
        Returns the size of this tree. The size is the number of objects
        added minus the number of objects removed from this tree.
        Returns
        --------
        output : int
            the number of boxed objects.
        """
    def clear(self) -> None:
        """
        Removes all objects from this tree.
        """
    def isEmpty(self) -> bool:
        """
        Returns true if this tree contains no objects.
        Returns
        --------
        output : bool
            true, if empty; false, otherwise.
        """
    def add(self, object: Object) -> bool:
        """
        Adds the specified object to this tree, if not already present.
        
        Parameters
        -----------
        object : Object
            the object.
        
        Returns
        --------
        output : bool
            true, if the object was added; false, otherwise.
        """
    def addPacked(self, objects: Object[]) -> int:
        """
        Adds the specified objects to this tree, if not already present.
        This method packs the objects, which means that it adds them in a
        special order. The goal is to reduce (1) the cost of building the
        R-tree, (2) the cost of subsequent queries, and (3) the memory
        consumed by the R-tree. However, depending on the locations and
        sizes of the added objects, packing may increase these costs.
        Packing seems to work best for uniformly distributed objects with
        similar size. Also, packing is best when this method is called for
        an empty R-tree.
        
        Parameters
        -----------
        objects : Object[]
            the objects.
        
        Returns
        --------
        output : int
            the number of objects added.
        """
    @overload
    def remove(self, object: Object) -> bool:
        """
        Deletes the specified object from this tree, if present.
        
        Parameters
        -----------
        object : Object
            the object.
        
        Returns
        --------
        output : bool
            true, if the object was removed; false, otherwise.
        """
    def contains(self, object: Object) -> bool:
        """
        Determines whether this tree contains the specified object.
        
        Parameters
        -----------
        object : Object
            the object.
        
        Returns
        --------
        output : bool
            true, if the object is in this tree; false, otherwise.
        """
    def iterator(self) -> Iterator:
        """
        Returns an iterator for all objects in this tree.
        
        The iterator does not support removal. A call to the method
        {@link java.util.Iterator#remove()} will cause a
        {@link java.lang.UnsupportedOperationException}.
        
        The iterator does not support concurrent modification. If this tree
        is modified after the iterator has been returned, a subsequent call
        to the method {@link java.util.Iterator#next()} will cause a
        {@link java.util.ConcurrentModificationException}.
        Returns
        --------
        output : Iterator
            the iterator.
        """
    def getLevels(self) -> int:
        """
        Gets the number of levels in this tree.
        Returns
        --------
        output : int
            the number of levels.
        """
    @overload
    def findOverlapping(self, min: Float1D, max: Float1D) -> Object[]:
        """
        Finds all objects with bounds that overlap the specified bounds.
        
        Parameters
        -----------
        min : Float1D
            array of bounding min coordinates.
        max : Float1D
            array of bounding max coordinates.
        
        Returns
        --------
        output : Object[]
            the array of objects found.
        """
    @overload
    def findOverlapping(self, box: Box) -> Object[]:
        """
        Finds all objects with bounds that overlap the specified box.
        
        Parameters
        -----------
        box : Box
            the box.
        
        Returns
        --------
        output : Object[]
            the array of objects found.
        """
    def findInSphere(self, center: Float1D, radius: float) -> Object[]:
        """
        Finds all objects in a specified sphere. An object is considered
        <em>in</em> the sphere if the distance from the sphere's center to
        the object (not its bounds) is less than or equal to the sphere's
        radius.
        
        Parameters
        -----------
        center : Float1D
            array of sphere center coordinates.
        radius : float
            the sphere radius.
        
        Returns
        --------
        output : Object[]
            the array of objects found.
        """
    @overload
    def findNearest(self, point: Float1D) -> Object:
        """
        Finds the object nearest to the specified point.
        
        Parameters
        -----------
        point : Float1D
            array of point coordinates.
        
        Returns
        --------
        output : Object
            the nearest object; null, if this tree is empty.
        """
    @overload
    def findNearest(self, k: int, point: Float1D) -> Object[]:
        """
        Finds the k objects nearest to the specified point.
        
        Parameters
        -----------
        k : int
            the number of nearest objects to find.
        point : Float1D
            array of point coordinates.
        
        Returns
        --------
        output : Object[]
            the array of objects, ordered by increasing distance to the point.
        """
    def getLeafArea(self) -> float:
        """
        Gets the leaf node area, the sum of the areas of all leaf node boxes.
        Returns
        --------
        output : float
            the area.
        """
    def getLeafVolume(self) -> float:
        """
        Gets the leaf node volume, the sum of the volumes of all leaf node boxes.
        Returns
        --------
        output : float
            the volume.
        """
    def dump(self) -> None:
        """
        Prints this tree to the standard output stream.
        Intended for debugging, only.
        """
    def validate(self) -> None:
        """
        Validates the internal state of this tree.
        Intended for debugging, only, with assertions enabled.
        """