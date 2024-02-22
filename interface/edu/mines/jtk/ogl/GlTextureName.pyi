from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class GlTextureName:
    """
    An OpenGL texture name. When constructed, a texture name calls
    glGenTextures to generate a single texture name. When disposed, it
    calls glDeleteTextures to delete any OpenGL resources bound to that
    name. If not disposed explicitly, a texture name will dispose itself
    when finalized during garbage collection.
    
    This class exists to implement the finalize method and thereby reduce
    the likelihood of OpenGL resource leaks. However, it is not foolproof,
    for two reasons. First, there is no guarantee that a texture name will
    ever be finalized. Second, to call glDeleteTextures, a texture name must
    lock an OpenGL context, and the only context it knows is the one in which
    it was constructed. That context may have been disposed, but the texture
    name may have been shared in a different unknown context. In this case,
    texture resources may be leaked in that unknown context.
    """

    def __init__(self) -> None:
        """
        Constructs a texture name in the current OpenGL context.
        Calls glGenTextures to create one texture object.
        """

    def name(self) -> int:
        """
        Returns the integer name corresponding to this texture name.
        Returns
        --------
        output : int
            the name; zero, if this texture name has been disposed.
        """

    def dispose(self) -> None:
        """
        Disposes this texture name. When practical, this method should be called
        explicitly. Otherwise, it will be called when this object is finalized
        during garbage collection.
        """
