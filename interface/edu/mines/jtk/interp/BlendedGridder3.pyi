from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.dsp import Sampling, Tensors3, LocalDiffusionKernel


class BlendedGridder3:
    """
    Tensor-guided blended neighbor gridding in 3D.
    Gridding is interpolation of a set of known sample values on a
    uniformly sampled grid. Here the interpolation is performed by
    a two-step blended neighbor process described by Hale (2009).
    
    The first step is to compute for all samples the distance to the
    nearest known sample and the value of that known sample. This first
    step produces a distance map and a nearest-neighbor interpolant.
    
    The second step is to blend (smooth) the nearest-neighbor interpolant,
    where the extent of smoothing varies spatially and is proportional to
    distances in the distance map.
    
    In tensor-guided gridding, we replace distance with time. Time is a
    simple term for non-Euclidean distance measured in a metric-tensor
    field. So "nearest" now means nearest in time. In the first step we
    compute a time map by solving an eikonal equation with coefficients
    that may be both anisotropic and spatially varying. In the second
    step, we blend the nearest-neighbor interpolant with an anisotropic
    and spatially varying smoothing filter.
    
    The default tensor field is homogeneous and isotropic. In this
    special case, time is equivalent to distance, and tensor-guided
    gridding is similar to gridding with Sibson's natural neighbor
    interpolant.
    
    Reference:
    <a href="http://www.mines.edu/~dhale/papers/Hale09ImageGuidedBlendedNeighborInterpolation.pdf">
    Hale, D., 2009, Image-guided blended neighbor interpolation, CWP-634</a>
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a gridder for default tensors.
        """

    @overload
    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs a gridder for default tensors and specified samples.
        The specified arrays are referenced; not copied.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2,x3).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    @overload
    def __init__(self, tensors: Tensors3) -> None:
        """
        Constructs a gridder for the specified tensors.
        
        Parameters
        -----------
        tensors : Tensors3
            the tensors.
        """

    @overload
    def __init__(self, tensors: Tensors3, f: Float1D, x1: Float1D, x2: Float1D,
                 x3: Float1D) -> None:
        """
        Constructs a gridder for the specified tensors and samples.
        The specified arrays are referenced; not copied.
        
        Parameters
        -----------
        tensors : Tensors3
            the tensors.
        f : Float1D
            array of sample values f(x1,x2,x3).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        x3 : Float1D
            array of sample x3 coordinates.
        """

    def setTensors(self, tensors: Tensors3) -> None:
        """
        Sets the tensor field used by this gridder.
        The default is a homogeneous and isotropic tensor field.
        
        Parameters
        -----------
        tensors : Tensors3
            the tensors; null for default tensors.
        """

    def setBlending(self, blending: bool) -> None:
        """
        Enables or disables blending in {@link #grid(Sampling,Sampling,Sampling)}.
        If true (the default), that method will perform both of the two
        steps described; that is, it will blend (smooth) after computing
        the nearest neighbor interpolant. If false, that method will perform
        only the first step and return the nearest neighbor interpolant.
        
        Parameters
        -----------
        blending : bool
            true, for blending; false, otherwise.
        """

    def setBlendingKernel(self, ldk: LocalDiffusionKernel) -> None:
        """
        Sets the local diffusion kernel used to perform blending.
        The default kernel uses a 2x2 stencil to compute derivatives.
        
        Parameters
        -----------
        ldk : LocalDiffusionKernel
            the local diffusion kernel.
        """

    def setSmoothness(self, smoothness: double) -> None:
        """
        Sets the smoothness of the interpolation of gridded values.
        The default is 0.5, which yields an interpolant with linear precision.
        Larger values yield smoother interpolants with plateaus at known samples.
        
        Parameters
        -----------
        smoothness : double
            the smoothness.
        """

    def setTimeMax(self, tmax: double) -> None:
        """
        Sets the maximum time computed by this gridder. The gridder has
        linear precision where times are less than the maximum time.
        
        Parameters
        -----------
        tmax : double
            the maximum time.
        """

    def setTimeMarkerX(self, tmx: bool) -> None:
        """
        Experimental use only.
        
        Parameters
        -----------
        tmx : bool
            time marker x.
        """

    def getTimeMarkerS(self) -> double:
        """
        Experimental use only.
        Returns
        --------
        output : double
            time marker s.
        """

    @overload
    def gridNearest(self, pnull: float, p: Float3D) -> Float3D:
        """
        Computes gridded values using nearest neighbors.
        Gridded values in the array p are computed for only unknown
        samples with value equal to the specified null value. Any
        known (non-null) sample values in the array p are not changed.
        
        This method also computes and returns an array of times to
        nearest-neighbor samples. Times are zero for known samples
        and are positive for gridded samples.
        
        Parameters
        -----------
        pnull : float
            the null value representing unknown samples.
        p : Float3D
            array of sample values to be gridded.
        
        Returns
        --------
        output : Float3D
            array of times to nearest known samples.
        """

    @overload
    def gridNearest(self, t: Float3D, p: Float3D) -> None:
        """
        Computes gridded values using nearest neighbors.
        Gridded values in the array p are computed for only unknown
        samples denoted by corresponding non-zero times in the array t.
        This method does not change known values in p, which correspond
        to zero times in t.
        
        Parameters
        -----------
        t : Float3D
            array of times to nearest known samples.
        p : Float3D
            array of nearest-neighbor gridded values.
        """

    def gridBlended(self, t: Float3D, p: Float3D, q: Float3D) -> None:
        """
        Computes gridded values using blended neighbors.
        Note that blended-neighbor gridding can be performed only
        after nearest-neighbor gridding. Blending does not change
        the values of known samples for which times are zero.
        
        Parameters
        -----------
        t : Float3D
            array of times to nearest known samples.
        p : Float3D
            array of nearest-neighbor gridded values.
        q : Float3D
            array of blended-neighbor gridded values.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D,
                     x3: Float1D) -> None:
        """
    
        """

    def grid(self, s1: Sampling, s2: Sampling, s3: Sampling) -> Float3D:
        """
    
        """
