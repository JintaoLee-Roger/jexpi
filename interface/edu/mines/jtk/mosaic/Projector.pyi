from typing import overload
from edu.mines.jtk.mapping import *


class Projector:
    """
    Converts (projects) world coordinates v to/from normalized coordinates u.
    The projection is a simple scale and translation, such that specified
    world coordinates (v0,v1) correspond to specified normalized coordinates
    (u0,u1).
    
    Specifically, a projector computes u = shift+scalev, where scale =
    (u1-u0)/(v1-v0), and shift = u0-scalev0. The projection exists only
    for v1 != v0. However, v0 and v1 are otherwise unconstrained. v0 may
    be greater than v1.
    
    The projection from normalized coordinates u to world coordinates v is
    simply the inverse, and this inverse exists only for u1 != u0.
    
    By definition, u0 is closest to normalized coordinate u=0, and u1 is
    closest to normalized coordinate u=1. These coordinates must satisfy
    the constraints 0.0 &lt;= u0 &lt; u1 &lt;= 1.0.
    
    Typically, the coordinates (v0,v1) represent bounds in world coordinate
    space. Then, the gaps in normalized coordinate space [0,u0) and (u1,1]
    represent margins, extra space needed for graphic rendering. The amount
    of extra space required varies, depending on the graphics. Accounting for
    this varying amount of extra space is a complex but important aspect of
    aligning the coordinate systems of two or more graphics.
    
    Alignment is accomplished by simply rendering all graphics using
    the same projector. We obtain this shared projector by merging the
    preferred projectors of each graphic. A preferred projector is one
    that a graphic might use if it were the only one being rendered.
    
    We assume that each graphic has a preferred projector that indicates
    the world coordinate span [v0,v1] and margins [0,u0) and (u1,1] that
    it would prefer if it were the only graphic rendered. We then merge
    two projectors into one so that the merged projector contains the
    union of the two world coordinate spans and has adequate margins.
    
    A projector has a sign, which is the sign of v1-v0. Note that this sign
    is never ambiguous, because v1 never equals v0. When merging a projector
    B into into a projector A, we preserve the sign of projector A.
    """

    @overload
    def __init__(self, v0: double, v1: double) -> None:
        """
        Constructs a projector with specified v values, u0=0, and u1=1.
        The projector will have zero margins.
        v0 != v1 is required.
        v0 != v1 is required.
        
        Parameters
        -----------
        v0 : double
            the v coordinate that corresponds to u coordinate 0;
        v1 : double
            the v coordinate that corresponds to u coordinate 1;
        """

    @overload
    def __init__(self, v0: double, v1: double, scale: AxisScale) -> None:
        """
        Constructs a projector with specified v values and Scale,
        u0=0, and u1=1. The projector will have zero margins.
        v0 != v1 is required.
        v0 != v1 is required.
        
        Parameters
        -----------
        v0 : double
            the v coordinate that corresponds to u coordinate 0;
        v1 : double
            the v coordinate that corresponds to u coordinate 1;
        scale : AxisScale
            the AxisScale type of this projector
        """

    @overload
    def __init__(self, v0: double, v1: double, u0: double, u1: double) -> None:
        """
        Constructs a projector with specified v and u values. The
        parameters u0 and u1 determine the margins of the projector.
        v0 != v1 is required.
        v0 != v1 is required.
        0.0 &lt;= u0 &lt; u1 is required.
        u0 &lt; u1 &lt;= 1.0 is required.
        
        Parameters
        -----------
        v0 : double
            the v coordinate that corresponds to u coordinate 0;
        v1 : double
            the v coordinate that corresponds to u coordinate 1;
        u0 : double
            the u coordinate closest to normalized coordinate 0;
        u1 : double
            the u coordinate closest to normalized coordinate 1;
        """

    @overload
    def __init__(self, v0: double, v1: double, u0: double, u1: double,
                 s: AxisScale) -> None:
        """
        Constructs a projector with specified v and u values. The
        parameters u0 and u1 determine the margins of the projector.
        The world coordinate v0 corresponds to normalized coordinate u0;
        the world coordinate v1 corresponds to normalized coordinate u1.
        v0 != v1 is required.
        v0 != v1 is required.
        0.0 &lt;= u0 &lt; u1 is required.
        u0 &lt; u1 &lt;= 1.0 is required.
        
        Parameters
        -----------
        v0 : double
            the v coordinate that corresponds to u coordinate u0;
        v1 : double
            the v coordinate that corresponds to u coordinate u1;
        u0 : double
            the u coordinate closest to normalized coordinate 0;
        u1 : double
            the u coordinate closest to normalized coordinate 1;
        s : AxisScale
            the AxisScale type of this projector
        """

    @overload
    def __init__(self, p: Projector) -> None:
        """
        Constructs a copy of the specified projector.
        
        Parameters
        -----------
        p : Projector
            the projector.
        """

    def u(self, v: double) -> double:
        """
        Returns normalized coordinate u corresponding to world coordinate v.
        
        Parameters
        -----------
        v : double
            world coordinate v.
        
        Returns
        --------
        output : double
            normalized coordinate u.
        """

    def v(self, u: double) -> double:
        """
        Returns world coordinate v corresponding to normalized coordinate u.
        
        Parameters
        -----------
        u : double
            normalized coordinate u.
        
        Returns
        --------
        output : double
            world coordinate v.
        """

    def u0(self) -> double:
        """
        Returns the u-coordinate bound closest to u=0.
        Returns
        --------
        output : double
            the u-coordinate bound.
        """

    def u1(self) -> double:
        """
        Returns the u-coordinate bound closest to u=1.
        Returns
        --------
        output : double
            the u-coordinate bound.
        """

    def v0(self) -> double:
        """
        Returns the v-coordinate bound closest to u=0.
        Returns
        --------
        output : double
            the v-coordinate bound.
        """

    def v1(self) -> double:
        """
        Returns the v-coordinate bound closest to u=1.
        Returns
        --------
        output : double
            the v-coordinate bound.
        """

    def getScale(self) -> AxisScale:
        """
        Returns the scale type
        Returns
        --------
        output : AxisScale
            the value of _scaleType
        """

    def isLinear(self) -> bool:
        """
        Check whether projector is linear
        Returns
        --------
        output : bool
            true if Projector is linear, else false
        """

    def isLog(self) -> bool:
        """
        Check whether projector is logarithmic
        Returns
        --------
        output : bool
            true if Projector is logarithmic, else false
        """

    def merge(self, p: Projector) -> None:
        """
        Merges the specified projector into this projector.
        
        Parameters
        -----------
        p : Projector
            the projector.
        """

    def getScaleRatio(self, p: Projector) -> double:
        """
        Gets the scale ratio for this projector and a specified projector.
        Recall that a projector converts world coordinates v to normalized
        coordinates u by a simple scaling and translation: u = shift+scalev.
        This method returns the scale for this projector divided by the scale
        for the specified projector.
        
        This method is typically used to account for the effects of merging
        two or more projectors. For example, after merging, parameters that
        are proportional to the sizes of margins [0,u0) or (u1,1] in the
        specified projector should be scaled by this ratio before being used
        with this projector.
        
        Parameters
        -----------
        p : Projector
            a projector.
        
        Returns
        --------
        output : double
            the scale factor.
        """

    def equals(self, obj: Object) -> bool:
        """
    
        """

    def hashCode(self) -> int:
        """
    
        """

    def toString(self) -> String:
        """
    
        """
