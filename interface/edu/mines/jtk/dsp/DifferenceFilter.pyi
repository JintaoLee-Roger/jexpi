from typing import overload
from edu.mines.jtk.mapping import *


class DifferenceFilter:
    """
    A difference filter, with a transpose, inverse, and inverse-transpose.
    A 1-D difference filter is an approximation to a backward-difference
    filter: y[i] = x[i]-0.999x[i-1]. The constant 0.999 is less than
    one so that the recursive inverse filter y[i] = x[i]+0.999y[i-1] is
    stable. The inverse filter is sometimes called "leaky integration",
    and is especially useful for preconditioning inverse problems with
    smooth solutions.
    
    Sequential application of the backward-difference filter and its
    transpose yields an approximation to a negative centered 2nd-difference
    filter: y[i] = -x[i-1]+2x[i]-x[i+1].
    
    Extensions to 2-D and 3-D backward-difference filters are defined as in
    Claerbout, J., 1998, Multidimensional recursive filters via a helix:
    Geophysics, v. 63, n. 5, p. 1532-1541.
    
    These extensions were obtained here by factoring the negative centered
    2-D and 3-D 2nd-difference filters, respectively, using the Wilson-Burg
    algorithm, as in Fomel, S., Sava, P., Rickett, J., and Claerbout, J.,
    2003, The Wilson-Burg method of spectral factorization with application
    to helical filtering: Geophysical Prospecting, v. 51, p. 409-420.
    
    For all dimensions, these approximations yield less than one percent
    error in the negative centered 2nd-difference filter, relative to the
    exact central filter coefficient. For example, the error for a 2-D
    filter is less than 0.04 = 0.014, where 4 is the central coefficient
    in the exact negative 2nd-difference filter.
    """

    @overload
    def apply(self, x: Float1D, y: Float1D) -> None:
        """
        Applies this difference filter.
        
        Parameters
        -----------
        x : Float1D
            the filter input.
        y : Float1D
            the filter output.
        """

    @overload
    def apply(self, x: Float2D, y: Float2D) -> None:
        """
        Applies this difference filter.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    @overload
    def apply(self, x: Float3D, y: Float3D) -> None:
        """
        Applies this difference filter.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    @overload
    def applyTranspose(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the transpose of this filter.
        
        Parameters
        -----------
        x : Float1D
            the filter input.
        y : Float1D
            the filter output.
        """

    @overload
    def applyTranspose(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the transpose of this filter.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    @overload
    def applyTranspose(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the transpose of this filter.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    @overload
    def applyInverse(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the inverse of this filter.
        
        Parameters
        -----------
        x : Float1D
            the filter input.
        y : Float1D
            the filter output.
        """

    @overload
    def applyInverse(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the inverse of this filter.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    @overload
    def applyInverse(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the inverse of this filter.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """

    @overload
    def applyInverseTranspose(self, x: Float1D, y: Float1D) -> None:
        """
        Applies the inverse transpose of this filter.
        
        Parameters
        -----------
        x : Float1D
            the filter input.
        y : Float1D
            the filter output.
        """

    @overload
    def applyInverseTranspose(self, x: Float2D, y: Float2D) -> None:
        """
        Applies the inverse transpose of this filter.
        
        Parameters
        -----------
        x : Float2D
            the filter input.
        y : Float2D
            the filter output.
        """

    @overload
    def applyInverseTranspose(self, x: Float3D, y: Float3D) -> None:
        """
        Applies the inverse transpose of this filter.
        
        Parameters
        -----------
        x : Float3D
            the filter input.
        y : Float3D
            the filter output.
        """
