from typing import overload
from edu.mines.jtk.mapping import *


class LinearInterpolator:
    """
    A linear interpolator for uniformly-sampled functions y(x).
    Interpolation of functions y(x1,x2) is bi-linear.
    Interpolation of functions y(x1,x2,x3) is tri-linear.
    """

    def getExtrapolation(self) -> Extrapolation:
        """
        Gets the extrapolation method for this interpolator.
        Returns
        --------
        output : Extrapolation
            the extrapolation method.
        """

    def setExtrapolation(self, extrap: Extrapolation) -> None:
        """
        Sets the extrapolation method for this interpolator.
        The default extrapolation method is extrapolation with zeros.
        
        Parameters
        -----------
        extrap : Extrapolation
            the extrapolation method.
        """

    @overload
    def setUniformSampling(self, nxu: int, dxu: double, fxu: double) -> None:
        """
        Sets the current sampling for a uniformly-sampled function y(x).
        In some applications, this sampling never changes, and this method
        may be called only once for this interpolator.
        
        Parameters
        -----------
        nxu : int
            the number of uniform samples.
        dxu : double
            the uniform sampling interval.
        fxu : double
            the value x corresponding to the first uniform sample yu[0].
        """

    @overload
    def setUniformSamples(self, yu: Float1D) -> None:
        """
        Sets the current samples for a uniformly-sampled function y(x).
        If sample values are complex numbers, real and imaginary parts are
        packed in the array as real, imaginary, real, imaginary, and so on.
        
        Sample values are passed by reference, not by copy. Changes to sample
        values in the specified array will yield changes in interpolated values.
        by reference, not by copy.
        
        Parameters
        -----------
        yu : Float1D
            array[nxu] of uniform samples of y(x);
        """

    @overload
    def setUniform(self, nxu: int, dxu: double, fxu: double,
                   yu: Float1D) -> None:
        """
        Sets the current sampling and samples for a function y(x).
        This method simply calls the two methods
        {@link #setUniformSampling(int,double,double)} and
        {@link #setUniformSamples(float[])}
        with the specified parameters.
        by reference, not by copy.
        
        Parameters
        -----------
        nxu : int
            the number of uniform samples.
        dxu : double
            the uniform sampling interval.
        fxu : double
            the value x corresponding to the first uniform sample yu[0].
        yu : Float1D
            array[nxu] of uniform samples of y(x);
        """

    @overload
    def interpolate(self, x: double) -> float:
        """
        Interpolates the current uniform samples as real numbers.
        
        Parameters
        -----------
        x : double
            the value x at which to interpolate y(x).
        
        Returns
        --------
        output : float
            the interpolated y(x).
        """

    @overload
    def interpolate(self, nx: int, x: Float1D, y: Float1D) -> None:
        """
        Interpolates the current uniform samples as real numbers.
        
        Parameters
        -----------
        nx : int
            the number of output samples.
        x : Float1D
            array[nx] of values x at which to interpolate y(x).
        y : Float1D
            array[nx] of interpolated output y(x).
        """

    @overload
    def interpolate(self, nx: int, dx: double, fx: double, y: Float1D) -> None:
        """
        Interpolates the current uniform samples as real numbers.
        
        This method does not perform any anti-alias filtering, which may or
        may not be necessary to avoid aliasing when the specified output
        sampling interval exceeds the current uniform sampling interval.
        
        Parameters
        -----------
        nx : int
            the number of output samples.
        dx : double
            the output sampling interval.
        fx : double
            the value x corresponding to the first output sample y[0].
        y : Float1D
            array[nx] of interpolated output y(x).
        """

    @overload
    def setUniformSampling(self, nx1u: int, dx1u: double, fx1u: double,
                           nx2u: int, dx2u: double, fx2u: double) -> None:
        """
        Sets the current sampling for a uniformly-sampled function y(x1,x2).
        In some applications, this sampling never changes, and this method
        may be called only once for this interpolator.
        
        Parameters
        -----------
        nx1u : int
            the number of uniform samples in 1st dimension.
        dx1u : double
            the uniform sampling interval in 1st dimension.
        fx1u : double
            the value x1 correponding to the first sample yu[0][0].
        nx2u : int
            the number of uniform samples in 2nd dimension.
        dx2u : double
            the uniform sampling interval in 2nd dimension.
        fx2u : double
            the value x2 correponding to the first sample yu[0][0].
        """

    @overload
    def setUniformSamples(self, yu: Float2D) -> None:
        """
        Sets the current samples for a uniformly-sampled function y(x1,x2).
        If sample values are complex numbers, real and imaginary parts are
        packed in the array as real, imaginary, real, imaginary, and so on.
        
        Sample values are passed by reference, not by copy. Changes to sample
        values in the specified array will yield changes in interpolated values.
        by reference, not by copy.
        
        Parameters
        -----------
        yu : Float2D
            array[nx2u][nx1u] of samples of y(x1,x2);
        """

    @overload
    def setUniform(self, nx1u: int, dx1u: double, fx1u: double, nx2u: int,
                   dx2u: double, fx2u: double, yu: Float2D) -> None:
        """
        Sets the current sampling and samples for a function y(x1,x2).
        This method simply calls the two methods
        {@link #setUniformSampling(int,double,double,int,double,double)} and
        {@link #setUniformSamples(float[][])}
        with the specified parameters.
        by reference, not by copy.
        
        Parameters
        -----------
        nx1u : int
            the number of uniform samples in 1st dimension.
        dx1u : double
            the uniform sampling interval in 1st dimension.
        fx1u : double
            the value x1 correponding to the first sample yu[0][0].
        nx2u : int
            the number of uniform samples in 2nd dimension.
        dx2u : double
            the uniform sampling interval in 2nd dimension.
        fx2u : double
            the value x2 correponding to the first sample yu[0][0].
        yu : Float2D
            array[nx2u][nx1u] of samples of y(x1,x2);
        """

    @overload
    def interpolate(self, x1: double, x2: double) -> float:
        """
        Interpolates the current uniform samples as real numbers.
        
        Parameters
        -----------
        x1 : double
            the value x1 at which to interpolate y(x1,x2).
        x2 : double
            the value x2 at which to interpolate y(x1,x2).
        
        Returns
        --------
        output : float
            the interpolated y(x1,x2).
        """

    @overload
    def setUniformSampling(self, nx1u: int, dx1u: double, fx1u: double,
                           nx2u: int, dx2u: double, fx2u: double, nx3u: int,
                           dx3u: double, fx3u: double) -> None:
        """
        Sets the current sampling for a uniformly-sampled function y(x1,x2,x3).
        In some applications, this sampling never changes, and this method
        may be called only once for this interpolator.
        
        Parameters
        -----------
        nx1u : int
            the number of uniform samples in 1st dimension.
        dx1u : double
            the uniform sampling interval in 1st dimension.
        fx1u : double
            the value x1 correponding to the first sample yu[0][0][0].
        nx2u : int
            the number of uniform samples in 2nd dimension.
        dx2u : double
            the uniform sampling interval in 2nd dimension.
        fx2u : double
            the value x2 correponding to the first sample yu[0][0][0].
        nx3u : int
            the number of uniform samples in 3rd dimension.
        dx3u : double
            the uniform sampling interval in 3rd dimension.
        fx3u : double
            the value x3 correponding to the first sample yu[0][0][0].
        """

    @overload
    def setUniformSamples(self, yu: Float3D) -> None:
        """
        Sets the current samples for a uniformly-sampled function y(x1,x2,x3).
        If sample values are complex numbers, real and imaginary parts are
        packed in the array as real, imaginary, real, imaginary, and so on.
        
        Sample values are passed by reference, not by copy. Changes to sample
        values in the specified array will yield changes in interpolated values.
        by reference, not by copy.
        
        Parameters
        -----------
        yu : Float3D
            array[nx3u][nx2u][nx1u] of samples of y(x1,x2,x3);
        """

    @overload
    def setUniform(self, nx1u: int, dx1u: double, fx1u: double, nx2u: int,
                   dx2u: double, fx2u: double, nx3u: int, dx3u: double,
                   fx3u: double, yu: Float3D) -> None:
        """
        Sets the current sampling and samples for a function y(x1,x2,x3).
        This method simply calls the two methods
        {@link #setUniformSampling(
        int,double,double,int,double,double,int,double,double)} and
        {@link #setUniformSamples(float[][][])}
        with the specified parameters.
        by reference, not by copy.
        
        Parameters
        -----------
        nx1u : int
            the number of uniform samples in 1st dimension.
        dx1u : double
            the uniform sampling interval in 1st dimension.
        fx1u : double
            the value x1 correponding to the first sample yu[0][0][0].
        nx2u : int
            the number of uniform samples in 2nd dimension.
        dx2u : double
            the uniform sampling interval in 2nd dimension.
        fx2u : double
            the value x2 correponding to the first sample yu[0][0][0].
        nx3u : int
            the number of uniform samples in 3rd dimension.
        dx3u : double
            the uniform sampling interval in 3rd dimension.
        fx3u : double
            the value x3 correponding to the first sample yu[0][0][0].
        yu : Float3D
            array[nx3u][nx2u][nx1u] of samples of y(x1,x2,x3);
        """

    @overload
    def interpolate(self, x1: double, x2: double, x3: double) -> float:
        """
        Interpolates the current uniform samples as real numbers.
        
        Parameters
        -----------
        x1 : double
            the value x1 at which to interpolate y(x1,x2,x3).
        x2 : double
            the value x2 at which to interpolate y(x1,x2,x3).
        x3 : double
            the value x3 at which to interpolate y(x1,x2,x3).
        
        Returns
        --------
        output : float
            the interpolated y(x1,x2,x3).
        """
