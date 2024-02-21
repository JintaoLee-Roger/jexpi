from typing import overload
from edu.mines.jtk.mapping import *


class Geometry:
    """
    Robust geometric predicates.
    
    These geometric predicates are notoriously susceptible to roundoff error.
    For example, the simplest and fastest test to determine whether a point
    c is left of a line defined by two points a and b may fail when all three
    points are nearly co-linear.
    
    Therefore, each predicate is implemented by two types of methods. One
    method is fast, but may yield incorrect answers. The other method is
    slower, because it (1) computes a bound on the roundoff error and
    (2) reverts to an exact algorithm if the fast method might yield the
    wrong answer.
    
    Most applications should use the slower exact methods.
    The fast methods are provided only for comparison.
    
    These predicates are adapted from those developed by Jonathan Shewchuk,
    1997, Delaunay Refinement Mesh Generation: Ph.D. dissertation, Carnegie
    Mellon University. (Currently, the methods here do not use Shewchuk's
    adaptive four-stage pipeline. Instead, only two - the fastest and the
    exact stages - are used.)
    """

    @overload
    @staticmethod
    def leftOfLine(self, xa: double, ya: double, xb: double, yb: double,
                   xc: double, yc: double) -> double:
        """
        Determines if a point c is left of the line defined by the
        points a and b. This is equivalent to determining whether the
        points a, b, and c are in counter-clockwise (CCW) order.
        negative, if right of line;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x coordinate of point a.
        ya : double
            y coordinate of point a.
        xb : double
            x coordinate of point b.
        yb : double
            y coordinate of point b.
        xc : double
            x coordinate of point c.
        yc : double
            y coordinate of point c.
        
        Returns
        --------
        output : double
            positive, if left of line;
        """

    @overload
    @staticmethod
    def leftOfLine(self, pa: Double1D, pb: Double1D, pc: Double1D) -> double:
        """
        Determines if a point c is left of the line defined by the
        points a and b. This is equivalent to determining whether the
        points a, b, and c are in counter-clockwise (CCW) order.
        negative, if right of line;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y} coordinates of point a.
        pb : Double1D
            {x,y} coordinates of point b.
        pc : Double1D
            {x,y} coordinates of point c.
        
        Returns
        --------
        output : double
            positive, if left of line;
        """

    @overload
    @staticmethod
    def leftOfLine(self, pa: Float1D, pb: Float1D, pc: Float1D) -> double:
        """
        Determines if a point c is left of the line defined by the
        points a and b. This is equivalent to determining whether the
        points a, b, and c are in counter-clockwise (CCW) order.
        negative, if right of line;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y} coordinates of point a.
        pb : Float1D
            {x,y} coordinates of point b.
        pc : Float1D
            {x,y} coordinates of point c.
        
        Returns
        --------
        output : double
            positive, if left of line;
        """

    @overload
    @staticmethod
    def leftOfLineFast(self, xa: double, ya: double, xb: double, yb: double,
                       xc: double, yc: double) -> double:
        """
        Determines if a point c is left of the line defined by the
        points a and b. This is equivalent to determining whether the
        points a, b, and c are in counter-clockwise (CCW) order.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if right of line;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x coordinate of point a.
        ya : double
            y coordinate of point a.
        xb : double
            x coordinate of point b.
        yb : double
            y coordinate of point b.
        xc : double
            x coordinate of point c.
        yc : double
            y coordinate of point c.
        
        Returns
        --------
        output : double
            positive, if left of line;
        """

    @overload
    @staticmethod
    def leftOfLineFast(self, pa: Double1D, pb: Double1D,
                       pc: Double1D) -> double:
        """
        Determines if a point c is left of the line defined by the
        points a and b. This is equivalent to determining whether the
        points a, b, and c are in counter-clockwise (CCW) order.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if right of line;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y} coordinates of point a.
        pb : Double1D
            {x,y} coordinates of point b.
        pc : Double1D
            {x,y} coordinates of point c.
        
        Returns
        --------
        output : double
            positive, if left of line;
        """

    @overload
    @staticmethod
    def leftOfLineFast(self, pa: Float1D, pb: Float1D, pc: Float1D) -> double:
        """
        Determines if a point c is left of the line defined by the
        points a and b. This is equivalent to determining whether the
        points a, b, and c are in counter-clockwise (CCW) order.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if right of line;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y} coordinates of point a.
        pb : Float1D
            {x,y} coordinates of point b.
        pc : Float1D
            {x,y} coordinates of point c.
        
        Returns
        --------
        output : double
            positive, if left of line;
        """

    @overload
    @staticmethod
    def leftOfPlane(self, xa: double, ya: double, za: double, xb: double,
                    yb: double, zb: double, xc: double, yc: double, zc: double,
                    xd: double, yd: double, zd: double) -> double:
        """
        Determines if a point d is left of the plane defined by the
        points a, b, and c. The latter are assumed to be in CCW order,
        as viewed from the right side of the plane.
        negative, if right of plane;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x coordinate of point a.
        ya : double
            y coordinate of point a.
        za : double
            z coordinate of point a.
        xb : double
            x coordinate of point b.
        yb : double
            y coordinate of point b.
        zb : double
            z coordinate of point b.
        xc : double
            x coordinate of point c.
        yc : double
            y coordinate of point c.
        zc : double
            z coordinate of point c.
        xd : double
            x coordinate of point d.
        yd : double
            y coordinate of point d.
        zd : double
            z coordinate of point d.
        
        Returns
        --------
        output : double
            positive, if left of plane;
        """

    @overload
    @staticmethod
    def leftOfPlane(self, pa: Double1D, pb: Double1D, pc: Double1D,
                    pd: Double1D) -> double:
        """
        Determines if a point d is left of the plane defined by the
        points a, b, and c. The latter are assumed to be in CCW order,
        as viewed from the right side of the plane.
        negative, if right of plane;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y,z} coordinates of point a.
        pb : Double1D
            {x,y,z} coordinates of point b.
        pc : Double1D
            {x,y,z} coordinates of point c.
        pd : Double1D
            {x,y,z} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if left of plane;
        """

    @overload
    @staticmethod
    def leftOfPlane(self, pa: Float1D, pb: Float1D, pc: Float1D,
                    pd: Float1D) -> double:
        """
        Determines if a point d is left of the plane defined by the
        points a, b, and c. The latter are assumed to be in CCW order,
        as viewed from the right side of the plane.
        negative, if right of plane;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y,z} coordinates of point a.
        pb : Float1D
            {x,y,z} coordinates of point b.
        pc : Float1D
            {x,y,z} coordinates of point c.
        pd : Float1D
            {x,y,z} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if left of plane;
        """

    @overload
    @staticmethod
    def leftOfPlaneFast(self, xa: double, ya: double, za: double, xb: double,
                        yb: double, zb: double, xc: double, yc: double,
                        zc: double, xd: double, yd: double,
                        zd: double) -> double:
        """
        Determines if a point d is left of the plane defined by the
        points a, b, and c. The latter are assumed to be in CCW order,
        as viewed from the right side of the plane.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if right of plane;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x coordinate of point a.
        ya : double
            y coordinate of point a.
        za : double
            z coordinate of point a.
        xb : double
            x coordinate of point b.
        yb : double
            y coordinate of point b.
        zb : double
            z coordinate of point b.
        xc : double
            x coordinate of point c.
        yc : double
            y coordinate of point c.
        zc : double
            z coordinate of point c.
        xd : double
            x coordinate of point d.
        yd : double
            y coordinate of point d.
        zd : double
            z coordinate of point d.
        
        Returns
        --------
        output : double
            positive, if left of plane;
        """

    @overload
    @staticmethod
    def leftOfPlaneFast(self, pa: Double1D, pb: Double1D, pc: Double1D,
                        pd: Double1D) -> double:
        """
        Determines if a point d is left of the plane defined by the
        points a, b, and c. The latter are assumed to be in CCW order,
        as viewed from the right side of the plane.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if right of plane;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y,z} coordinates of point a.
        pb : Double1D
            {x,y,z} coordinates of point b.
        pc : Double1D
            {x,y,z} coordinates of point c.
        pd : Double1D
            {x,y,z} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if left of plane;
        """

    @overload
    @staticmethod
    def leftOfPlaneFast(self, pa: Float1D, pb: Float1D, pc: Float1D,
                        pd: Float1D) -> double:
        """
        Determines if a point d is left of the plane defined by the
        points a, b, and c. The latter are assumed to be in CCW order,
        as viewed from the right side of the plane.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if right of plane;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y,z} coordinates of point a.
        pb : Float1D
            {x,y,z} coordinates of point b.
        pc : Float1D
            {x,y,z} coordinates of point c.
        pd : Float1D
            {x,y,z} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if left of plane;
        """

    @overload
    @staticmethod
    def inCircle(self, xa: double, ya: double, xb: double, yb: double,
                 xc: double, yc: double, xd: double, yd: double) -> double:
        """
        Determines if a point d is inside the circle defined by the points
        a, b, and c. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfLine} would return a positive number.
        negative, if outside the circle;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x coordinate of point a.
        ya : double
            y coordinate of point a.
        xb : double
            x coordinate of point b.
        yb : double
            y coordinate of point b.
        xc : double
            x coordinate of point c.
        yc : double
            y coordinate of point c.
        xd : double
            x coordinate of point d.
        yd : double
            y coordinate of point d.
        
        Returns
        --------
        output : double
            positive, if inside the circle;
        """

    @overload
    @staticmethod
    def inCircle(self, pa: Double1D, pb: Double1D, pc: Double1D,
                 pd: Double1D) -> double:
        """
        Determines if a point d is inside the circle defined by the points
        a, b, and c. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfLine} would return a positive number.
        negative, if outside the circle;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y} coordinates of point a.
        pb : Double1D
            {x,y} coordinates of point b.
        pc : Double1D
            {x,y} coordinates of point c.
        pd : Double1D
            {x,y} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if inside the circle;
        """

    @overload
    @staticmethod
    def inCircle(self, pa: Float1D, pb: Float1D, pc: Float1D,
                 pd: Float1D) -> double:
        """
        Determines if a point d is inside the circle defined by the points
        a, b, and c. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfLine} would return a positive number.
        negative, if outside the circle;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y} coordinates of point a.
        pb : Float1D
            {x,y} coordinates of point b.
        pc : Float1D
            {x,y} coordinates of point c.
        pd : Float1D
            {x,y} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if inside the circle;
        """

    @overload
    @staticmethod
    def inCircleFast(self, xa: double, ya: double, xb: double, yb: double,
                     xc: double, yc: double, xd: double, yd: double) -> double:
        """
        Determines if a point d is inside the circle defined by the points
        a, b, and c. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfLine} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if outside the circle;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x coordinate of point a.
        ya : double
            y coordinate of point a.
        xb : double
            x coordinate of point b.
        yb : double
            y coordinate of point b.
        xc : double
            x coordinate of point c.
        yc : double
            y coordinate of point c.
        xd : double
            x coordinate of point d.
        yd : double
            y coordinate of point d.
        
        Returns
        --------
        output : double
            positive, if inside the circle;
        """

    @overload
    @staticmethod
    def inCircleFast(self, pa: Double1D, pb: Double1D, pc: Double1D,
                     pd: Double1D) -> double:
        """
        Determines if a point d is inside the circle defined by the points
        a, b, and c. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfLine} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if outside the circle;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y} coordinates of point a.
        pb : Double1D
            {x,y} coordinates of point b.
        pc : Double1D
            {x,y} coordinates of point c.
        pd : Double1D
            {x,y} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if inside the circle;
        """

    @overload
    @staticmethod
    def inCircleFast(self, pa: Float1D, pb: Float1D, pc: Float1D,
                     pd: Float1D) -> double:
        """
        Determines if a point d is inside the circle defined by the points
        a, b, and c. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfLine} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if outside the circle;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y} coordinates of point a.
        pb : Float1D
            {x,y} coordinates of point b.
        pc : Float1D
            {x,y} coordinates of point c.
        pd : Float1D
            {x,y} coordinates of point d.
        
        Returns
        --------
        output : double
            positive, if inside the circle;
        """

    @overload
    @staticmethod
    def inSphere(self, xa: double, ya: double, za: double, xb: double,
                 yb: double, zb: double, xc: double, yc: double, zc: double,
                 xd: double, yd: double, zd: double, xe: double, ye: double,
                 ze: double) -> double:
        """
        Determines if a point e is inside the sphere defined by the points
        a, b, c, and d. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfPlane} would return a positive number.
        negative, if outside the sphere;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x coordinate of point a.
        ya : double
            y coordinate of point a.
        za : double
            z coordinate of point a.
        xb : double
            x coordinate of point b.
        yb : double
            y coordinate of point b.
        zb : double
            z coordinate of point b.
        xc : double
            x coordinate of point c.
        yc : double
            y coordinate of point c.
        zc : double
            z coordinate of point c.
        xd : double
            x coordinate of point d.
        yd : double
            y coordinate of point d.
        zd : double
            z coordinate of point d.
        xe : double
            x coordinate of point e.
        ye : double
            y coordinate of point e.
        ze : double
            z coordinate of point e.
        
        Returns
        --------
        output : double
            positive, if inside the sphere;
        """

    @overload
    @staticmethod
    def inSphere(self, pa: Double1D, pb: Double1D, pc: Double1D, pd: Double1D,
                 pe: Double1D) -> double:
        """
        Determines if a point e is inside the sphere defined by the points
        a, b, c, and d. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfPlane} would return a positive number.
        negative, if outside the sphere;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y,z} coordinates of point a.
        pb : Double1D
            {x,y,z} coordinates of point b.
        pc : Double1D
            {x,y,z} coordinates of point c.
        pd : Double1D
            {x,y,z} coordinates of point d.
        pe : Double1D
            {x,y,z} coordinates of point e.
        
        Returns
        --------
        output : double
            positive, if inside the sphere;
        """

    @overload
    @staticmethod
    def inSphere(self, pa: Float1D, pb: Float1D, pc: Float1D, pd: Float1D,
                 pe: Float1D) -> double:
        """
        Determines if a point e is inside the sphere defined by the points
        a, b, c, and d. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfPlane} would return a positive number.
        negative, if outside the sphere;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y,z} coordinates of point a.
        pb : Float1D
            {x,y,z} coordinates of point b.
        pc : Float1D
            {x,y,z} coordinates of point c.
        pd : Float1D
            {x,y,z} coordinates of point d.
        pe : Float1D
            {x,y,z} coordinates of point e.
        
        Returns
        --------
        output : double
            positive, if inside the sphere;
        """

    @overload
    @staticmethod
    def inSphereFast(self, xa: double, ya: double, za: double, xb: double,
                     yb: double, zb: double, xc: double, yc: double,
                     zc: double, xd: double, yd: double, zd: double,
                     xe: double, ye: double, ze: double) -> double:
        """
        Determines if a point e is inside the sphere defined by the points
        a, b, c, and d. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfPlane} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if outside the sphere;
        zero, otherwise.
        
        Parameters
        -----------
        xa : double
            x-coordinate of point a.
        ya : double
            y-coordinate of point a.
        za : double
            z-coordinate of point a.
        xb : double
            x-coordinate of point b.
        yb : double
            y-coordinate of point b.
        zb : double
            z-coordinate of point b.
        xc : double
            x-coordinate of point c.
        yc : double
            y-coordinate of point c.
        zc : double
            z-coordinate of point c.
        xd : double
            x-coordinate of point d.
        yd : double
            y-coordinate of point d.
        zd : double
            z-coordinate of point d.
        xe : double
            x-coordinate of point e.
        ye : double
            y-coordinate of point e.
        ze : double
            z-coordinate of point e.
        
        Returns
        --------
        output : double
            positive, if inside the sphere;
        """

    @overload
    @staticmethod
    def inSphereFast(self, pa: Double1D, pb: Double1D, pc: Double1D,
                     pd: Double1D, pe: Double1D) -> double:
        """
        Determines if a point e is inside the sphere defined by the points
        a, b, c, and d. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfPlane} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if outside the sphere;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Double1D
            {x,y,z} coordinates of point a.
        pb : Double1D
            {x,y,z} coordinates of point b.
        pc : Double1D
            {x,y,z} coordinates of point c.
        pd : Double1D
            {x,y,z} coordinates of point d.
        pe : Double1D
            {x,y,z} coordinates of point e.
        
        Returns
        --------
        output : double
            positive, if inside the sphere;
        """

    @overload
    @staticmethod
    def inSphereFast(self, pa: Float1D, pb: Float1D, pc: Float1D, pd: Float1D,
                     pe: Float1D) -> double:
        """
        Determines if a point e is inside the sphere defined by the points
        a, b, c, and d. The latter are assumed to be in CCW order, such that
        the method {@link #leftOfPlane} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        negative, if outside the sphere;
        zero, otherwise.
        
        Parameters
        -----------
        pa : Float1D
            {x,y,z} coordinates of point a.
        pb : Float1D
            {x,y,z} coordinates of point b.
        pc : Float1D
            {x,y,z} coordinates of point c.
        pd : Float1D
            {x,y,z} coordinates of point d.
        pe : Float1D
            {x,y,z} coordinates of point e.
        
        Returns
        --------
        output : double
            positive, if inside the sphere;
        """

    @overload
    @staticmethod
    def inOrthoSphere(self, xa: double, ya: double, za: double, wa: double,
                      xb: double, yb: double, zb: double, wb: double,
                      xc: double, yc: double, zc: double, wc: double,
                      xd: double, yd: double, zd: double, wd: double,
                      xe: double, ye: double, ze: double,
                      we: double) -> double:
        """
        Determines whether or not a weighted point e is inside the
        ortho-sphere defined by the weighted points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        The weights wa, wb, wc, wd equal the squared radii of spheres
        associated with the corresponding points a, b, c, and d. The
        ortho-sphere is orthogonal to each of these four spheres.
        
        If all four weights (and radii) equal zero, then the ortho-sphere
        is the circumsphere. In this case, the method {@link #inSphere}
        is more efficient.
        
        Parameters
        -----------
        xa : double
            x-coordinate of point a.
        ya : double
            y-coordinate of point a.
        za : double
            z-coordinate of point a.
        wa : double
            w-coordinate of point a.
        xb : double
            x-coordinate of point b.
        yb : double
            y-coordinate of point b.
        zb : double
            z-coordinate of point b.
        wb : double
            w-coordinate of point b.
        xc : double
            x-coordinate of point c.
        yc : double
            y-coordinate of point c.
        zc : double
            z-coordinate of point c.
        wc : double
            w-coordinate of point c.
        xd : double
            x-coordinate of point d.
        yd : double
            y-coordinate of point d.
        zd : double
            z-coordinate of point d.
        wd : double
            w-coordinate of point d.
        xe : double
            x-coordinate of point e.
        ye : double
            y-coordinate of point e.
        ze : double
            z-coordinate of point e.
        we : double
            w-coordinate of point e.
        
        Returns
        --------
        output : double
            a positive number if inside ortho-sphere; negative, otherwise.
        """

    @overload
    @staticmethod
    def inOrthoSphere(self, pa: Double1D, pb: Double1D, pc: Double1D,
                      pd: Double1D, pe: Double1D) -> double:
        """
        Determines whether or not a weighted point e is inside the
        ortho-sphere defined by the weighted points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        Parameters
        -----------
        pa : Double1D
            {x,y,z,w} coordinates of point a.
        pb : Double1D
            {x,y,z,w} coordinates of point b.
        pc : Double1D
            {x,y,z,w} coordinates of point c.
        pd : Double1D
            {x,y,z,w} coordinates of point d.
        pe : Double1D
            {x,y,z,w} coordinates of point d.
        
        Returns
        --------
        output : double
            a positive number if within ortho-sphere; negative, otherwise.
        """

    @overload
    @staticmethod
    def inOrthoSphere(self, pa: Float1D, pb: Float1D, pc: Float1D, pd: Float1D,
                      pe: Float1D) -> double:
        """
        Determines whether or not a weighted point e is inside the
        ortho-sphere defined by the weighted points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        Parameters
        -----------
        pa : Float1D
            {x,y,z,w} coordinates of point a.
        pb : Float1D
            {x,y,z,w} coordinates of point b.
        pc : Float1D
            {x,y,z,w} coordinates of point c.
        pd : Float1D
            {x,y,z,w} coordinates of point d.
        pe : Float1D
            {x,y,z,w} coordinates of point d.
        
        Returns
        --------
        output : double
            a positive number if within ortho-sphere; negative, otherwise.
        """

    @overload
    @staticmethod
    def inOrthoSphereFast(self, xa: double, ya: double, za: double, wa: double,
                          xb: double, yb: double, zb: double, wb: double,
                          xc: double, yc: double, zc: double, wc: double,
                          xd: double, yd: double, zd: double, wd: double,
                          xe: double, ye: double, ze: double,
                          we: double) -> double:
        """
        Determines whether or not a weighted point e is inside the
        ortho-sphere defined by the weighted points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        
        Parameters
        -----------
        xa : double
            x-coordinate of point a.
        ya : double
            y-coordinate of point a.
        za : double
            z-coordinate of point a.
        wa : double
            w-coordinate of point a.
        xb : double
            x-coordinate of point b.
        yb : double
            y-coordinate of point b.
        zb : double
            z-coordinate of point b.
        wb : double
            w-coordinate of point b.
        xc : double
            x-coordinate of point c.
        yc : double
            y-coordinate of point c.
        zc : double
            z-coordinate of point c.
        wc : double
            w-coordinate of point c.
        xd : double
            x-coordinate of point d.
        yd : double
            y-coordinate of point d.
        zd : double
            z-coordinate of point d.
        wd : double
            w-coordinate of point d.
        xe : double
            x-coordinate of point e.
        ye : double
            y-coordinate of point e.
        ze : double
            z-coordinate of point e.
        we : double
            w-coordinate of point e.
        
        Returns
        --------
        output : double
            a positive number if within ortho-sphere; negative, otherwise.
        """

    @overload
    @staticmethod
    def inOrthoSphereFast(self, pa: Double1D, pb: Double1D, pc: Double1D,
                          pd: Double1D, pe: Double1D) -> double:
        """
        Determines whether or not a weighted point e is inside the
        ortho-sphere defined by the weighted points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        
        Parameters
        -----------
        pa : Double1D
            {x,y,z,w} coordinates of point a.
        pb : Double1D
            {x,y,z,w} coordinates of point b.
        pc : Double1D
            {x,y,z,w} coordinates of point c.
        pd : Double1D
            {x,y,z,w} coordinates of point d.
        pe : Double1D
            {x,y,z,w} coordinates of point e.
        
        Returns
        --------
        output : double
            positive, if inside the ortho-sphere; negative, otherwise.
        """

    @overload
    @staticmethod
    def inOrthoSphereFast(self, pa: Float1D, pb: Float1D, pc: Float1D,
                          pd: Float1D, pe: Float1D) -> double:
        """
        Determines whether or not a weighted point e is inside the
        ortho-sphere defined by the weighted points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        <em>Note: this fast method may return an incorrect result.</em>
        
        Parameters
        -----------
        pa : Float1D
            {x,y,z,w} coordinates of point a.
        pb : Float1D
            {x,y,z,w} coordinates of point b.
        pc : Float1D
            {x,y,z,w} coordinates of point c.
        pd : Float1D
            {x,y,z,w} coordinates of point d.
        pe : Float1D
            {x,y,z,w} coordinates of point e.
        
        Returns
        --------
        output : double
            positive, if inside the ortho-sphere; negative, otherwise.
        """

    @overload
    @staticmethod
    def centerCircle(self, xa: float, ya: float, xb: float, yb: float,
                     xc: float, yc: float, po: Float1D) -> None:
        """
        Computes the center of the circle defined by the points a, b, and c.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfLine} would return a positive number.
        
        Parameters
        -----------
        xa : float
            x-coordinate of point a.
        ya : float
            y-coordinate of point a.
        xb : float
            x-coordinate of point b.
        yb : float
            y-coordinate of point b.
        xc : float
            x-coordinate of point c.
        yc : float
            y-coordinate of point c.
        po : Float1D
            array containing (x,y) coordinates of center.
        """

    @overload
    @staticmethod
    def centerCircle(self, pa: Float1D, pb: Float1D, pc: Float1D,
                     po: Float1D) -> None:
        """
        Computes the center of the circle defined by the points a, b, and c.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfLine} would return a positive number.
        
        Parameters
        -----------
        pa : Float1D
            {x,y} coordinates of point a.
        pb : Float1D
            {x,y} coordinates of point b.
        pc : Float1D
            {x,y} coordinates of point c.
        po : Float1D
            array containing (x,y) coordinates of center.
        """

    @overload
    @staticmethod
    def centerCircle(self, xa: double, ya: double, xb: double, yb: double,
                     xc: double, yc: double, po: Double1D) -> None:
        """
        Computes the center of the circle defined by the points a, b, and c.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfLine} would return a positive number.
        
        Parameters
        -----------
        xa : double
            x-coordinate of point a.
        ya : double
            y-coordinate of point a.
        xb : double
            x-coordinate of point b.
        yb : double
            y-coordinate of point b.
        xc : double
            x-coordinate of point c.
        yc : double
            y-coordinate of point c.
        po : Double1D
            array containing (x,y) coordinates of center.
        """

    @overload
    @staticmethod
    def centerCircle(self, pa: Double1D, pb: Double1D, pc: Double1D,
                     po: Double1D) -> None:
        """
        Computes the center of the circle defined by the points a, b, and c.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfLine} would return a positive number.
        
        Parameters
        -----------
        pa : Double1D
            {x,y} coordinates of point a.
        pb : Double1D
            {x,y} coordinates of point b.
        pc : Double1D
            {x,y} coordinates of point c.
        po : Double1D
            array containing (x,y) coordinates of center.
        """

    @overload
    @staticmethod
    def centerSphere(self, xa: float, ya: float, za: float, xb: float,
                     yb: float, zb: float, xc: float, yc: float, zc: float,
                     xd: float, yd: float, zd: float, po: Float1D) -> None:
        """
        Computes the center of the sphere defined by the points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        Parameters
        -----------
        xa : float
            x-coordinate of point a.
        ya : float
            y-coordinate of point a.
        za : float
            z-coordinate of point a.
        xb : float
            x-coordinate of point b.
        yb : float
            y-coordinate of point b.
        zb : float
            z-coordinate of point b.
        xc : float
            x-coordinate of point c.
        yc : float
            y-coordinate of point c.
        zc : float
            z-coordinate of point c.
        xd : float
            x-coordinate of point d.
        yd : float
            y-coordinate of point d.
        zd : float
            z-coordinate of point d.
        po : Float1D
            array containing (x,y,z) coordinates of center.
        """

    @overload
    @staticmethod
    def centerSphere(self, pa: Float1D, pb: Float1D, pc: Float1D, pd: Float1D,
                     po: Float1D) -> None:
        """
        Computes the center of the sphere defined by the points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        Parameters
        -----------
        pa : Float1D
            {x,y,z} coordinates of point a.
        pb : Float1D
            {x,y,z} coordinates of point b.
        pc : Float1D
            {x,y,z} coordinates of point c.
        pd : Float1D
            {x,y,z} coordinates of point d.
        po : Float1D
            array containing (x,y,z) coordinates of center.
        """

    @overload
    @staticmethod
    def centerSphere(self, xa: double, ya: double, za: double, xb: double,
                     yb: double, zb: double, xc: double, yc: double,
                     zc: double, xd: double, yd: double, zd: double,
                     po: Double1D) -> None:
        """
        Computes the center of the sphere defined by the points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        Parameters
        -----------
        xa : double
            x-coordinate of point a.
        ya : double
            y-coordinate of point a.
        za : double
            z-coordinate of point a.
        xb : double
            x-coordinate of point b.
        yb : double
            y-coordinate of point b.
        zb : double
            z-coordinate of point b.
        xc : double
            x-coordinate of point c.
        yc : double
            y-coordinate of point c.
        zc : double
            z-coordinate of point c.
        xd : double
            x-coordinate of point d.
        yd : double
            y-coordinate of point d.
        zd : double
            z-coordinate of point d.
        po : Double1D
            array containing (x,y,z) coordinates of center.
        """

    @overload
    @staticmethod
    def centerSphere(self, pa: Double1D, pb: Double1D, pc: Double1D,
                     pd: Double1D, po: Double1D) -> None:
        """
        Computes the center of the sphere defined by the points a, b, c, and d.
        The latter are assumed to be in CCW order, such that the method
        {@link #leftOfPlane} would return a positive number.
        
        Parameters
        -----------
        pa : Double1D
            {x,y,z} coordinates of point a.
        pb : Double1D
            {x,y,z} coordinates of point b.
        pc : Double1D
            {x,y,z} coordinates of point c.
        pd : Double1D
            {x,y,z} coordinates of point d.
        po : Double1D
            array containing (x,y,z) coordinates of center.
        """

    @staticmethod
    def centerCircle3D(self, xa: double, ya: double, za: double, xb: double,
                       yb: double, zb: double, xc: double, yc: double,
                       zc: double, po: Double1D) -> None:
        """
        Computes the center of the circle defined by the 3-D points a, b, and c.
        Because the points have 3-D coordinates, they may specified in any order.
        
        Parameters
        -----------
        xa : double
            x-coordinate of point a.
        ya : double
            y-coordinate of point a.
        za : double
            z-coordinate of point a.
        xb : double
            x-coordinate of point b.
        yb : double
            y-coordinate of point b.
        zb : double
            z-coordinate of point b.
        xc : double
            x-coordinate of point c.
        yc : double
            y-coordinate of point c.
        zc : double
            z-coordinate of point c.
        po : Double1D
            array containing (x,y,z) coordinates of center.
        """
