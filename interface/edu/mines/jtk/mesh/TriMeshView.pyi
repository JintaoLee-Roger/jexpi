from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *
from edu.mines.jtk.sgl import *


class TriMeshView:
    """
    Tiled view of a tri mesh.
    """

    def __init__(self, mesh: TriMesh) -> None:
        """
        Constructs a new view of the specified tri mesh.
        
        Parameters
        -----------
        mesh : TriMesh
            a tri mesh.
        """

    def setMesh(self, mesh: TriMesh) -> None:
        """
        Sets the tri mesh rendered by this view.
        
        Parameters
        -----------
        mesh : TriMesh
            the tri mesh.
        """

    def setOrientation(self, orientation: Orientation) -> None:
        """
        Sets the orientation of mesh (x,y) axes.
        
        Parameters
        -----------
        orientation : Orientation
            the orientation.
        """

    def getOrientation(self) -> Orientation:
        """
        Gets the orientation of (x,y) axes.
        Returns
        --------
        output : Orientation
            the orientation.
        """

    def setNodesVisible(self, drawNodes: bool) -> None:
        """
        Sets the visibility (drawing or no drawing) of nodes.
        The default is true.
        
        Parameters
        -----------
        drawNodes : bool
            true, to draw nodes; false, otherwise.
        """

    def setTrisVisible(self, drawTris: bool) -> None:
        """
        Sets the visibility (drawing or no drawing) of tris.
        The default is true.
        
        Parameters
        -----------
        drawTris : bool
            true, to draw tris; false, otherwise.
        """

    def setSubTrisVisible(self, drawSubTris: bool) -> None:
        """
        Sets the visibility (drawing or no drawing) of subdivided tris.
        The default is false.
        
        Parameters
        -----------
        drawSubTris : bool
            true, to draw subdivided tris; false, otherwise.
        """

    def setPolysVisible(self, drawPolys: bool) -> None:
        """
        Sets the visibility (drawing or no drawing) of polygons.
        The default is false.
        
        Parameters
        -----------
        drawPolys : bool
            true, to draw polygons; false, otherwise.
        """

    def setTriBoundsVisible(self, drawTriBounds: bool) -> None:
        """
        Sets the visibility (drawing or no drawing) of tri bounds.
        The default is false.
        
        Parameters
        -----------
        drawTriBounds : bool
            true, to draw tri bounds; false, otherwise.
        """

    def setPolyBoundsVisible(self, drawPolyBounds: bool) -> None:
        """
        Sets the visibility (drawing or no drawing) of poly bounds.
        The default is false.
        
        Parameters
        -----------
        drawPolyBounds : bool
            true, to draw poly bounds; false, otherwise.
        """

    def showNodes(self) -> None:
        """
        Shows (draws) the nodes.
        """

    def hideNodes(self) -> None:
        """
        Hides (does not draw) the nodes.
        """

    def showTris(self) -> None:
        """
        Shows (draws) the tris.
        """

    def hideTris(self) -> None:
        """
        Hides (does not draw) the tris.
        """

    def showPolys(self) -> None:
        """
        Shows (draws) the polygons.
        """

    def hidePolys(self) -> None:
        """
        Hides (does not draw) the polygons.
        """

    def showTriBounds(self) -> None:
        """
        Shows (draws) the tri bounds.
        """

    def hideTriBounds(self) -> None:
        """
        Hides (does not draw) the tri bounds.
        """

    def showPolyBounds(self) -> None:
        """
        Shows (draws) the poly bounds.
        """

    def hidePolyBounds(self) -> None:
        """
        Hides (does not draw) the poly bounds.
        """

    def setLineColor(self, lineColor: Color) -> None:
        """
        Sets the color of lines used to draw edges of triangles and polygons.
        
        Parameters
        -----------
        lineColor : Color
            the line color.
        """

    def setTriColor(self, lineColor: Color) -> None:
        """
        Sets the color of lines used to draw edges of triangles.
        
        Parameters
        -----------
        lineColor : Color
            the line color.
        """

    def setTriEdgeWeights(self, triEdgeWeights: Map) -> None:
        """
        Sets the map from triangle edges to weights.
        If set, this map overrides the tri line color.
        
        Parameters
        -----------
        triEdgeWeights : Map
            a map from triangle edges to weights.
        """

    def setPolyColor(self, lineColor: Color) -> None:
        """
        Sets the color of lines used to draw edges of polygons.
        
        Parameters
        -----------
        lineColor : Color
            the line color.
        """

    def setLineWidth(self, lineWidth: int) -> None:
        """
        Sets the width of lines used to draw edges of triangles.
        
        Parameters
        -----------
        lineWidth : int
            line width in pixels (or points, as for a font).
        """

    def setMarkColor(self, markColor: Color) -> None:
        """
        Sets the color of marks used to draw nodes.
        
        Parameters
        -----------
        markColor : Color
            mark color.
        """

    def setMarkWidth(self, markWidth: int) -> None:
        """
        Sets the width of marks used to draw nodes.
        
        Parameters
        -----------
        markWidth : int
            mark width in pixels (or points, as for a font).
        """

    def setTriPainter(self, triPainter: TriPainter) -> None:
        """
        Sets the custom triangle painter.
        
        Parameters
        -----------
        triPainter : TriPainter
            the painter.
        """

    def paint(self, g2d: Graphics2D) -> None:
        """
    
        """
