from typing import overload
from edu.mines.jtk.mapping import *


class GlDisplayList:
    """
    An OpenGL display list. When constructed, a display list calls
    glGenLists to generate one or more display lists. When disposed, it
    calls glDeleteLists to delete any OpenGL resources bound to those
    lists. If not disposed explicitly, a display list will dispose itself
    when finalized during garbage collection.
    
    This class exists to implement the finalize method and thereby reduce
    the likelihood of OpenGL resource leaks. However, it is not foolproof,
    for two reasons. First, there is no guarantee that a display list will
    ever be finalized. Second, to call glDeleteLists, a display list must
    lock an OpenGL context, and the only context it knows is the one in which
    it was constructed. That context may have been disposed, but the display
    list may have been shared in a different unknown context. In this case,
    display list resources may be leaked in that unknown context.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a display list in the current OpenGL context.
        Calls glGenLists to create one display list object.
        """

    @overload
    def __init__(self, range: int) -> None:
        """
        Constructs display lists in the current OpenGL context.
        Calls glGenLists to create the specified number of display list objects.
        
        Parameters
        -----------
        range : int
            the number of display lists.
        """

    def list(self) -> int:
        """
        Returns the integer index corresponding to this display list. If more
        than one list, this method returns the index of the first list.
        Returns
        --------
        output : int
            the index; zero, if this display list has been disposed.
        """

    def range(self) -> int:
        """
        Returns the number of display lists.
        Returns
        --------
        output : int
            the number of display lists; zero, if disposed.
        """

    def dispose(self) -> None:
        """
        Disposes this display list. When practical, this method should be called
        explicitly. Otherwise, it will be called when this object is finalized
        during garbage collection.
        """
