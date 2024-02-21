from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import *

class LocalLaplacianFilter:
    """
    Local Laplacian filter defined by non-constant diffusion tensors.
    The Laplacian operator appears in diffusion equations, and this
    filter is useful in the context of anisotropic diffusion filtering.
    
    This filter computes y = y+G'DGx where G is an approximation to the
    gradient operator, G' is its adjoint, and D is a local diffusion
    tensor that determines for each image sample the direction of the
    Laplacian filter.
    
    Local Laplacian filters are rarely used alone. While zeroing some
    features in images, they tend to attenuate many other features as
    well. Therefore, these filters are typically used in combinations
    with others.
    
    For example, the filter implied by (I+G'DG)y = G'DGx acts as a
    notch filter. It attenuates features for which G'DGx is zero while
    preserving other features. Diffusivities d (inside D) control the
    width of the notch. Note that application of this filter requires
    solving a sparse symmetric positive-definite system of equations.
    
    An even simpler example is the filter implied by (I+G'DG)y = x.
    This filter smooths features in the directions implied by the
    tensors D. Again, application of this filter requires solving a
    sparse symmetric positive-definite system of equations.
    
    The accumulation of the filter output in y = y+G'DGx is useful when
    constructing such combination filters. For y = 0, this filter computes
    y = G'DGx. For y = x, this filter computes y = (I+G'DG)x.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a local Laplacian filter.
        """

    @overload
    def __init__(self, scale: double) -> None:
        """
        Constructs a local Laplacian filter.
        
        Parameters
        -----------
        scale : double
            scale factor for all diffusion coefficients.
        """

    @overload
    def apply(self, d: Tensors2, x: Float2D, y: Float2D) -> None:
        """
        Computes y = y+G'DGx for 2D arrays x and y.
        
        Parameters
        -----------
        d : Tensors2
            a tensor.
        x : Float2D
            input array. Must be distinct from the array y.
        y : Float2D
            input/output array. Must be distinct from the array x.
        """

    @overload
    def apply(self, d: Tensors3, x: Float3D, y: Float3D) -> None:
        """
        Computes y = y+G'DGx for 3D arrays x and y.
        
        Parameters
        -----------
        d : Tensors3
            a 3x3 tensor.
        x : Float3D
            input array. Must be distinct from the array y.
        y : Float3D
            input/output array. Must be distinct from the array x.
        """
