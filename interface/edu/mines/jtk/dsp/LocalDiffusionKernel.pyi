from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.util import *
from edu.mines.jtk.dsp import *

class LocalDiffusionKernel:
    """
    A local diffusion kernel for use in anisotropic diffusion filtering.
    
    This kernel is a filter that computes y += G'DGx where G is a
    gradient operator, G' is its adjoint, and D is a local diffusion
    tensor field that determines for each image sample the filter
    coefficients.
    
    A local diffusion kernel is typically used in combinations with others.
    For example, the filter implied by (I+G'DG)y = G'DGx acts as a notch
    filter. It attenuates features for which G'DG is zero while preserving
    other features. The diffusion tensors in D control the width, orientation,
    and anisotropy of the spectral notch. Note that application of this filter
    requires solution of a sparse symmetric positive-definite system of
    equations.
    
    An even simpler example is the filter implied by (I+G'DG)y = x. This
    filter smooths features in the directions implied by the tensors D.
    Again, application of this filter requires solving a sparse symmetric
    positive-definite system of equations.
    
    The accumulation of the kernel output in y = y+G'DGx is useful when
    constructing such filter combinations. Given y = 0, this kernel
    computes y = G'DGx. Given y = x, it computes y = (I+G'DG)x.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a local diffusion kernel with default 2x2 stencil.
        """

    @overload
    def __init__(self, s: Stencil) -> None:
        """
        Constructs a local diffusion kernel with specified stencil.
        
        Parameters
        -----------
        s : Stencil
            the stencil used to approximate a derivative.
        """

    def getStencil(self) -> Stencil:
        """
        Gets the stencil used by this local diffusion kernel.
        Returns
        --------
        output : Stencil
            the stencil.
        """

    def setNumberOfPasses(self, npass: int) -> None:
        """
        Sets the number of kernel passes in each apply of this filter.
        For example, if npass = 2, then the output is computed in two
        passes: (1) y += G'DGx, (2) y += G'DGy.
        The default is one pass.
        
        Parameters
        -----------
        npass : int
            the number of passes.
        """

    @overload
    def apply(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for constant isotropic identity tensor.
        
        Parameters
        -----------
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, d: Tensors2, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for specified tensor coefficients.
        
        Parameters
        -----------
        d : Tensors2
            tensor coefficients.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, c: float, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for specified scale factor.
        Uses a constant isotropic identity tensor.
        
        Parameters
        -----------
        c : float
            constant scale factor for tensor coefficients.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, d: Tensors2, c: float, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for specified tensor coefficients and scale factor.
        
        Parameters
        -----------
        d : Tensors2
            tensor coefficients.
        c : float
            constant scale factor for tensor coefficients.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, c: float, s: Float2D, x: Float2D, y: Float2D) -> None:
        """
        Applies this filter for specified scale factors.
        Uses a constant isotropic identity tensor.
        
        Parameters
        -----------
        c : float
            constant scale factor for tensor coefficients.
        s : Float2D
            array of scale factors for tensor coefficients.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, d: Tensors2, c: float, s: Float2D, x: Float2D,
              y: Float2D) -> None:
        """
        Applies this filter for specified tensor coefficients and scale factors.
        
        Parameters
        -----------
        d : Tensors2
            tensor coefficients.
        c : float
            constant scale factor for tensor coefficients.
        s : Float2D
            array of scale factors for tensor coefficients.
        x : Float2D
            input array.
        y : Float2D
            output array.
        """

    @overload
    def apply(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for a constant isotropic identity tensor.
        
        Parameters
        -----------
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, d: Tensors3, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for specified tensor coefficients.
        
        Parameters
        -----------
        d : Tensors3
            tensor coefficients.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, c: float, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for specified scale factor.
        Uses a constant isotropic identity tensor.
        
        Parameters
        -----------
        c : float
            constant scale factor for tensor coefficients.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, d: Tensors3, c: float, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for specified tensor coefficients and scale factor.
        
        Parameters
        -----------
        d : Tensors3
            tensor coefficients.
        c : float
            constant scale factor for tensor coefficients.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, c: float, s: Float3D, x: Float3D, y: Float3D) -> None:
        """
        Applies this filter for specified scale factors.
        Uses a constant isotropic identity tensor.
        
        Parameters
        -----------
        c : float
            constant scale factor for tensor coefficients.
        s : Float3D
            array of scale factors for tensor coefficients.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """

    @overload
    def apply(self, d: Tensors3, c: float, s: Float3D, x: Float3D,
              y: Float3D) -> None:
        """
        Applies this filter for specified tensor coefficients and scale factors.
        
        Parameters
        -----------
        d : Tensors3
            tensor coefficients.
        c : float
            constant scale factor for tensor coefficients.
        s : Float3D
            array of scale factors for tensor coefficients.
        x : Float3D
            input array.
        y : Float3D
            output array.
        """
