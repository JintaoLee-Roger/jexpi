from typing import overload
from edu.mines.jtk.mapping import *


class EigenTensors2:
    """
    An array of eigen-decompositions of tensors for 2D image processing.
    Each tensor is a symmetric positive-semidefinite 2-by-2 matrix:
    <pre><code>
    A = |a11 a12|
    |a12 a22|
    </code></pre>
    Such tensors can be used to parameterize anisotropic image processing.
    
    The eigen-decomposition of the matrix A is
    <pre><code>
    A = auuu' + avvv'
    = (au-av)uu' + avI
    </code></pre>
    where u and v are orthogonal unit eigenvectors of A. (The notation u'
    denotes the transpose of u.) The outer products of eigenvectors are
    scaled by the non-negative eigenvalues au and av. The second equation
    exploits the identity uu' + vv' = I, and makes apparent the redundancy
    of the vector v.
    """

    @overload
    def __init__(self, n1: int, n2: int) -> None:
        """
        Constructs tensors for specified array dimensions. All eigenvalues
        and eigenvectors are not set and are initially zero.
        
        Parameters
        -----------
        n1 : int
            number of tensors in 1st dimension.
        n2 : int
            number of tensors in 2nd dimension.
        """

    @overload
    def __init__(self, u1: Float2D, u2: Float2D, au: Float2D,
                 av: Float2D) -> None:
        """
        Constructs tensors for specified array dimensions and eigenvalues.
        
        Parameters
        -----------
        u1 : Float2D
            array of 1st components of u.
        u2 : Float2D
            array of 2nd components of u.
        au : Float2D
            array of 1D eigenvalues.
        av : Float2D
            array of 2D eigenvalues.
        """

    @overload
    def __init__(self, t: EigenTensors2) -> None:
        """
        Constructs tensors from the specified tensors.
        
        Parameters
        -----------
        t : EigenTensors2
            the tensors from which to copy eigenvectors and eigenvalues.
        """

    def getN1(self) -> int:
        """
        Gets the number of tensors in the 1st dimension.
        Returns
        --------
        output : int
            the number of tensors in the 1st dimension.
        """

    def getN2(self) -> int:
        """
        Gets the number of tensors in the 2nd dimension.
        Returns
        --------
        output : int
            the number of tensors in the 2nd dimension.
        """

    @overload
    def getTensor(self, i1: int, i2: int, a: Float1D) -> None:
        """
        Gets tensor elements for specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        a : Float1D
            array {a11,a12,a22} of tensor elements.
        """

    @overload
    def getTensor(self, i1: int, i2: int) -> Float1D:
        """
        Gets tensor elements for specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        
        Returns
        --------
        output : Float1D
            a array {a11,a12,a22} of tensor elements.
        """

    @overload
    def getEigenvalues(self, i1: int, i2: int, a: Float1D) -> None:
        """
        Gets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        a : Float1D
            array {au,av} of eigenvalues.
        """

    @overload
    def getEigenvalues(self, i1: int, i2: int) -> Float1D:
        """
        Gets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        
        Returns
        --------
        output : Float1D
            array {au,av} of eigenvalues.
        """

    @overload
    def getEigenvalues(self, au: Float2D, av: Float2D) -> None:
        """
        Gets eigenvalues for all tensors.
        
        Parameters
        -----------
        au : Float2D
            array of eigenvalues au.
        av : Float2D
            array of eigenvalues av.
        """

    @overload
    def getEigenvectorU(self, i1: int, i2: int, u: Float1D) -> None:
        """
        Gets the eigenvector u for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        u : Float1D
            array {u1,u2} of eigenvector components.
        """

    @overload
    def getEigenvectorU(self, i1: int, i2: int) -> Float1D:
        """
        Gets the eigenvector u for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        
        Returns
        --------
        output : Float1D
            array {u1,u2} of eigenvector components.
        """

    @overload
    def getEigenvectorV(self, i1: int, i2: int, v: Float1D) -> None:
        """
        Gets the eigenvector v for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        v : Float1D
            array {v1,v2} of eigenvector components.
        """

    @overload
    def getEigenvectorV(self, i1: int, i2: int) -> Float1D:
        """
        Gets the eigenvector v for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        
        Returns
        --------
        output : Float1D
            array {v1,v2} of eigenvector components.
        """

    @overload
    def setTensor(self, i1: int, i2: int, a: Float1D) -> None:
        """
        Sets tensor elements for specified indices.
        This method first computes an eigen-decomposition of the specified
        tensor, and then stores the computed eigenvectors and eigenvalues.
        The eigenvalues are ordered such that au &gt;= av &gt;= 0.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        a : Float1D
            array {a11,a12,a22} of tensor elements.
        """

    @overload
    def setTensor(self, i1: int, i2: int, a11: float, a12: float,
                  a22: float) -> None:
        """
        Sets tensor elements for specified indices.
        This method first computes an eigen-decomposition of the specified
        tensor, and then stores the computed eigenvectors and eigenvalues.
        The eigenvalues are ordered such that au &gt;= av &gt;= 0.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        a11 : float
            tensor element a11.
        a12 : float
            tensor element a12.
        a22 : float
            tensor element a22.
        """

    @overload
    def setEigenvalues(self, au: float, av: float) -> None:
        """
        Sets eigenvalues for all tensors.
        
        Parameters
        -----------
        au : float
            eigenvalue au.
        av : float
            eigenvalue av.
        """

    @overload
    def setEigenvalues(self, i1: int, i2: int, au: float, av: float) -> None:
        """
        Sets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        au : float
            eigenvalue au.
        av : float
            eigenvalue av.
        """

    @overload
    def setEigenvalues(self, i1: int, i2: int, a: Float1D) -> None:
        """
        Sets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        a : Float1D
            array {au,av} of eigenvalues.
        """

    @overload
    def setEigenvalues(self, au: Float2D, av: Float2D) -> None:
        """
        Sets eigenvalues for all tensors.
        
        Parameters
        -----------
        au : Float2D
            array of eigenvalues au.
        av : Float2D
            array of eigenvalues av.
        """

    @overload
    def setEigenvectorU(self, i1: int, i2: int, u1: float, u2: float) -> None:
        """
        Sets the eigenvector u for the tensor with specified indices.
        The specified vector is assumed to have length one.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        u1 : float
            1st component of u.
        u2 : float
            2nd component of u.
        """

    @overload
    def setEigenvectorU(self, i1: int, i2: int, u: Float1D) -> None:
        """
        Sets the eigenvector u for the tensor with specified indices.
        The specified vector is assumed to have length one.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        u : Float1D
            {u1,u2} of eigenvector components.
        """

    def scale(self, s: Float2D) -> None:
        """
        Scales eigenvalues of these tensors by specified factors.
        
        Parameters
        -----------
        s : Float2D
            array of scale factors.
        """

    def invert(self) -> None:
        """
        Inverts these tensors by inverting their eigenvalues.
        Takes no care to avoid division by zero eigenvalues.
        """

    def invertStructure(self, p0: double, p1: double) -> None:
        """
        Inverts these tensors, assumed to be structure tensors.
        After inversion, all eigenvalues are in the range (0,1].
        Specifically, after inversion, 0 &lt; au &lt;= av &lt;= 1.
        
        Before inversion, tensors are assumed to be structure tensors,
        for which eigenvalues au are not less than their corresponding
        eigenvalues av. (Any eigenvalues au for which this condition is
        not satisfied are set equal to the corresponding eigenvalue av.)
        Structure tensors can, for example, be computed using
        {@link LocalOrientFilter}.
        
        Then, if any eigenvalues are equal to zero, this method adds a
        small fraction of the largest eigenvalue au to all eigenvalues.
        If am is the minimum of the eigenvalues av after this perturbation,
        then the parameter p0 is used to compute a0 = pow(am/av,p0) and
        the parameter p1 is used to compute a1 = pow(av/au,p1). Inverted
        eigenvalues are then au = a0a1 and av = a0.
        
        In this way, p0 emphasizes overall amplitude and p1 emphasizes
        linearity. For amplitude-independent tensors with all eigenvalues
        av equal to one, set p0 = 0.0. To enhance linearity, set p1 &gt; 1.0.
        To simply invert (and normalize) these tensors, set p0 = p1 = 1.0.
        
        Parameters
        -----------
        p0 : double
            power for amplitude.
        p1 : double
            power for linearity.
        """
