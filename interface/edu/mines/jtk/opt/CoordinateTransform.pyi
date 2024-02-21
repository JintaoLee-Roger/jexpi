from typing import overload
from edu.mines.jtk.mapping import *


class CoordinateTransform:
    """
    Find a best linear combination of input
    coordinates to fit output coordinates.
    Finds a_io (a with subscripts i and o)
    to best approximate the linear transform.
    <pre>
    out_o = sum_i ( a_io  in_i )
    </pre>
    where in_i are input coordinates,<br>
    out_o are output coordinates,<br>
    i is the index of each input dimension,<br>
    and o is the index of each output dimension.<br>
    </p>
    The optimum coefficients minimize this least
    squares error:
    <pre>
    sum_oj [ sum_i ( a_io  in_ij ) - out_oj ]^2
    </pre>
    where in_ij is an input array of different coordinates,<br>
    out_oj is an output array of corresponding coordinates,<br>
    and j is the index of pairs of coordinates to be fit
    in a least-squares sense.
    </p>
    Normal equations (indexed by k) are solved independently for each o:
    <pre>
    sum_ij ( in_kj  in_ij  a_io ) = sum_j ( in_kj  out_oj )
    </pre>
    The Hessian is <code> H = sum_j ( in_kj  in_ij ) </code>
    and the gradient <code> b = - sum_j ( in_kj  out_oj ) </code>
    </p>
    The solution is undamped and may not behave as you
    want for degenerate solutions.
    </p>
    If the linear transform needs a translation shift,
    then include a constant as one of the input coordinates.
    """

    def __init__(self, dimensionOut: int, dimensionIn: int) -> None:
        """
        Constructor sets number of input and output coordinates.
        
        Parameters
        -----------
        dimensionOut : int
            Number of output coordinates.
        dimensionIn : int
            Number of input coordinates.
        """

    def add(self, out: Double1D, ins: Double1D) -> None:
        """
        Add an observation of a set of input and output coordinates
        You should add enough of these to determine (or overdetermine)
        a unique linear mapping.
        To allow translation, include a constant 1 as an input coordinate.
        with an unknown linear relationship to input coordinates.
        that should be linearly combined to calculate each of the
        output coordinates.
        To allow translation, include a constant 1.
        
        Parameters
        -----------
        out : Double1D
            A set of observed output coordinates
        ins : Double1D
            A set of observed input coordinates
        """

    def get(self, ins: Double1D) -> Double1D:
        """
        For a given set of input coordinates,
        return the linearly predicted output coordinates.
        
        Parameters
        -----------
        ins : Double1D
            A set of input coordinates
        
        Returns
        --------
        output : Double1D
            A computed set of output coordinates.
        """
