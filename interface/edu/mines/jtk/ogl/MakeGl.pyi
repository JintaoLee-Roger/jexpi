from typing import overload
from edu.mines.jtk.mapping import *


class MakeGl:
    """
    Makes OpenGL wrapper class Gl.java for JOGL.
    GL.
    To make a new Gl.java, copy the javadoc files GL.html from JOGL
    and run this program. The currently required files GL.html are
    in the list of inputFileNames declared below.
    
    NOTE: This program does not currently generate a Gl.java that will
    compile, mostly due to duplicate declarations of constants and
    functions in the various GL interfaces provided by JOGL. Therefore,
    some editing of the generated Gl.java is required.
    
    This program will require modification if the format of JOGL's
    javadoc-generated html files changes.
    
    An alternative to this program would be to use reflection on the JOGL
    class file com.jogamp.opengl.GL.class, but this alternative would not
    preserve the names of method parameters. A better alternative would be
    for JOGL to provide these bindings.
    """

    @staticmethod
    def main(self, args: String1D) -> None:
        """
    
        """
