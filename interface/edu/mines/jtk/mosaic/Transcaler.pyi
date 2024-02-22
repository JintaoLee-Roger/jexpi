from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.mosaic import *
from edu.mines.jtk.mosaic import Projector


class Transcaler:
    """
    Translates and scales (maps) user coordinates to/from device coordinates.
    The mapping is specified by two rectangles, one in user coordinates and
    the other in device coordinates.
    
    Device coordinates are ints, and the device coordinate rectangle
    typically corresponds to device bounds. User coordinates are doubles.
    
    In conversion from user to device coordinates, the latter are clipped
    to lie in the range [-32768,32767], which is the range of a 16-bit
    short integer. Although device coordinates are represented by ints,
    they are often limited by an underlying graphics systems to the 16-bit
    range of shorts.
    
    Conversion from/to user coordinates to/from device coordinates behaves
    robustly in the cases where the mapping is degenerate. For example, if
    the device coordinate rectangle has width one, then conversion from
    any device x-coordinate to user x-coordinate yields the average of the
    user x-coordinate bounds. Likewise, if the user coordinate rectangle
    has zero width, then conversion from any user x-coordinate to device
    x-coordinate yields the average of the device x-coordinate bounds.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a transcaler with identity coordinate mapping.
        In this mapping, device coordinates equal user coordinates,
        rounded to the nearest integer.
        """

    @overload
    def __init__(self, width: int, height: int) -> None:
        """
        Constructs a transcaler with specified device width and height.
        Maps user coordinates (0.0,0.0) to device coordinates (0,0) and
        user coordinates (1.0,1.0) to device coordinates (width-1,height-1).
        
        Parameters
        -----------
        width : int
            the width, in device coordinates.
        height : int
            the height, in device coordinates.
        """

    @overload
    def __init__(self, x1u: double, y1u: double, x2u: double, y2u: double,
                 x1d: int, y1d: int, x2d: int, y2d: int) -> None:
        """
        Constructs a transcaler with specified coordinate mapping.
        
        Parameters
        -----------
        x1u : double
            the user x-coordinate corresponding to x1d.
        y1u : double
            the user y-coordinate corresponding to y1d.
        x2u : double
            the user x-coordinate corresponding to x2d.
        y2u : double
            the user y-coordinate corresponding to y2d.
        x1d : int
            the device x-coordinate corresponding to x1u.
        y1d : int
            the device y-coordinate corresponding to y1u.
        x2d : int
            the device x-coordinate corresponding to x2u.
        y2d : int
            the device y-coordinate corresponding to y2u.
        """

    @overload
    def setMapping(self, x1u: double, y1u: double, x2u: double, y2u: double,
                   x1d: int, y1d: int, x2d: int, y2d: int) -> None:
        """
        Sets the coordinate mapping for this transcaler.
        
        Parameters
        -----------
        x1u : double
            the user x-coordinate corresponding to x1d.
        y1u : double
            the user y-coordinate corresponding to y1d.
        x2u : double
            the user x-coordinate corresponding to x2d.
        y2u : double
            the user y-coordinate corresponding to y2d.
        x1d : int
            the device x-coordinate corresponding to x1u.
        y1d : int
            the device y-coordinate corresponding to y1u.
        x2d : int
            the device x-coordinate corresponding to x2u.
        y2d : int
            the device y-coordinate corresponding to y2u.
        """

    @overload
    def setMapping(self, x1u: double, y1u: double, x2u: double,
                   y2u: double) -> None:
        """
        Sets the user-coordinate part of the mapping for this transcaler.
        
        Parameters
        -----------
        x1u : double
            the user x-coordinate corresponding to the current x1d.
        y1u : double
            the user y-coordinate corresponding to the current y1d.
        x2u : double
            the user x-coordinate corresponding to the current x2d.
        y2u : double
            the user y-coordinate corresponding to the current y2d.
        """

    @overload
    def setMapping(self, x1d: int, y1d: int, x2d: int, y2d: int) -> None:
        """
        Sets the device-coordinate part of the mapping for this transcaler.
        
        Parameters
        -----------
        x1d : int
            the device x-coordinate corresponding to the current x1u.
        y1d : int
            the device y-coordinate corresponding to the current y1u.
        x2d : int
            the device x-coordinate corresponding to the current x2u.
        y2d : int
            the device y-coordinate corresponding to the current y2u.
        """

    @overload
    def setMapping(self, width: int, height: int) -> None:
        """
        Sets the device-coordinate width and height. Maps the current user
        coordinates (x1u,y1u) to device coordinates (0,0) and user coordinates
        (x2u,y2u) to device coordinates (width-1,height-1).
        
        Parameters
        -----------
        width : int
            device-coordinate width.
        height : int
            device-coordinate height.
        """

    def combineWith(self, xp: Projector, yp: Projector) -> Transcaler:
        """
        Returns a new transcaler that combines this transcaler with projectors.
        The returned transcaler includes the transforms of the projectors.
        Does not change this transcaler.
        
        Parameters
        -----------
        xp : Projector
            the projector for x coordinates.
        yp : Projector
            the projector for y coordinates.
        
        Returns
        --------
        output : Transcaler
            the new transcaler.
        """

    @overload
    def x(self, xu: double) -> int:
        """
        Converts the specified user x-coordinate to device x-coordinate.
        
        Parameters
        -----------
        xu : double
            the user x-coordinate.
        
        Returns
        --------
        output : int
            the device x-coordinate.
        """

    @overload
    def y(self, yu: double) -> int:
        """
        Converts the specified user y-coordinate to device y-coordinate.
        
        Parameters
        -----------
        yu : double
            the user y-coordinate.
        
        Returns
        --------
        output : int
            the device y-coordinate.
        """

    @overload
    def width(self, wu: double) -> int:
        """
        Converts the specified user-coordinate width to device-coordinate width.
        
        Parameters
        -----------
        wu : double
            the user-coordinate width.
        
        Returns
        --------
        output : int
            the device-coordinate width.
        """

    @overload
    def height(self, hu: double) -> int:
        """
        Converts the specified user-coordinate height to device-coordinate height.
        
        Parameters
        -----------
        hu : double
            the user-coordinate height.
        
        Returns
        --------
        output : int
            the device-coordinate height.
        """

    @overload
    def x(self, xd: int) -> double:
        """
        Converts the specified device x-coordinate to user x-coordinate.
        
        Parameters
        -----------
        xd : int
            the device x-coordinate.
        
        Returns
        --------
        output : double
            the user x-coordinate.
        """

    @overload
    def y(self, yd: int) -> double:
        """
        Converts the specified device y-coordinate to user y-coordinate.
        
        Parameters
        -----------
        yd : int
            the device y-coordinate.
        
        Returns
        --------
        output : double
            the user y-coordinate.
        """

    @overload
    def width(self, wd: int) -> double:
        """
        Converts the specified device-coordinate width to user-coordinate width.
        
        Parameters
        -----------
        wd : int
            the device-coordinate width.
        
        Returns
        --------
        output : double
            the user-coordinate width.
        """

    @overload
    def height(self, hd: int) -> double:
        """
        Converts the specified device-coordinate height to user-coordinate height.
        
        Parameters
        -----------
        hd : int
            the device-coordinate height.
        
        Returns
        --------
        output : double
            the user-coordinate height.
        """
