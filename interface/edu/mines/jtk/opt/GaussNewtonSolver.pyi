from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.opt import *


class GaussNewtonSolver:
    """
    Solve least-squares inverse of a non-linear Transform.
    See QuadraticSolver to solve least-squares inverse of a linear Transform.
    """

    @staticmethod
    def solve(self, data: VectConst, referenceModel: VectConst,
              perturbModel: VectConst, transform: Transform,
              dampOnlyPerturbation: bool, conjugateGradIterations: int,
              lineSearchIterations: int, linearizationIterations: int,
              lineSearchError: double, monitor: Monitor) -> Vect:
        """
        Solve nonquadratic objective function with Gauss Newton iterations.
        Minimizes
        <pre>
        [f(m+x)-data]'N[f(m+x)-data] + (m+x)'M(m+x)
        </pre>
        if dampOnlyPerturbation is true and
        <pre>
        [f(m+x)-data]'N[f(m+x)-data] + (x)'M(x)
        </pre>
        if dampOnlyPerturbation is false.
        </p>
        m is the reference model and x is the perturbation of that model,
        Returns full solution m+x.
        </p>
        </p>
        Iterative linearization of f(m+x) ~= f(m) + Fx makes the objective
        function quadratic in x: [f(m)+Fx-data]'N[f(m)+Fx-data] + (m+x)'M(m+x)
        x is solved with the specified number of conjugate gradient iterations.
        This perturbation is then scaled after searching the nonquadratic
        objective function with the specified number of line search iterations.
        The scaled perturbation x is added to the previous reference model m
        to update the new reference model m.  Relinearization is repeated for
        the specified number of linearization iterations. Cost is proprotional to
        <pre>
        linearizationIterations( 2 conjugateGradIterations + lineSearchIterations );
        </pre>
        Hard constraints, if any, will be applied during line searches, and
        to the final result.
        </p>
        "Line search error" is an acceptable fraction of imprecision
        in the scale factor for the line search.  A very small value
        will cause the maximum number of line seach iterations to be used.
        The optimized model will be a revised instance of this class.
        model to perturb the reference model.  It must be possible
        to project between the perturbed and reference model.
        The initial state of this vector is ignored.
        to model. If false, then damp the reference model plus
        the perturbation.
        the non-linear transform. Set to 1 if transform is already linear.
        (Anything less than 1 will be set to 1)
        search to scale a pertubation before adding to reference model.
        Recommend 20 or greater.  Use 0 if you want to disable the
        line search altogether and add the perturbation with a scale
        factor of 1.
        gradient iterations.
        in the scale factor for the line search. Recommend 0.001 or smaller.
        
        Parameters
        -----------
        data : VectConst
            The data to be fit.
        referenceModel : VectConst
            This is the starting velocity model.
        perturbModel : VectConst
            If non-null, then use instances of this
        transform : Transform
            Describes the linear or nonlinear transform.
        dampOnlyPerturbation : bool
            If true then, only damp perturbations
        conjugateGradIterations : int
            Number of times to relinearize
        lineSearchIterations : int
            Number of iterations for a a line
        linearizationIterations : int
            The specified number of conjugate
        lineSearchError : double
            is an acceptable fraction of imprecision
        monitor : Monitor
            Report progress here, if non-null.
        
        Returns
        --------
        output : Vect
            Result of optimization, using a cloned instance of referenceModel.
        """

    @staticmethod
    def setExpensiveDebug(self, debug: bool) -> None:
        """
        Turn on expensive checking of transform and vector properties
        during solving of equations.
        
        Parameters
        -----------
        debug : bool
            If true, then turn on expensive debugging.
        """
