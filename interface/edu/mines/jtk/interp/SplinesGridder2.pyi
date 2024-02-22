from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.interp import *
from edu.mines.jtk.dsp import *


class SplinesGridder2:
    """
    Tensor-guided 2D gridding with bi-harmonic and harmonic splines.
    At locations where gridded values are not constrained by specified
    (known) sample values, the gridded values q satisfy the equation
    (G'DGG'DG+tG'DG)q = 0, where G is a finite-difference approximation
    of the gradient operator, G' is its transpose, D is a tensor field,
    and t is a scalar constant that controls the tension, the weight of
    the harmonic G'DG operator relative to the bi-harmonic G'DGG'DG
    operator.
    
    In the isotropic and homogeneous case, where D = I is the identity
    matrix, this gridder is an implementation of Smith and Wessel's
    (1990) gridding with continuous curvature splines in tension. The
    finite-difference approximations to derivatives in G are different,
    however, because of the tensors D between G' and G in G'DG. These
    tensors D must be symmetric and positive-semidefinite (SPSD) so that
    the finite-difference operators G'DG and G'DGG'DG are SPSD as well.
    
    Another difference between this implementation and that of Smith and
    Wessel (1990) is that a multigrid method is not used here to find the
    gridded values q. Multigrid methods are ineffective for tensors fields
    D that are anisotropic and inhomogeneous. Instead, this implementation
    uses conjugate-gradient (CG) iterations.
    
    The gridded values q must be obtained by solving iteratively the large
    sparse system of equations (G'DGG'DG+tG'DG)q = 0. To facilitate a CG
    solver, these equations are rewritten as (K+MAM)q = (K-MAK)q, where
    A = G'DGG'DG+tG'DG, M is a diagonal matrix operator with ones where
    sample values are missing and zeros where values are known, and
    K = I-M is a diagonal matrix with ones where sample values are known
    and zero where they are missing. The matrix K+MAM on the left-hand side
    is symmetric and positive-definite (SPD), so that CG iterations can be
    used to solve for the unknown values in q. Only known values in q appear
    in the right-hand side column vector (K-MAK)q.
    
    See Smith, W.H.F., and P. Wessel, 1990, Gridding with continuous
    curvature splines in tension: Geophysics, 55, 293--305.
    """

    @overload
    def __init__(self) -> None:
        """
        Constructs a gridder for default tensors.
        """

    @overload
    def __init__(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
        Constructs a gridder for default tensors and specified samples.
        The specified arrays are referenced; not copied.
        
        Parameters
        -----------
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    @overload
    def __init__(self, tensors: Tensors2) -> None:
        """
        Constructs a gridder for the specified tensors.
        
        Parameters
        -----------
        tensors : Tensors2
            the tensors.
        """

    @overload
    def __init__(self, tensors: Tensors2, f: Float1D, x1: Float1D,
                 x2: Float1D) -> None:
        """
        Constructs a gridder for the specified tensors and samples.
        The specified arrays are referenced; not copied.
        
        Parameters
        -----------
        tensors : Tensors2
            the tensors.
        f : Float1D
            array of sample values f(x1,x2).
        x1 : Float1D
            array of sample x1 coordinates.
        x2 : Float1D
            array of sample x2 coordinates.
        """

    def setTensors(self, tensors: Tensors2) -> None:
        """
        Sets the tensor field used by this gridder.
        The default is a homogeneous and isotropic tensor field.
        
        Parameters
        -----------
        tensors : Tensors2
            the tensors; null for default tensors.
        """

    def setTension(self, tension: double) -> None:
        """
        Sets the tension, the weight for the harmonic spline.
        The default tension is 0.0, for a purely bi-harmonic spline.
        
        This tension parameter is not equivalent to the parameter t in
        the class documentation above. The latter would be infinite if
        the tension specified here could be set to 1.0.
        
        Parameters
        -----------
        tension : double
            the tension; must be in the range [0:1).
        """

    def setMaxIterations(self, niter: int) -> None:
        """
        Sets the maximum number of conjugate-gradient iterations.
        The default maximum number of iterations is 10,000.
        
        Parameters
        -----------
        niter : int
            the maximum number of iterations.
        """

    def getIterationCount(self) -> int:
        """
        Returns the number of conjugate-gradient iterations required.
        The number returned corresponds to the last use of this gridder.
        Returns
        --------
        output : int
            the number of iterations.
        """

    def getResiduals(self) -> Float1D:
        """
        Gets the initial residual and one residual for each iteration.
        The residuals returned correspond to the last use of this gridder.
        
        Residuals are normalized root-mean-square differences between
        the left and right sides of the system of equations that are
        solved iteratively when computing gridded values. The returned
        residuals are normalized, so that the zeroth residual (before any
        conjugate-gradient iterations are performed) is one.
        Returns
        --------
        output : Float1D
            array of residuals.
        """

    @overload
    def gridMissing(self, qnull: float, q: Float2D) -> None:
        """
        Computes gridded values that are missing in the specified array.
        Missing values are those equal to the specified null value.
        
        Parameters
        -----------
        qnull : float
            the null value representing missing samples.
        q : Float2D
            array in which missing (null) values are to be replaced.
        """

    @overload
    def gridMissing(self, m: Bool2D, q: Float2D) -> None:
        """
        Computes gridded values that are missing in the specified array.
        Missing values are those with missing-value flags set to true.
        
        Parameters
        -----------
        m : boolean[][]
            array of missing-value flags; true where value is missing.
        q : Float2D
            array in which flagged missing values are to be replaced.
        """

    def setScattered(self, f: Float1D, x1: Float1D, x2: Float1D) -> None:
        """
    
        """

    def grid(self, s1: Sampling, s2: Sampling) -> Float2D:
        """
    
        """
