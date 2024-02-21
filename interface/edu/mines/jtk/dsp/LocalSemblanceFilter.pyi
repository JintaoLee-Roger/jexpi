from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.dsp import *


class LocalSemblanceFilter:
    """
    Computes local semblance images using local smoothing filters.
    Local semblance (Hale, 2009) is defined to be a squared smoothed-image
    divided by a smoothed squared-image, where smoothing is performed by local
    smoothing filters along the eigenvectors of a structure tensor field.
    
    Reference:
    <a
    href="http://www.mines.edu/~dhale/papers/Hale09StructureOrientedSmoothingAndSemblance.pdf">
    Hale, D., 2009, Structure-oriented smoothing and semblance, CWP-635</a>
    """

    def __init__(self, halfWidth1: int, halfWidth2: int) -> None:
        """
        Constructs a local semblance filter.
        
        Parameters
        -----------
        halfWidth1 : int
            half-width of 1st smoothing filter.
        halfWidth2 : int
            half-width of 2nd smoothing filter.
        """

    @overload
    def semblance(self, f: Float1D, s: Float1D) -> None:
        """
        Computes local semblance for a 1D array.
        
        Parameters
        -----------
        f : Float1D
            the array of input values.
        s : Float1D
            the array of output semblance values.
        """

    @overload
    def semblance(self, f: Float1D) -> Float1D:
        """
        Returns local semblance for a 1D array.
        
        Parameters
        -----------
        f : Float1D
            the array of input values.
        
        Returns
        --------
        output : Float1D
            the array of semblance values.
        """

    @overload
    def semblance(self, d: Direction2, t: EigenTensors2, f: Float2D,
                  s: Float2D) -> None:
        """
        Computes local semblance for a 2D array.
        
        Parameters
        -----------
        d : Direction2
            direction(s) for the first inner smoothing.
        t : EigenTensors2
            eigen-decomposition of a tensor field.
        f : Float2D
            the array of input values.
        s : Float2D
            the array of output semblance values.
        """

    @overload
    def semblance(self, d: Direction2, t: EigenTensors2,
                  f: Float2D) -> Float2D:
        """
        Returns local semblance for a 2D array.
        
        Parameters
        -----------
        d : Direction2
            direction(s) for the first inner smoothing.
        t : EigenTensors2
            eigen-decomposition of a tensor field.
        f : Float2D
            the array of input values.
        
        Returns
        --------
        output : Float2D
            the array of semblance values.
        """

    @overload
    def semblance(self, d: Direction3, t: EigenTensors3, f: Float3D,
                  s: Float3D) -> None:
        """
        Computes local semblance for a 3D array.
        
        Parameters
        -----------
        d : Direction3
            direction(s) for the first inner smoothing.
        t : EigenTensors3
            eigen-decomposition of a tensor field.
        f : Float3D
            the array of input values.
        s : Float3D
            the array of output semblance values.
        """

    @overload
    def semblance(self, d: Direction3, t: EigenTensors3,
                  f: Float3D) -> Float3D:
        """
        Returns local semblance for a 3D array.
        
        Parameters
        -----------
        d : Direction3
            direction(s) for the first inner smoothing.
        t : EigenTensors3
            eigen-decomposition of a tensor field.
        f : Float3D
            the array of input values.
        
        Returns
        --------
        output : Float3D
            the array of semblance values.
        """

    @overload
    def smooth1(self, f: Float1D, g: Float1D) -> None:
        """
        Applies the 1st inner smoothing of this semblance filter.
        
        Parameters
        -----------
        f : Float1D
            the input array.
        g : Float1D
            the output array.
        """

    @overload
    def smooth1(self, f: Float1D) -> Float1D:
        """
        Applies the 1st inner smoothing of this semblance filter.
        
        Parameters
        -----------
        f : Float1D
            the input array.
        
        Returns
        --------
        output : Float1D
            the output array.
        """

    @overload
    def smooth1(self, d: Direction2, t: EigenTensors2, f: Float2D,
                g: Float2D) -> None:
        """
        Applies the 1st inner smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction2
            direction(s) for the first inner smoothing.
        t : EigenTensors2
            eigen-decomposition of a tensor field.
        f : Float2D
            the input array.
        g : Float2D
            the output array.
        """

    @overload
    def smooth1(self, d: Direction2, t: EigenTensors2, f: Float2D) -> Float2D:
        """
        Applies the 1st inner smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction2
            direction(s) for the first inner smoothing.
        t : EigenTensors2
            eigen-decomposition of a tensor field.
        f : Float2D
            the input array.
        
        Returns
        --------
        output : Float2D
            the output array.
        """

    @overload
    def smooth1(self, d: Direction3, t: EigenTensors3, f: Float3D,
                g: Float3D) -> None:
        """
        Applies the 1st inner smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction3
            direction(s) for the first inner smoothing.
        t : EigenTensors3
            eigen-decomposition of a tensor field.
        f : Float3D
            the input array.
        g : Float3D
            the output array.
        """

    @overload
    def smooth1(self, d: Direction3, t: EigenTensors3, f: Float3D) -> Float3D:
        """
        Applies the 1st inner smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction3
            direction(s) for the first inner smoothing.
        t : EigenTensors3
            eigen-decomposition of a tensor field.
        f : Float3D
            the input array.
        
        Returns
        --------
        output : Float3D
            the output array.
        """

    @overload
    def smooth2(self, f: Float1D, g: Float1D) -> None:
        """
        Applies the 2nd outer smoothing of this semblance filter.
        
        Parameters
        -----------
        f : Float1D
            the input array.
        g : Float1D
            the output array.
        """

    @overload
    def smooth2(self, f: Float1D) -> Float1D:
        """
        Applies the 2nd outer smoothing of this semblance filter.
        
        Parameters
        -----------
        f : Float1D
            the input array.
        
        Returns
        --------
        output : Float1D
            the output array.
        """

    @overload
    def smooth2(self, d: Direction2, t: EigenTensors2, f: Float2D,
                g: Float2D) -> None:
        """
        Applies the 2nd outer smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction2
            direction(s) for the first inner smoothing.
        t : EigenTensors2
            eigen-decomposition of a tensor field.
        f : Float2D
            the input array.
        g : Float2D
            the output array.
        """

    @overload
    def smooth2(self, d: Direction2, t: EigenTensors2, f: Float2D) -> Float2D:
        """
        Applies the 2nd outer smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction2
            direction(s) for the first inner smoothing.
        t : EigenTensors2
            eigen-decomposition of a tensor field.
        f : Float2D
            the input array.
        
        Returns
        --------
        output : Float2D
            the output array.
        """

    @overload
    def smooth2(self, d: Direction3, t: EigenTensors3, f: Float3D,
                g: Float3D) -> None:
        """
        Applies the 2nd outer smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction3
            direction(s) for the first inner smoothing.
        t : EigenTensors3
            eigen-decomposition of a tensor field.
        f : Float3D
            the input array.
        g : Float3D
            the output array.
        """

    @overload
    def smooth2(self, d: Direction3, t: EigenTensors3, f: Float3D) -> Float3D:
        """
        Applies the 2nd outer smoothing of this semblance filter.
        
        Parameters
        -----------
        d : Direction3
            direction(s) for the first inner smoothing.
        t : EigenTensors3
            eigen-decomposition of a tensor field.
        f : Float3D
            the input array.
        
        Returns
        --------
        output : Float3D
            the output array.
        """
