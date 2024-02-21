from typing import overload
from edu.mines.jtk.mapping import *


class Quantiler:
    """
    A quantile estimator that enables incremental updates. In other words,
    the estimator processes samples sequentially in one pass, and does not
    require all samples to be sorted, or even partially sorted, in fast
    random-access memory.
    
    The quantile estimate is probably not useful for fewer than 10 samples.
    
    The estimate is most accurate for cumulative distribution functions
    that are smooth in the neighborhood of the desired quantile q. For
    such distributions, the accuracy of the estimate improves with
    successive updates.
    
    This class is an implementation of the algorithm published by Jain,
    R. and Chlamtac, I., 1985, The PP algorithm for dynamic calculation of
    quantiles and histograms without storing observations:  Comm. ACM,
    v. 28, n. 10.
    """

    @overload
    def __init__(self, q: float) -> None:
        """
        Constructs a quantiler for the specified quantile fraction.
        
        Parameters
        -----------
        q : float
            the quantile fraction; 0 &lt;= q &lt;= 1 is required.
        """

    @overload
    def __init__(self, q: float, fnull: float) -> None:
        """
        Constructs a quantiler for the specified quantile fraction and null value.
        
        Parameters
        -----------
        q : float
            the quantile; 0 &lt;= q &lt;= 1 is required.
        fnull : float
            the null value to be ignored in estimating the quantile.
        """

    @overload
    def estimate(self) -> float:
        """
        Returns the current quantile estimate.
        Returns
        --------
        output : float
            the current quantile estimate.
        """

    @overload
    def update(self, f: float) -> float:
        """
        Updates the quantile estimate with the specified sample.
        
        Parameters
        -----------
        f : float
            the sample used to update the estimate.
        
        Returns
        --------
        output : float
            the updated quantile estimate.
        """

    @overload
    def update(self, f: Float1D) -> float:
        """
        Updates the quantile estimate with the specified samples.
        
        Parameters
        -----------
        f : Float1D
            array[] of samples used to update the estimate.
        
        Returns
        --------
        output : float
            the updated quantile estimate.
        """

    @overload
    def update(self, f: Float2D) -> float:
        """
        Updates the quantile estimate with the specified samples.
        
        Parameters
        -----------
        f : Float2D
            array[][] of samples used to update the estimate.
        
        Returns
        --------
        output : float
            the updated quantile estimate.
        """

    @overload
    def update(self, f: Float3D) -> float:
        """
        Updates the quantile estimate with the specified samples.
        
        Parameters
        -----------
        f : Float3D
            array[][][] of samples used to update the estimate.
        
        Returns
        --------
        output : float
            the updated quantile estimate.
        """

    @overload
    @staticmethod
    def estimate(self, q: float, f: Float1D) -> float:
        """
        Estimates the specified quantile for the specified and samples.
        
        Parameters
        -----------
        q : float
            the quantile; 0 &lt;= q &lt;= 1 is required.
        f : Float1D
            array[] of samples used to compute the estimate.
        
        Returns
        --------
        output : float
            the quantile estimate.
        """

    @overload
    @staticmethod
    def estimate(self, q: float, f: Float2D) -> float:
        """
        Estimates the specified quantile for the specified and samples.
        
        Parameters
        -----------
        q : float
            the quantile; 0 &lt;= q &lt;= 1 is required.
        f : Float2D
            array[][] of samples used to compute the estimate.
        
        Returns
        --------
        output : float
            the quantile estimate.
        """

    @overload
    @staticmethod
    def estimate(self, q: float, f: Float3D) -> float:
        """
        Estimates the specified quantile for the specified and samples.
        
        Parameters
        -----------
        q : float
            the quantile; 0 &lt;= q &lt;= 1 is required.
        f : Float3D
            array[][][] of samples used to compute the estimate.
        
        Returns
        --------
        output : float
            the quantile estimate.
        """

    @overload
    @staticmethod
    def estimate(self, q: float, fnull: float, f: Float1D) -> float:
        """
        Estimates the specified quantile for the specified null value and samples.
        
        Parameters
        -----------
        q : float
            the quantile; 0 &lt;= q &lt;= 1 is required.
        fnull : float
            the null value to be ignored in estimating the quantile.
        f : Float1D
            array[] of samples used to compute the estimate.
        
        Returns
        --------
        output : float
            the quantile estimate.
        """

    @overload
    @staticmethod
    def estimate(self, q: float, fnull: float, f: Float2D) -> float:
        """
        Estimates the specified quantile for the specified null value and samples.
        
        Parameters
        -----------
        q : float
            the quantile; 0 &lt;= q &lt;= 1 is required.
        fnull : float
            the null value to be ignored in estimating the quantile.
        f : Float2D
            array[][] of samples used to compute the estimate.
        
        Returns
        --------
        output : float
            the quantile estimate.
        """

    @overload
    @staticmethod
    def estimate(self, q: float, fnull: float, f: Float3D) -> float:
        """
        Estimates the specified quantile for the specified null value and samples.
        
        Parameters
        -----------
        q : float
            the quantile; 0 &lt;= q &lt;= 1 is required.
        fnull : float
            the null value to be ignored in estimating the quantile.
        f : Float3D
            array[][][] of samples used to compute the estimate.
        
        Returns
        --------
        output : float
            the quantile estimate.
        """
