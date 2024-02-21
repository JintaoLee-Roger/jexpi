from typing import overload
from edu.mines.jtk.mapping import *


class EigenTensors3:
    """
    An array of eigen-decompositions of tensors for 3D image processing.
    Each tensor is a symmetric positive-semidefinite 3-by-3 matrix:
    <pre><code>
    |a11 a12 a13|
    A = |a12 a22 a23|
    |a13 a23 a33|
    </code></pre>
    Such tensors can be used to parameterize anisotropic image processing.
    
    The eigen-decomposition of the matrix A is
    <pre><code>
    A = auuu' + avvv' + awww'
    = (au-av)uu' + (aw-av)ww' + avI
    </code></pre>
    where u, v, and w are orthogonal unit eigenvectors of A. (The notation
    u' denotes the transpose of u.) The outer products of eigenvectors are
    scaled by the non-negative eigenvalues au, av, and aw. The second
    equation exploits the identity uu' + vv' + ww' = I, and makes
    apparent the redundancy of the vector v.
    
    Only the 1st and 2nd components of the eigenvectors u and w are stored.
    Except for a sign, the 3rd components may be computed from the 1st and
    2nd. Because the tensors are independent of the choice of sign, the
    eigenvectors u and w are stored with an implied non-negative 3rd
    component.
    
    Storage may be further reduced by compression, whereby eigenvalues
    and eigenvectors are quantized. Quantization errors for eigenvalues
    (au,av,aw) are less than 0.001(au+av+aw). Quantization errors for
    eigenvectors are less than one degree of arc on the unit sphere.
    Memory required to store each tensor is 12 bytes if compressed, and
    28 bytes if not compressed.
    """

    @overload
    def __init__(self, n1: int, n2: int, n3: int, compressed: bool) -> None:
        """
        Constructs tensors for specified array dimensions. All eigenvalues
        and eigenvectors u and w are not set and are initially zero.
        
        Parameters
        -----------
        n1 : int
            number of tensors in 1st dimension.
        n2 : int
            number of tensors in 2nd dimension.
        n3 : int
            number of tensors in 3rd dimension.
        compressed : bool
            true, for compressed tensors; false, otherwise.
        """

    @overload
    def __init__(self, u1: Float3D, u2: Float3D, w1: Float3D, w2: Float3D,
                 au: Float3D, av: Float3D, aw: Float3D,
                 compressed: bool) -> None:
        """
        Constructs tensors for specified array dimensions and eigenvalues.
        The 3rd components of eigenvectors u and w are computed from the 1st
        and 2nd components and are assumed to be non-negative.
        
        Parameters
        -----------
        u1 : Float3D
            array of 1st components of u.
        u2 : Float3D
            array of 2nd components of u.
        w1 : Float3D
            array of 1st components of w.
        w2 : Float3D
            array of 2nd components of w.
        au : Float3D
            array of eigenvalues au.
        av : Float3D
            array of eigenvalues av.
        aw : Float3D
            array of eigenvalues aw.
        compressed : bool
            true, for compressed tensors; false, otherwise.
        """

    @overload
    def __init__(self, t: EigenTensors3) -> None:
        """
        Constructs tensors from the specified tensors.
        
        Parameters
        -----------
        t : EigenTensors3
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

    def getN3(self) -> int:
        """
        Gets the number of tensors in the 3rd dimension.
        Returns
        --------
        output : int
            the number of tensors in the 3rd dimension.
        """

    @overload
    def getTensor(self, i1: int, i2: int, i3: int, a: Float1D) -> None:
        """
        Gets tensor elements for specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        a : Float1D
            array {a11,a12,a13,a22,a23,a33} of tensor elements.
        """

    @overload
    def getTensor(self, i1: int, i2: int, i3: int) -> Float1D:
        """
        Gets tensor elements for specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        
        Returns
        --------
        output : Float1D
            a array {a11,a12,a13,a22,a23,a33} of tensor elements.
        """

    @overload
    def getEigenvalues(self, i1: int, i2: int, i3: int, a: Float1D) -> None:
        """
        Gets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        a : Float1D
            array {au,av,aw} of eigenvalues.
        """

    @overload
    def getEigenvalues(self, i1: int, i2: int, i3: int) -> Float1D:
        """
        Gets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        
        Returns
        --------
        output : Float1D
            array {au,av,aw} of eigenvalues.
        """

    @overload
    def getEigenvalues(self, au: Float3D, av: Float3D, aw: Float3D) -> None:
        """
        Gets eigenvalues for all tensors.
        
        Parameters
        -----------
        au : Float3D
            array of eigenvalues au.
        av : Float3D
            array of eigenvalues av.
        aw : Float3D
            array of eigenvalues aw.
        """

    @overload
    def getEigenvectorU(self, i1: int, i2: int, i3: int, u: Float1D) -> None:
        """
        Gets the eigenvector u for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        u : Float1D
            array {u1,u2,u3} of eigenvector components.
        """

    @overload
    def getEigenvectorU(self, i1: int, i2: int, i3: int) -> Float1D:
        """
        Gets the eigenvector u for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        
        Returns
        --------
        output : Float1D
            array {u1,u2,u3} of eigenvector components.
        """

    @overload
    def getEigenvectorV(self, i1: int, i2: int, i3: int, v: Float1D) -> None:
        """
        Gets the eigenvector v for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        v : Float1D
            array {v1,v2,v3} of eigenvector components.
        """

    @overload
    def getEigenvectorV(self, i1: int, i2: int, i3: int) -> Float1D:
        """
        Gets the eigenvector v for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        
        Returns
        --------
        output : Float1D
            array {v1,v2,v3} of eigenvector components.
        """

    @overload
    def getEigenvectorW(self, i1: int, i2: int, i3: int, w: Float1D) -> None:
        """
        Gets the eigenvector w for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        w : Float1D
            array {w1,w2,w3} of eigenvector components.
        """

    @overload
    def getEigenvectorW(self, i1: int, i2: int, i3: int) -> Float1D:
        """
        Gets the eigenvector w for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        
        Returns
        --------
        output : Float1D
            array {w1,w2,w3} of eigenvector components.
        """

    @overload
    def setTensor(self, i1: int, i2: int, i3: int, a: Float1D) -> None:
        """
        Sets tensor elements for specified indices.
        This method first computes an eigen-decomposition of the specified
        tensor, and then stores the computed eigenvectors and eigenvalues.
        The eigenvalues are ordered such that au &gt;= av &gt;= aw &gt;= 0.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        a : Float1D
            array {a11,a12,a13,a22,a23,a33} of tensor elements.
        """

    @overload
    def setTensor(self, i1: int, i2: int, i3: int, a11: float, a12: float,
                  a13: float, a22: float, a23: float, a33: float) -> None:
        """
        Sets tensor elements for specified indices.
        This method first computes an eigen-decomposition of the specified
        tensor, and then stores the computed eigenvectors and eigenvalues.
        The eigenvalues are ordered such that au &gt;= av &gt;= aw &gt;= 0.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        a11 : float
            tensor element a11.
        a12 : float
            tensor element a12.
        a13 : float
            tensor element a13.
        a22 : float
            tensor element a22.
        a23 : float
            tensor element a23.
        a33 : float
            tensor element a33.
        """

    @overload
    def setEigenvalues(self, au: float, av: float, aw: float) -> None:
        """
        Sets eigenvalues for all tensors.
        
        Parameters
        -----------
        au : float
            eigenvalue au.
        av : float
            eigenvalue av.
        aw : float
            eigenvalue aw.
        """

    @overload
    def setEigenvalues(self, au: Float3D, av: Float3D, aw: Float3D) -> None:
        """
        Sets eigenvalues for all tensors.
        
        Parameters
        -----------
        au : Float3D
            array of eigenvalues au.
        av : Float3D
            array of eigenvalues av.
        aw : Float3D
            array of eigenvalues aw.
        """

    @overload
    def setEigenvalues(self, i1: int, i2: int, i3: int, au: float, av: float,
                       aw: float) -> None:
        """
        Sets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        au : float
            eigenvalue au.
        av : float
            eigenvalue av.
        aw : float
            eigenvalue aw.
        """

    @overload
    def setEigenvalues(self, i1: int, i2: int, i3: int, a: Float1D) -> None:
        """
        Sets eigenvalues for the tensor with specified indices.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        a : Float1D
            array {au,av,aw} of eigenvalues.
        """

    @overload
    def setEigenvectorU(self, i1: int, i2: int, i3: int, u1: float, u2: float,
                        u3: float) -> None:
        """
        Sets the eigenvector u for the tensor with specified indices.
        The specified vector is assumed to have length one. If the 3rd
        component is negative, this method stores the negative of the
        specified vector, so that the 3rd component is positive.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        u1 : float
            1st component of u.
        u2 : float
            2nd component of u.
        u3 : float
            3nd component of u.
        """

    @overload
    def setEigenvectorU(self, i1: int, i2: int, i3: int, u: Float1D) -> None:
        """
        Sets the eigenvector u for the tensor with specified indices.
        The specified vector is assumed to have length one. If the 3rd
        component is negative, this method stores the negative of the
        specified vector, so that the 3rd component is positive.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        u : Float1D
            {u1,u2,u3} of eigenvector components.
        """

    @overload
    def setEigenvectorW(self, i1: int, i2: int, i3: int, w1: float, w2: float,
                        w3: float) -> None:
        """
        Sets the eigenvector w for the tensor with specified indices.
        The specified vector is assumed to have length one. If the 3rd
        component is negative, this method stores the negative of the
        specified vector, so that the 3rd component is positive.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        w1 : float
            1st component of w.
        w2 : float
            2nd component of w.
        w3 : float
            3nd component of w.
        """

    @overload
    def setEigenvectorW(self, i1: int, i2: int, i3: int, w: Float1D) -> None:
        """
        Sets the eigenvector w for the tensor with specified indices.
        The specified vector is assumed to have length one. If the 3rd
        component is negative, this method stores the negative of the
        specified vector, so that the 3rd component is positive.
        
        Parameters
        -----------
        i1 : int
            index for 1st dimension.
        i2 : int
            index for 2nd dimension.
        i3 : int
            index for 3rd dimension.
        w : Float1D
            {w1,w2,w3} of eigenvector components.
        """

    def scale(self, s: Float3D) -> None:
        """
        Scales eigenvalues of these tensors by specified factors.
        
        Parameters
        -----------
        s : Float3D
            array of scale factors.
        """

    def invert(self) -> None:
        """
        Inverts these tensors by inverting their eigenvalues.
        Takes no care to avoid division by zero eigenvalues.
        """

    def invertStructure(self, p0: double, p1: double, p2: double) -> None:
        """
        Inverts these tensors, assumed to be structure tensors.
        After inversion, all eigenvalues are in the range (0,1].
        Specifically, after inversion, 0 &lt; au &lt;= av &lt;= aw &lt;= 1.
        
        Before inversion, tensors are assumed to be structure tensors,
        for which eigenvalues au are not less than their corresponding
        eigenvalues av which are not less than their corresponding aw.
        (Any eigenvalues au for which this condition is not satisfied
        are set equal to the corresponding eigenvalue av; likewise for
        av and aw.) Structure tensors can, for example, be computed using
        {@link LocalOrientFilter}.
        
        Then, if any eigenvalues are equal to zero, this method adds a
        small fraction of the largest eigenvalue au to all eigenvalues.
        If am is the minimum of the eigenvalues aw after this perturbation,
        then the parameter p0 is used to compute a0 = pow(am/aw,p0), the
        parameter p1 is used to compute a1 = pow(aw/av,p1), and the parameter
        p2 is used to compute a2 = pow(av/au,p2). Inverted eigenvalues are
        then au = a0a1a2, av = a0a1 and aw = a0.
        
        In this way, p0 emphasizes overall amplitude, p1 emphasizes
        linearity and p2 emphasizes planarity. For amplitude-independent
        tensors with all eigenvalues av equal to one, set p0 = 0.0. To
        enhance linearity, set p1 &gt; 1.0. To enhance planarity, set
        p2 &gt; 1.0. To simply invert (and normalize) these tensors, set
        p0 = p1 = p2 = 1.0.
        
        Parameters
        -----------
        p0 : double
            power for amplitude.
        p1 : double
            power for linearity.
        p2 : double
            power for planarity.
        """
