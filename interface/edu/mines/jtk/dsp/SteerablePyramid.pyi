from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import *


class SteerablePyramid:
    """
    Steerable pyramid for 2D and 3D images. Includes creation of the steerable
    pyramid, estimation of local orientation and dimensionality attributes,
    application of steering weights and scaling to enhance locally linear
    features, and construction of the filtered image.
    
    This implementation of the steerable pyramid transform performs a
    multi-scale, multi-orientation decomposition of an input image through
    application of radial and directional filters in wavenumber domain.
    The basis steerable filter amplitudes are proportional to cos^2(theta).
    Three basis orientations are used for 2D, and six orientations are used
    for 3D images.  Radial filters are used to partition the data into
    1-octave bands, with a cosine taper.  Images are subsampled for each
    pyramid level which greatly reduces processing effort for lower
    wavenumbers.
    
    Directionally-filtered basis images are used to estimate local orientation
    and dimensionality.  Preprocessing, which includes averaging in space
    and scale domains, is applied for these estimates.  Steering weights can be
    calculated and applied.  Scaling and thresholding can also be applied,
    based on a local dimensionality attribute.  For 3D images, processing can
    be applied to enhance either locally-linear or locally-planar features.
    
    The number of pyramid levels to use is calculated from the size of the
    input image, assuming a minimum basis image dimension of 9 samples in x,y
    or z.  The input image is padded before it is transformed to wavenumber
    domain, where the filters are applied.  The main reason for this padding is
    to avoid losing first or last samples when subsampling.  We like the number
    of samples to be such that, for number of samples n in x, y, or z,
    (n-1)/2+1 will always yield an integer.
    
    The format of the steerable pyramid is a 4-dimensional array for 2D, and a
    5-dimensional array for 3D.  The first dimension is level number and second
    dimension is basis filter orientation.  Below these are either 2D or 3D
    arrays.
    To illustrate for 2D:
    
    [0][0][0][0] to [0][0][n2][n1] = level 0, theta 0
    
    [0][1][0][0] to [0][1][n2][n1] = level 0, theta PI/3
    
    [0][2][0][0] to [0][2][n2][n1] = level 0, theta 2PI/3
    
    [1][0][0][0] to [1][0][(n2-1)/2+1][(n1-1)/2+1] = level 1, theta 0
    
    [1][1][0][0] to [1][1][(n2-1)/2+1][(n1-1)/2+1] = level 1, theta PI/3
    
    [1][2][0][0] to [1][2][(n2-1)/2+1][(n1-1)/2+1] = level 1, theta 2PI/3
    
    ...
    
    [NLEVEL-1][2][0][0] to
    [NLEVEL-1][2][(n2-1)/(2^(NLEVEL-1))+1][(n1-1)/(2^(NLEVEL-1))+1]
    = level N-1, theta 2PI/3
    
    [NLEVEL][0][0][0] to [NLEVEL][0][(n2-1)/(2^NLEVEL)+1][(n1-1)/(2^NLEVEL)+1]
    = residual low-wavenumber image
    
    The 3D steerable pyramid array is the same except that it is arrays of
    arrays of 3D, rather than 2D arrays.
    """

    @overload
    def __init__(self) -> None:
        """
        Construct a steerable pyramid with default cutoff wavenumbers
        used in the radial low-pass filters.  Default values are:
        ka=0.60 and kb=1.00, where ka and kb are wavenumbers at start and
        end of taper (Amp(ka)=1.0, Amp(kb)=0.0).
        """

    @overload
    def __init__(self, ka: double, kb: double) -> None:
        """
        Construct a steerable pyramid with specified cutoff wavenumbers
        used in the radial low-pass filters.
        
        Parameters
        -----------
        ka : double
            wavenumber at start of taper.  Amp(ka)=1.
        kb : double
            wavenumber at end of taper.  Amp(ka)=0.
        """

    @overload
    def makePyramid(self, x: Float2D) -> Float4D:
        """
        Creates a steerable pyramid representation of an input 2D image.
        2D image.
        
        Parameters
        -----------
        x : Float2D
            input 2D image.
        
        Returns
        --------
        output : Float4D
            array containing steerable pyramid representation of the input
        """

    @overload
    def makePyramid(self, x: Float3D) -> Float5D:
        """
        Creates a steerable pyramid representation of an input 3D image.
        3D image.
        
        Parameters
        -----------
        x : Float3D
            input 3D image.
        
        Returns
        --------
        output : Float5D
            array containing steerable pyramid representation of the input
        """

    @overload
    def sumPyramid(self, keeplow: bool, spyr: Float4D) -> Float2D:
        """
        Sums all basis images from an input 2D steerable pyramid to create a
        filtered output image.  Optionally, residual low-wavenumber image can
        be zeroed.
        
        Parameters
        -----------
        keeplow : bool
            if true:keep low-wavenumber energy, if false: zero it.
        spyr : Float4D
            input 2D steerable pyramid.
        
        Returns
        --------
        output : Float2D
            array containing output filtered 2D image.
        """

    @overload
    def sumPyramid(self, keeplow: bool, spyr: Float5D) -> Float3D:
        """
        Sums all basis images from an input 3D steerable pyramid to create a
        filtered output image.  Optionally, residual low-wavenumber image can
        be zeroed.
        
        Parameters
        -----------
        keeplow : bool
            if true:keep low-wavenumber energy, if false: zero it.
        spyr : Float5D
            input 3D steerable pyramid.
        
        Returns
        --------
        output : Float3D
            array containing output filtered 3D image.
        """

    @overload
    def estimateAttributes(self, sigma: double, spyr: Float4D) -> Float4D:
        """
        Estimation of local orientation and linearity attributes in 2D.
        Preprocessing and 2D Gaussian filtering are applied to input
        basis images before analysis, and averaging of data from adjacent
        pyramid levels is performed.  Gaussian half-widths are varied
        when averaging adjacent levels to maintain consistent smoothing
        for the levels being averaged.
        
        The format of the output attributes is a 4-dimensional array.
        The first dimension is level number and second dimension is type
        of attribute.  Below these are 2D arrays:
        
        [0][0][0][0] to [0][0][n2][n1] = level 0, theta attribute (radians)
        
        [0][1][0][0] to [0][1][n2][n1] = level 0, linearity attribute
        
        [1][0][0][0] to [1][0][(n2-1)/2+1][(n1-1)/2+1] = level 1,
        theta attribute (radians)
        
        [1][1][0][0] to [1][1][(n2-1)/2+1][(n1-1)/2+1] = level 1,
        linearity attribute
        
        ...
        
        [NLEVEL-1][1][0][0] to
        [NLEVEL-1][1][(n2-1)/(2^(NLEVEL-1))+1][(n1-1)/(2^(NLEVEL-1))+1]
        = level N-1, linearity attribute
        attribute for all sample locations in every pyramid level.  Array
        consists of numlevels2 2D sub-arrays.  For each level the first
        sub-array contains orientation theta in radians, and the second
        contains linearity attribute ranging from 0 to 1.
        
        Parameters
        -----------
        sigma : double
            half-width of 2D Gaussian smoothing filter.
        spyr : Float4D
            input 2D steerable pyramid.
        
        Returns
        --------
        output : Float4D
            array containing local orientation estimate and linearity
        """

    @overload
    def estimateAttributes(self, forlinear: bool, sigma: double,
                           spyr: Float5D) -> Float5D:
        """
        Estimation of local orientation and linearity attributes in 3D.
        Preprocessing and 3D Gaussian filtering are applied to input
        basis images before analysis, and averaging of data from adjacent
        pyramid levels is performed.  Gaussian half-widths are varied
        when averaging adjacent levels to maintain consistent smoothing
        for the levels being averaged.
        
        In 3D we have a choice of filtering to enhance locally-planar or
        locally-linear image features.  There is a parameter in this
        method to select one of these choices.  If enhancement of planar
        features is selected the output orientation attributes define the
        normal to locally-planar features, and the dimensionality attribute
        is a measure of planarity.  If enhancement of locally-linear
        features is selected the output orientation attributes define the
        orientation of a locally-linear feature, and the dimensionality
        attribute is a local measure of linearity.
        
        The format of the output attributes is a 5-dimensional array.
        The first dimension is level number and second dimension is type
        of attribute.  Below these are 3D arrays:
        
        [0][0][0][0][0] to [0][0][n3][n2][n1] = level 0, direction cosine a
        
        [0][0][0][0][0] to [0][0][n3][n2][n1] = level 0, direction cosine b
        
        [0][0][0][0][0] to [0][0][n3][n2][n1] = level 0, direction cosine c
        
        [0][1][0][0][0] to [0][1][n3][n2][n1] = level 0, dimensionality attribute
        
        These are repeated for all levels, subsampled for every successive level.
        planar.
        attribute for all sample locations in every pyramid level.  Array
        consists of numlevels4 3D sub-arrays.  For each level the first three
        sub-arrays contain direction cosines, and the fourth contains
        dimensionality attribute ranging from 0 to 1.
        
        Parameters
        -----------
        forlinear : bool
            true: apply to enhance locally linear, false: apply for
        sigma : double
            half-width of 3D Gaussian smoothing filter.
        spyr : Float5D
            input 3D steerable pyramid.
        
        Returns
        --------
        output : Float5D
            array containing local orientation estimate and dimensionality
        """

    @overload
    def steerScale(self, forlinear: bool, linpowr: int, k: float,
                   thresh: float, attr: Float5D, spyr: Float5D) -> None:
        """
        Applies steering weights and scaling or thresholding based on linearity
        attribute to the basis images in the input 3D steerable pyramid array.
        If "forlinear" option was used when estimateAttributes was run, this
        method will convert basis images from plane-enhancing cos^2-filtered
        to line-enhancing sin^2-filtered versions.
        Scaling options include:
        No scaling (linpowr=0).
        Linearity raised to a power (1 &le; linpowr &le; 98).
        Sigmoidal thresholding (linpowr=99) Typical values for thresholding
        parameters are k=50.0, thresh=0.5.
        for planar.
        
        Parameters
        -----------
        forlinear : bool
            true: apply to enhance locally linear, false: apply
        linpowr : int
            linearity power and scaling type switch.
        k : float
            sigmoidal thresholding steepness.
        thresh : float
            threshold.
        attr : Float5D
            input array containing direction cosines and dimensionality.
        spyr : Float5D
            input/output 3D steerable pyramid.
        """

    @overload
    def steerScale(self, linpowr: int, k: float, thresh: float, attr: Float4D,
                   spyr: Float4D) -> None:
        """
        Applies steering weights and scaling or thresholding based on linearity
        attribute to the basis images in the input 2D steerable pyramid.
        Scaling options include:
        No scaling (linpowr=0).
        Linearity raised to a power (1 &le; linpowr &le; 98).
        Sigmoidal thresholding (linpowr=99) Typical values for thresholding
        parameters are k=50.0, thresh=0.5.
        
        Parameters
        -----------
        linpowr : int
            linearity power and scaling type switch.
        k : float
            sigmoidal thresholding steepness.
        thresh : float
            threshold.
        attr : Float4D
            input array containing local orientation and linearity.
        spyr : Float4D
            input/output 2D steerable pyramid.
        """
