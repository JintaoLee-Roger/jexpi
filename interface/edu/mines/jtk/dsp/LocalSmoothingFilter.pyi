from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import Tensors2, Tensors3, LocalDiffusionKernel

class LocalSmoothingFilter:
    """
    Local smoothing of images with tensor filter coefficients.
    Smoothing is performed by solving a sparse symmetric positive-definite
    (SPD) system of equations: (I+G'DG)y = x, where G is a gradient operator,
    D is an SPD tensor field, x is an input image, and y is an output image.
    
    The sparse system of filter equations (I+G'DG)y = x is solved iteratively,
    beginning with y = x. Iterations continue until either the error in the
    solution y is below a specified threshold or the number of iterations
    exceeds a specified limit.
    
    For low wavenumbers the output of this filter approximates the solution
    to an anisotropic inhomogeneous diffusion equation, where the filter
    input x corresponds to the initial condition at time t = 0 and filter
    output y corresponds to the solution at some later time t.
    
    Additional smoothing filters may be applied to the input image x before
    or after solving the sparse system of equations for the smoothed output
    image y. These additional filters compensate for deficiencies in the
    gradient operator G, which is a finite-difference approximation that is
    poor for high wavenumbers near the Nyquist limit. The extra smoothing
    filters attenuate these high wavenumbers.
    
    The additional smoothing filter S is a simple 3x3 (or, in 3D, 3x3x3)
    weighted-average filter that zeros Nyquist wavenumbers. This filter
    is fast and has non-negative coefficients. However, it may smooth too
    much, as it attenuates all non-zero wavenumbers, not only the highest
    wavenumbers. Moreover, this filter is not isotropic.
    
    The other additional smoothing operator L is an isotropic low-pass
    filter designed to pass wavenumbers up to a specified maximum.
    Although slower than S, the cost of applying L to the input image x is
    likely to be insignificant relative to the cost of solving the sparse
    system of equations for the output image y.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a local smoothing filter with default parameters.
        The default parameter small is 0.01 and the default maximum
        number of iterations is 100. Uses a default 2x2 stencil for the
        derivatives in the operator G.
        """

    @overload
    def __init__(self, small: double, niter: int) -> None:
        """
        Constructs a local smoothing filter with specified iteration parameters.
        Uses a default 2x2 stencil for the derivatives in the operator G.
        times the norm of the input array.
        
        Parameters
        -----------
        small : double
            stop when norm of residuals is less than this factor
        niter : int
            stop when number of iterations exceeds this limit.
        """

    @overload
    def __init__(self, small: double, niter: int,
                 ldk: LocalDiffusionKernel) -> None:
        """
        Constructs a local smoothing filter with specified parameters.
        times the norm of the input array.
        
        Parameters
        -----------
        small : double
            stop when norm of residuals is less than this factor
        niter : int
            stop when number of iterations exceeds this limit.
        ldk : LocalDiffusionKernel
            the local diffusion kernel that computes y += (I+G'DG)x.
        """

    def setPreconditioner(self, pc: bool) -> None:
        """
        Sets the use of a preconditioner in this local smoothing filter.
        A preconditioner requires extra memory and more computing time
        per iteration, but may result in fewer iterations.
        The default is to not use a preconditioner.
        
        Parameters
        -----------
        pc : bool
            true, to use a preconditioner; false, otherwise.
        """

    @overload
    def apply(self, c: float, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter for specified constant scale factor.
        Local smoothing for 1D arrays is a special case that requires no tensors.
        All tensors are implicitly scalar values equal to one, so that filtering
        is determined entirely by the specified constant scale factor.
        
        Parameters
        -----------
        c : float
            constant scale factor.
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def apply(self, c: float, s: Float1D, x: Float1D, y: Float1D) -> None:
        """
        Applies this filter for specified scale factors.
        Local smoothing for 1D arrays is a special case that requires no tensors.
        All tensors are implicitly scalar values equal to one, so that filtering
        is determined entirely by the specified scale factors.
        
        Parameters
        -----------
        c : float
            constant scale factor.
        s : Float1D
            array of scale factors.
        x : Float1D
            input array.
        y : Float1D
            output array.
        """

    @overload
    def apply(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for identity tensors.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, c: float, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for identity tensors and specified scale factor.
        
        Parameters
        -----------
        c : float
            constant scale factor.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, c: float, s: Float2D, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for identity tensors and specified scale factors.
        
        Parameters
        -----------
        c : float
            constant scale factor.
        s : Float2D
            array of scale factors.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, d: Tensors2, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for specified tensors.
        
        Parameters
        -----------
        d : Tensors2
            tensors.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, d: Tensors2, c: float, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for specified tensors and scale factor.
        
        Parameters
        -----------
        d : Tensors2
            tensors.
        c : float
            constant scale factor for tensors.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, d: Tensors2, c: float, s: Float2D, x: Float2D,
              y: Float2D) -> None:
        """
        Applies this filter for specified tensors and scale factors.
        
        Parameters
        -----------
        d : Tensors2
            tensors.
        c : float
            constant scale factor for tensors.
        s : Float2D
            array of scale factors for tensors.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for identity tensors.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, c: float, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for identity tensors and specified scale factor.
        
        Parameters
        -----------
        c : float
            constant scale factor.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, c: float, s: Float3D, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for identity tensors and specified scale factors.
        
        Parameters
        -----------
        c : float
            constant scale factor.
        s : Float3D
            array of scale factors.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, d: Tensors3, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for specified tensors.
        
        Parameters
        -----------
        d : Tensors3
            tensors.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, d: Tensors3, c: float, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for specified tensors and scale factor.
        
        Parameters
        -----------
        d : Tensors3
            tensors.
        c : float
            constant scale factor for tensors.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, d: Tensors3, c: float, s: Float3D, x: Float3D,
              y: Float3D) -> None:
        """
        Applies this filter for specified tensors and scale factors.
        
        Parameters
        -----------
        d : Tensors3
            tensors.
        c : float
            constant scale factor for tensors.
        s : Float3D
            array of scale factors for tensors.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def applySmoothS(self, x: Float2D, y: Float2D) -> None:
        """
        Applies a simple 3x3 weighted-average smoothing filter S.
        Input and output arrays x and y may be the same array.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def applySmoothS(self, x: Float3D, y: Float3D) -> None:
        """
        Applies a simple 3x3x3 weighted-average smoothing filter S.
        Input and output arrays x and y may be the same array.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def applySmoothL(self, kmax: double, x: Float2D, y: Float2D) -> None:
        """
        Applies an isotropic low-pass smoothing filter L.
        Input and output arrays x and y may be the same array.
        
        Parameters
        -----------
        kmax : double
            maximum wavenumber not attenuated, in cycles/sample.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def applySmoothL(self, kmax: double, x: Float3D, y: Float3D) -> None:
        """
        Applies an isotropic low-pass smoothing filter L.
        Input and output arrays x and y may be the same array.
        
        Parameters
        -----------
        kmax : double
            maximum wavenumber not attenuated, in cycles/sample.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """
