from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import EigenTensors2, EigenTensors3


class LocalOrientFilter:
    """
    Local estimates of orientations of features in images.
    Methods of this class can compute for each image sample numerous
    parameters related to orientation. All orientation information
    is derived from eigenvectors and eigenvalues of the structure tensor
    (also called the "gradient-squared tensor"). This tensor is equivalent
    to a matrix of 2nd partial derivatives of an autocorrelation evaluated
    at zero lag. In other words, orientation is here determined by the
    (2-D) ellipse or (3-D) ellipsoid that best fits the peak of the
    autocorrelation of image samples in a local window.
    
    The coordinate system for a 2-D image has two orthogonal axes 1 and 2,
    which correspond to the 1st and 2nd indices of the array containing
    image samples. For 2-D images, the eigenvectors are the unit vectors
    u = (u1,u2) and v = (v1,v2). The 1st eigenvector u is perpendicular
    to the best fitting line, and the 1st component u1 of u is always
    non-negative. The 2nd eigenvector v is perpendicular to u such that
    the cross product u1v2-u2v1 = 1; that is, v1 = -u2 and v2 = u1.
    The angle theta = asin(u2) is the angle measured counter-clockwise
    between the 1st eigenvector u and axis 1; -pi/2 &lt;= theta &lt;= pi/2.
    
    The coordinate system for a 3-D image has three orthogonal axes 1, 2
    and 3, which correspond to the 1st, 2nd and 3rd indices of the array
    containing image samples. For 3-D images, the eigenvectors are unit
    vectors u = (u1,u2,u3), v = (v1,v2,v3), and w = (w1,w2,w3). The 1st
    eigenvector u is orthogonal to the best fitting plane, and the 1st
    component u1 of u is always non-negative. The 2nd eigenvector v is
    orthogonal to the best fitting line within the best fitting plane.
    The 3rd eigenvector w is orthogonal to both u and v and is aligned
    with the direction in which the images changes least. The dip angle
    theta = acos(u1) is the angle between the 1st eigenvector u and axis 1;
    0 &lt;= theta &lt;= pi/2. The azimuthal angle phi = atan2(u3,u2)
    is well-defined for only non-zero theta; -pi &lt;= phi &lt;= pi.
    
    The local linearity or planarity of features is determined by the
    eigenvalues. For 2-D images with eigenvalues eu and ev (corresponding
    to the eigenvectors u and v), linearity is (eu-ev)/eu. For 3-D
    images with eigenvalues eu, ev, and ew, planarity is (eu-ev)/eu
    and linearity is (ev-ew)/eu. Both linearity and planarity are
    in the range [0,1].
    """

    @overload
    def __init__(self, sigma: double) -> None:
        """
        Constructs a filter with an isotropic Gaussian window.
        
        Parameters
        -----------
        sigma : double
            half-width of window; same for all dimensions.
        """

    @overload
    def __init__(self, sigma1: double, sigma2: double) -> None:
        """
        Constructs a filter with a possibly anisotropic Gaussian window.
        
        Parameters
        -----------
        sigma1 : double
            half-width of window in 1st dimension.
        sigma2 : double
            half-width of window in 2nd and higher dimensions.
        """

    @overload
    def __init__(self, sigma1: double, sigma2: double, sigma3: double) -> None:
        """
        Constructs a filter with a possibly anisotropic Gaussian window.
        
        Parameters
        -----------
        sigma1 : double
            half-width of window in 1st dimension.
        sigma2 : double
            half-width of window in 2nd dimension.
        sigma3 : double
            half-width of window in 3rd and higher dimensions.
        """

    @overload
    def setGradientSmoothing(self, sigma: double) -> None:
        """
        Sets half-width of Gaussian derivative filter used to compute gradients.
        Typically, this half-width should not exceed one-fourth that of the
        the corresponding Gaussian window used to compute local averages of
        gradient products.
        The default half-width for Gaussian derivatives is 1.0.
        
        Parameters
        -----------
        sigma : double
            half-width of derivatives; same for all dimensions.
        """

    @overload
    def setGradientSmoothing(self, sigma1: double, sigma2: double) -> None:
        """
        Sets half-widths of Gaussian derivative filters used to compute gradients.
        Typically, these half-widths should not exceed one-fourth those of the
        the corresponding Gaussian windows used to compute local averages of
        gradient-squared tensors.
        The default half-widths for Gaussian derivatives is 1.0.
        
        Parameters
        -----------
        sigma1 : double
            half-width of derivative in 1st dimension.
        sigma2 : double
            half-width of derivatives in 2nd and higher dimensions.
        """

    @overload
    def setGradientSmoothing(self, sigma1: double, sigma2: double,
                             sigma3: double) -> None:
        """
        Sets half-widths of Gaussian derivative filters used to compute gradients.
        Typically, these half-widths should not exceed one-fourth those of the
        the corresponding Gaussian windows used to compute local averages of
        gradient-squared tensors.
        The default half-widths for Gaussian derivatives is 1.0.
        
        Parameters
        -----------
        sigma1 : double
            half-width of derivative in 1st dimension.
        sigma2 : double
            half-width of derivative in 2nd dimension.
        sigma3 : double
            half-width of derivatives in 3rd and higher dimensions.
        """

    def applyForTheta(self, x: Float2D, theta: Float2D) -> None:
        """
        Applies this filter to estimate orientation angles.
        
        Parameters
        -----------
        x : Float2D
            input array for 2-D image.
        theta : Float2D
            orientation angle; -pi &lt;= theta &lt;= pi
        """

    @overload
    def applyForNormal(self, x: Float2D, u1: Float2D, u2: Float2D) -> None:
        """
        Applies this filter to estimate normal vectors (1st eigenvectors).
        
        Parameters
        -----------
        x : Float2D
            input array for 2-D image.
        u1 : Float2D
            1st component of normal vector.
        u2 : Float2D
            2nd component of normal vector.
        """

    def applyForNormalLinear(self, x: Float2D, u1: Float2D, u2: Float2D,
                             el: Float2D) -> None:
        """
        Applies this filter to estimate normal vectors and linearities.
        
        Parameters
        -----------
        x : Float2D
            input array for 2-D image.
        u1 : Float2D
            1st component of normal vector.
        u2 : Float2D
            2nd component of normal vector.
        el : Float2D
            linearity in range [0,1].
        """

    @overload
    def applyForTensors(self, x: Float2D) -> EigenTensors2:
        """
        Applies this filter to estimate 2-D structure tensors.
        
        Parameters
        -----------
        x : Float2D
            input array for 2-D image.
        
        Returns
        --------
        output : EigenTensors2
            structure tensors.
        """

    @overload
    def apply(self, x: Float2D, theta: Float2D, u1: Float2D, u2: Float2D,
              v1: Float2D, v2: Float2D, eu: Float2D, ev: Float2D,
              el: Float2D) -> None:
        """
        Applies this filter for the specified image and outputs. All
        outputs are optional and are computed for only non-null arrays.
        
        Parameters
        -----------
        x : Float2D
            input array for 2-D image
        theta : Float2D
            orientation angle = asin(u2); -pi &lt;= theta &lt;= pi
        u1 : Float2D
            1st component of 1st eigenvector.
        u2 : Float2D
            2nd component of 1st eigenvector.
        v1 : Float2D
            1st component of 2nd eigenvector.
        v2 : Float2D
            2nd component of 2nd eigenvector.
        eu : Float2D
            largest eigenvalue corresponding to the eigenvector u.
        ev : Float2D
            smallest eigenvalue corresponding to the eigenvector v.
        el : Float2D
            (eu-ev)/eu, a measure of linearity.
        """

    def applyForThetaPhi(self, x: Float3D, theta: Float3D,
                         phi: Float3D) -> None:
        """
        Applies this filter to estimate orientation angles.
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        theta : Float3D
            orientation dip angle; 0 &lt;= theta &lt;= pi/2.
        phi : Float3D
            orientation azimuthal angle; -pi &lt;= phi &lt;= pi.
        """

    @overload
    def applyForNormal(self, x: Float3D, u1: Float3D, u2: Float3D,
                       u3: Float3D) -> None:
        """
        Applies this filter to estimate normal vectors (1st eigenvectors).
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        u1 : Float3D
            1st component of normal vector.
        u2 : Float3D
            2nd component of normal vector.
        u3 : Float3D
            3rd component of normal vector.
        """

    def applyForNormalPlanar(self, x: Float3D, u1: Float3D, u2: Float3D,
                             u3: Float3D, ep: Float3D) -> None:
        """
        Applies this filter to estimate normal vectors and planarities.
        Normal vectors are 1st eigenvectors corresponding to largest eigenvalues.
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        u1 : Float3D
            1st component of normal vector.
        u2 : Float3D
            2nd component of normal vector.
        u3 : Float3D
            3rd component of normal vector.
        ep : Float3D
            planarity in range [0,1].
        """

    def applyForInline(self, x: Float3D, w1: Float3D, w2: Float3D,
                       w3: Float3D) -> None:
        """
        Applies this filter to estimate inline vectors (3rd eigenvectors).
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        w1 : Float3D
            1st component of inline vector.
        w2 : Float3D
            2nd component of inline vector.
        w3 : Float3D
            3rd component of inline vector.
        """

    def applyForInlineLinear(self, x: Float3D, w1: Float3D, w2: Float3D,
                             w3: Float3D, el: Float3D) -> None:
        """
        Applies this filter to estimate inline vectors and linearities.
        Inline vectors are 3rd eigenvectors corresponding to smallest eigenvalues.
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        w1 : Float3D
            1st component of inline vector.
        w2 : Float3D
            2nd component of inline vector.
        w3 : Float3D
            3rd component of inline vector.
        el : Float3D
            linearity in range [0,1].
        """

    @overload
    def applyForTensors(self, x: Float3D) -> EigenTensors3:
        """
        Applies this filter to estimate compressed 3-D structure tensors.
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        
        Returns
        --------
        output : EigenTensors3
            structure tensors.
        """

    @overload
    def applyForTensors(self, x: Float3D, compressed: bool) -> EigenTensors3:
        """
        Applies this filter to estimate 3-D structure tensors.
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        compressed : bool
            true, for compressed tensors; false, otherwise.
        
        Returns
        --------
        output : EigenTensors3
            structure tensors.
        """

    @overload
    def apply(self, x: Float3D, theta: Float3D, phi: Float3D, u1: Float3D,
              u2: Float3D, u3: Float3D, v1: Float3D, v2: Float3D, v3: Float3D,
              w1: Float3D, w2: Float3D, w3: Float3D, eu: Float3D, ev: Float3D,
              ew: Float3D, ep: Float3D, el: Float3D) -> None:
        """
        Applies this filter for the specified image and outputs. All
        outputs are optional and are computed for only non-null arrays.
        
        Parameters
        -----------
        x : Float3D
            input array for 3-D image.
        theta : Float3D
            orientation dip angle; 0 &lt;= theta &lt;= pi/2.
        phi : Float3D
            orientation azimuthal angle; -pi &lt;= phi &lt;= pi.
        u1 : Float3D
            1st component of 1st eigenvector.
        u2 : Float3D
            2nd component of 1st eigenvector.
        u3 : Float3D
            3rd component of 1st eigenvector.
        v1 : Float3D
            1st component of 2nd eigenvector.
        v2 : Float3D
            2nd component of 2nd eigenvector.
        v3 : Float3D
            3rd component of 2nd eigenvector.
        w1 : Float3D
            1st component of 3rd eigenvector.
        w2 : Float3D
            2nd component of 3rd eigenvector.
        w3 : Float3D
            3rd component of 3rd eigenvector.
        eu : Float3D
            largest eigenvalue corresponding to the eigenvector u.
        ev : Float3D
            middle eigenvalue corresponding to the eigenvector v.
        ew : Float3D
            smallest eigenvalue corresponding to the eigenvector w.
        ep : Float3D
            (eu-ev)/eu, a measure of planarity.
        el : Float3D
            (ev-ew)/eu, a measure of linearity.
        """
