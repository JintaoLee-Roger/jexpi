from typing import overload
from edu.mines.jtk.mapping import *


class OrbitView:
    """
    A view of a world, as if in orbit around that world.
    By default, the view camera is aimed towards the world, from a point
    outside the world's sphere. The camera's up axis is always aligned
    with lines of constant longitude. An orbit view is designed to draw
    on a single view canvas.
    
    All views maintain a world-to-view transform. In an orbit view, that
    world-to-view transform is comprised of a world-to-unit-sphere
    transform and a unit-sphere-to-view transform.
    
    The world-to-unit-sphere transform centers and normalizes the world.
    A world drawn by an orbit view has a world sphere that, by default, is
    the bounding sphere of the world when first viewed. The world-to-unit-
    sphere transform first translates the world sphere's center to the origin,
    and then scales the world sphere to have unit radius. The purpose of this
    first transform is to make other orbit view parameters independent
    of world coordinates. To modify the world-to-unit-sphere transform,
    set the world sphere.
    
    The second unit-sphere-to-view transform applies a translate, scale,
    and rotate to the unit sphere, and then applies a final translate
    down the z-axis to push the transformed sphere into the view frustum.
    The orbit view applies the first translate, scale, and rotate in that
    order, so that the scale and rotate occurs about the center of
    the view.
    
    The rotate part of the unit-sphere-to-view transform is comprised of
    two rotations, because an orbit view camera has both azimuth and
    elevation angles. Imagine a line from the center of the unit sphere
    to the camera. The point where that line intersects the sphere has a
    latitude and longitude. The azimuth angle is the longitude, positive
    for degrees East, negative for degrees West. The elevation angle is
    the latitude, positive for degrees North, negative for degrees South.
    
    An orbit view supports both perspective and orthographic projections.
    For perspective projections, the field of view is computed by assuming
    that the distance from the eye to the default screen is approximately
    equal to the size of that screen.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs an orbit view of no world.
        """

    @overload
    def __init__(self, world: World) -> None:
        """
        Constructs an orbit view of the specified world.
        
        Parameters
        -----------
        world : World
            the world.
        """

    def reset(self) -> None:
        """
        Resets this view to its state when constructed.
        """

    def setWorldSphere(self, worldSphere: BoundingSphere) -> None:
        """
        Sets the world sphere used to parameterize this view.
        If null (the default), this view uses the bounding sphere of the
        the world when first viewed.
        
        Parameters
        -----------
        worldSphere : BoundingSphere
            the world sphere; null, if none.
        """

    def getWorldSphere(self) -> BoundingSphere:
        """
        Gets the world sphere used to parameterize this view.
        Returns
        --------
        output : BoundingSphere
            the world sphere; null, if none.
        """

    def setProjection(self, projection: Projection) -> None:
        """
        Sets the projection for this view.
        
        Parameters
        -----------
        projection : Projection
            the projection.
        """

    def getProjection(self) -> Projection:
        """
        Gets the projection for this view.
        Returns
        --------
        output : Projection
            the projection.
        """

    def setAzimuth(self, azimuth: double) -> None:
        """
        Sets the azimuth for this view.
        
        Parameters
        -----------
        azimuth : double
            the azimuth.
        """

    def getAzimuth(self) -> double:
        """
        Gets the azimuth for this view.
        Returns
        --------
        output : double
            the azimuth.
        """

    def setElevation(self, elevation: double) -> None:
        """
        Sets the elevation for this view.
        
        Parameters
        -----------
        elevation : double
            the elevation.
        """

    def getElevation(self) -> double:
        """
        Gets the elevation for this view.
        Returns
        --------
        output : double
            the elevation.
        """

    def setAzimuthAndElevation(self, azimuth: double,
                               elevation: double) -> None:
        """
        Sets the azimuth and elevation for this view.
        
        Parameters
        -----------
        azimuth : double
            the azimuth.
        elevation : double
            the elevation.
        """

    def setScale(self, scale: double) -> None:
        """
        Sets the scale factor for this view.
        
        Parameters
        -----------
        scale : double
            the scale factor.
        """

    def getScale(self) -> double:
        """
        Gets the scale factor for this view.
        Returns
        --------
        output : double
            the scale factor.
        """

    def setTranslate(self, translate: Vector3) -> None:
        """
        Sets the translate vector for this view.
        
        Parameters
        -----------
        translate : Vector3
            the translate vector.
        """

    def getTranslate(self) -> Vector3:
        """
        Gets the translate vector for this view.
        Returns
        --------
        output : Vector3
            the translate vector.
        """

    def getWorldToUnitSphere(self) -> Matrix44:
        """
        Gets the world-to-unit-sphere transform for this view.
        Returns
        --------
        output : Matrix44
            the world-to-unit-sphere transform.
        """

    def getUnitSphereToView(self) -> Matrix44:
        """
        Gets the unit-sphere-to-view transform for this view.
        Returns
        --------
        output : Matrix44
            the unit-sphere-to-view transform.
        """

    def setEyeToScreenDistance(self, esd: double) -> None:
        """
        Sets the eye-to-screen distance, in pixels. If zero, the default,
        this view will use the screen size (length of the screen diagonal).
        This parameter is used only for perspective views.
        
        Parameters
        -----------
        esd : double
            the eye-to-screen distance, in pixels.
        """

    def setOrbitViewLighting(self,
                             orbitViewLighting: OrbitViewLighting) -> None:
        """
        Sets the scene lighting.
        
        Parameters
        -----------
        orbitViewLighting : OrbitViewLighting
            the scene lighting.
        """

    def getOrbitViewLighting(self) -> OrbitViewLighting:
        """
        Gets the scene lighting.
        Returns
        --------
        output : OrbitViewLighting
            the scene lighting.
        """
