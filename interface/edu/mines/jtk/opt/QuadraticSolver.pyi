from typing import overload
from edu.mines.jtk.mapping import *


class QuadraticSolver:
    """
    Minimize a simple quadratic objective function.
    Finds the x that minimizes the quadratic function 0.5 x'Hx + b'x .
    Solves Hx + b = 0  for x (the Normal Equations of a least-squares problem)
    b is the gradient for x=0, and H is the hessian.
    The algorithm is a conjugate gradient.
    A is an approximate inverse Hessian, making AH more diagonal
    and improving convergence.
    A may also include a model-dependent conditioning to converge
    earlier on eigenfunction of most importance.
    The algorithm assumes that the application of H dominates the cost.
    <pre>
    x = p = u = 0;
    beta = 0;
    g = b;
    a = A g;
    q = H a;
    do {
    p = -a + beta p
    u = Hp = -q + beta u
    scalar = -p'g/p'u
    x = x + scalar p
    if (done) return x
    g = H x + b = g + scalar u
    a = A g
    q = H a
    beta = p'H A g / p'H p = p'q/p'u
    }
    </pre>
    </p>
    Also contains a solver for a least-squares inverse of a linear
    transform, using QuadraticTransform as a wrapper.
    """

    def __init__(self, quadratic: Quadratic) -> None:
        """
        Implement the Quadratic interface and pass to this constructor.
        Pass a vector b to the constructor (a copy is cloned internally).
        This solver calls Vect and Quadratic methods.
        Does not call Vect.multiplyInverseCovariance().
        
        Parameters
        -----------
        quadratic : Quadratic
            Defines the Hessian quadratic term.
        """

    @overload
    def solve(self, numberIterations: int, monitor: Monitor) -> Vect:
        """
        Return a new solution after the number of conjugate gradient
        iterations.
        
        Parameters
        -----------
        numberIterations : int
            is the number of iterations to perform.
        monitor : Monitor
            If non-null, then track all progress.
        
        Returns
        --------
        output : Vect
            Optimized solution
        """

    @overload
    @staticmethod
    def solve(self, data: VectConst, referenceModel: VectConst,
              linearTransform: LinearTransform, dampOnlyPerturbation: bool,
              conjugateGradIterations: int, monitor: Monitor) -> Vect:
        """
        Solve quadratic objective function for linear transform.
        Minimizes
        <pre>
        [F(m+x)-data]'N[F(m+x)-data] + (m+x)'M(m+x)
        </pre>
        if dampOnlyPerturbation is true and
        <pre>
        [F(m+x)-data]'N[F(m+x)-data] + (x)'M(x)
        </pre>
        if dampOnlyPerturbation is false.
        to reference model. If false, then damp the reference model plus
        the perturbation.
        gradient iterations.
        
        Parameters
        -----------
        data : VectConst
            The data to be fit.
        referenceModel : VectConst
            Initialize with this model.
        linearTransform : LinearTransform
            Describes the linear transform.
        dampOnlyPerturbation : bool
            If true then, only damp perturbations
        conjugateGradIterations : int
            The specified number of conjugate
        monitor : Monitor
            Report progress here, if non-null.
        
        Returns
        --------
        output : Vect
            Result of optimization
        """
