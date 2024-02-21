from typing import overload
from edu.mines.jtk.mapping import *


class DMatrix:
    """
    A double-precision matrix.
    Matrix elements are stored in an array of arrays of doubles a[m][n],
    such that array element a[i][j] corresponds to the i'th row and the
    j'th column of the m-by-n matrix.
    
    This class was adapted from the package Jama, which was developed by
    Joe Hicklin, Cleve Moler, and Peter Webb of The MathWorks, Inc., and by
    Ronald Boisvert, Bruce Miller, Roldan Pozo, and Karin Remington of the
    National Institue of Standards and Technology.
    """

    @overload
    def __init__(self, m: int, n: int) -> None:
        """
        Constructs an m-by-n matrix of zeros.
        
        Parameters
        -----------
        m : int
            the number of rows.
        n : int
            the number of columns.
        """

    @overload
    def __init__(self, m: int, n: int, v: double) -> None:
        """
        Constructs an m-by-n matrix filled with the specified value.
        
        Parameters
        -----------
        m : int
            the number of rows.
        n : int
            the number of columns.
        v : double
            the value.
        """

    @overload
    def __init__(self, a: Double2D) -> None:
        """
        Constructs a matrix from the specified array. Does not copy array
        elements into a new array. Rather, the new matrix simply references
        the specified array.
        
        The specified array must be regular. That is, each row much contain
        the same number of columns, and each column must contain the same
        number of rows.
        
        Parameters
        -----------
        a : Double2D
            the array.
        """

    @overload
    def __init__(self, a: DMatrix) -> None:
        """
        Constructs a copy of the specified matrix.
        
        Parameters
        -----------
        a : DMatrix
            the matrix.
        """

    @overload
    def __init__(self, m: int, n: int, a: Double2D) -> None:
        """
        Constructs a matrix quickly without checking arguments. Does not
        copy array elements into a new array. Rather, the new matrix simply
        references the specified array.
        
        Parameters
        -----------
        m : int
            the number of rows.
        n : int
            the number of columns.
        a : Double2D
            the array.
        """

    def getM(self) -> int:
        """
        Gets the number of rows in this matrix.
        Returns
        --------
        output : int
            the number of rows.
        """

    def getRowCount(self) -> int:
        """
        Gets the number of rows in this matrix.
        Returns
        --------
        output : int
            the number of rows.
        """

    def getN(self) -> int:
        """
        Gets the number of columns in this matrix.
        Returns
        --------
        output : int
            the number of columns.
        """

    def getColumnCount(self) -> int:
        """
        Gets the number of columns in this matrix.
        Returns
        --------
        output : int
            the number of columns.
        """

    def getArray(self) -> Double2D:
        """
        Gets the array in which matrix elements are stored.
        Returns
        --------
        output : Double2D
            the array; by reference, not by copy.
        """

    def isSquare(self) -> bool:
        """
        Determines whether this matrix is square.
        Returns
        --------
        output : bool
            true, if square; false, otherwise.
        """

    def isSymmetric(self) -> bool:
        """
        Determines whether this matrix is symmetric (and square).
        Returns
        --------
        output : bool
            true, if symmetric (and square); false, otherwise.
        """

    @overload
    def get(self) -> Double2D:
        """
        Gets all elements of this matrix into a new array.
        Returns
        --------
        output : Double2D
            the array.
        """

    @overload
    def get(self, a: Double2D) -> None:
        """
        Gets all elements of this matrix into the specified array.
        
        Parameters
        -----------
        a : Double2D
            the array.
        """

    @overload
    def get(self, i: int, j: int) -> double:
        """
        Gets a matrix element.
        
        Parameters
        -----------
        i : int
            the row index.
        j : int
            the column index.
        
        Returns
        --------
        output : double
            the element.
        """

    @overload
    def get(self, i0: int, i1: int, j0: int, j1: int) -> DMatrix:
        """
        Gets the specified submatrix a[i0:i1][j0:j1] of this matrix.
        
        Parameters
        -----------
        i0 : int
            the index of first row.
        i1 : int
            the index of last row.
        j0 : int
            the index of first column.
        j1 : int
            the index of last column.
        
        Returns
        --------
        output : DMatrix
            the submatrix.
        """

    @overload
    def get(self, r: Int1D, c: Int1D) -> DMatrix:
        """
        Gets a new matrix from the specified rows and columns of this matrix.
        
        Parameters
        -----------
        r : Int1D
            the array of row indices; null, for all rows.
        c : Int1D
            the array of column indices; null, for all columns.
        
        Returns
        --------
        output : DMatrix
            the matrix.
        """

    @overload
    def get(self, i: int, c: Int1D) -> DMatrix:
        """
        Gets a matrix from specified one row and columns of this matrix.
        
        Parameters
        -----------
        i : int
            the row index.
        c : Int1D
            the array of column indices; null, for all columns.
        
        Returns
        --------
        output : DMatrix
            the matrix.
        """

    @overload
    def get(self, r: Int1D, j: int) -> DMatrix:
        """
        Gets a matrix from specified rows and one column of this matrix.
        
        Parameters
        -----------
        r : Int1D
            the array of row indices; null, for all rows.
        j : int
            the column index.
        
        Returns
        --------
        output : DMatrix
            the matrix.
        """

    @overload
    def get(self, i0: int, i1: int, c: Int1D) -> DMatrix:
        """
        Gets a matrix from specified rows and columns of this matrix.
        
        Parameters
        -----------
        i0 : int
            the index of the first row.
        i1 : int
            the index of the last row.
        c : Int1D
            the array of column indices; null, for all columns.
        
        Returns
        --------
        output : DMatrix
            the matrix.
        """

    @overload
    def get(self, r: Int1D, j0: int, j1: int) -> DMatrix:
        """
        Gets a matrix from specified rows and columns of this matrix.
        
        Parameters
        -----------
        r : Int1D
            the array of row indices; null, for all rows.
        j0 : int
            the index of the first column.
        j1 : int
            the index of the last column.
        
        Returns
        --------
        output : DMatrix
            the matrix.
        """

    def getPackedColumns(self) -> Double1D:
        """
        Gets the elements of this matrix packed by columns.
        Returns
        --------
        output : Double1D
            the array of matrix elements packed by columns.
        """

    def getPackedRows(self) -> Double1D:
        """
        Gets the elements of this matrix packed by rows.
        Returns
        --------
        output : Double1D
            the array of matrix elements packed by rows.
        """

    @overload
    def set(self, a: Double2D) -> None:
        """
        Sets all elements of this matrix from the specified array.
        Copies each array element into this matrix.
        
        Parameters
        -----------
        a : Double2D
            the array.
        """

    @overload
    def set(self, i: int, j: int, v: double) -> None:
        """
        Sets a matrix element.
        
        Parameters
        -----------
        i : int
            the row index.
        j : int
            the column index.
        v : double
            the element value.
        """

    @overload
    def set(self, i0: int, i1: int, j0: int, j1: int, x: DMatrix) -> None:
        """
        Sets the specified submatrix a[i0:i1][j0:j1] of this matrix.
        
        Parameters
        -----------
        i0 : int
            the index of first row.
        i1 : int
            the index of last row.
        j0 : int
            the index of first column.
        j1 : int
            the index of last column.
        x : DMatrix
            the matrix from which to copy elements.
        """

    @overload
    def set(self, r: Int1D, c: Int1D, x: DMatrix) -> None:
        """
        Sets the specified rows and columns of this matrix.
        
        Parameters
        -----------
        r : Int1D
            the array of row indices; null, for all rows.
        c : Int1D
            the array of column indices; null, for all columns.
        x : DMatrix
            the matrix from which to copy elements.
        """

    @overload
    def set(self, i: int, c: Int1D, x: DMatrix) -> None:
        """
        Sets the specified one row and columns of this matrix.
        
        Parameters
        -----------
        i : int
            the row index.
        c : Int1D
            the array of column indices; null, for all columns.
        x : DMatrix
            the matrix from which to copy elements.
        """

    @overload
    def set(self, r: Int1D, j: int, x: DMatrix) -> None:
        """
        Sets the specified rows and one column of this matrix.
        
        Parameters
        -----------
        r : Int1D
            the array of row indices; null, for all rows.
        j : int
            the column index.
        x : DMatrix
            the matrix from which to copy elements.
        """

    @overload
    def set(self, i0: int, i1: int, c: Int1D, x: DMatrix) -> None:
        """
        Sets the specified rows and columns of this matrix.
        
        Parameters
        -----------
        i0 : int
            the index of the first row.
        i1 : int
            the index of the last row.
        c : Int1D
            the array of column indices; null, for all columns.
        x : DMatrix
            the matrix from which to copy elements.
        """

    @overload
    def set(self, r: Int1D, j0: int, j1: int, x: DMatrix) -> None:
        """
        Sets the specified rows and columns of this matrix.
        
        Parameters
        -----------
        r : Int1D
            the array of row indices; null, for all rows.
        j0 : int
            the index of the first column.
        j1 : int
            the index of the last column.
        x : DMatrix
            the matrix from which to copy elements.
        """

    def setPackedColumns(self, c: Double1D) -> None:
        """
        Sets the elements of this matrix from an array packed by columns.
        
        Parameters
        -----------
        c : Double1D
            the array of matrix elements packed by columns.
        """

    def setPackedRows(self, r: Double1D) -> None:
        """
        Sets the elements of this matrix from an array packed by rows.
        
        Parameters
        -----------
        r : Double1D
            the array of matrix elements packed by rows.
        """

    def transpose(self) -> DMatrix:
        """
        Returns the transpose of this matrix.
        Returns
        --------
        output : DMatrix
            the transpose.
        """

    def norm1(self) -> double:
        """
        Returns the one-norm (maximum column sum) of this matrix.
        Returns
        --------
        output : double
            the one-norm.
        """

    def norm2(self) -> double:
        """
        Returns the two-norm (maximum singular value) of this matrix.
        Returns
        --------
        output : double
            the two-norm.
        """

    def normI(self) -> double:
        """
        Returns the infinity-norm (maximum row sum) of this matrix.
        Returns
        --------
        output : double
            the infinity-norm.
        """

    def normF(self) -> double:
        """
        Returns the Frobenius norm (sqrt of sum of squares) of this matrix.
        Returns
        --------
        output : double
            the Frobenius norm.
        """

    def negate(self) -> DMatrix:
        """
        Returns C = -A, where A is this matrix.
        Returns
        --------
        output : DMatrix
            C = -A.
        """

    def plus(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A + B, where A is this matrix.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A + B.
        """

    def plusEquals(self, b: DMatrix) -> DMatrix:
        """
        Returns A = A + B, where A is this matrix.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            A = A + B.
        """

    def minus(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A - B, where A is this matrix.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A - B.
        """

    def minusEquals(self, b: DMatrix) -> DMatrix:
        """
        Returns A = A - B, where A is this matrix.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            A = A - B.
        """

    def arrayTimes(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A . B, where A is this matrix.
        The symbol . denotes element-by-element multiplication.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A . B.
        """

    def arrayTimesEquals(self, b: DMatrix) -> DMatrix:
        """
        Returns A = A . B, where A is this matrix.
        The symbol . denotes element-by-element multiplication.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            A = A . B.
        """

    def arrayRightDivide(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A ./ B, where A is this matrix.
        The symbol ./ denotes element-by-element right division.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A ./ B.
        """

    def arrayRightDivideEquals(self, b: DMatrix) -> DMatrix:
        """
        Returns A = A ./ B, where A is this matrix.
        The symbol ./ denotes element-by-element right division.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            A = A ./ B.
        """

    def arrayLeftDivide(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A .\ B, where A is this matrix.
        The symbol .\ denotes element-by-element left division.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A .\ B.
        """

    def arrayLeftDivideEquals(self, b: DMatrix) -> DMatrix:
        """
        Returns A = A .\ B, where A is this matrix.
        The symbol .\ denotes element-by-element left division.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            A = A .\ B.
        """

    @overload
    def times(self, s: double) -> DMatrix:
        """
        Returns C = A  s, where A is this matrix, and s is a scalar.
        
        Parameters
        -----------
        s : double
            the scalar s.
        
        Returns
        --------
        output : DMatrix
            C = A  s.
        """

    def timesEquals(self, s: double) -> DMatrix:
        """
        Returns A = A  s, where A is this matrix, and s is a scalar.
        
        Parameters
        -----------
        s : double
            the scalar s.
        
        Returns
        --------
        output : DMatrix
            A = A  s.
        """

    @overload
    def times(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A  B, where A is this matrix. The number of columns in
        this matrix A must equal the number of rows in the specified matrix B.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A  B.
        """

    def trace(self) -> double:
        """
        Returns the trace (sum of diagonal elements) of this matrix.
        Returns
        --------
        output : double
            the trace.
        """

    @staticmethod
    def random(self, m: int, n: int) -> DMatrix:
        """
        Returns a new matrix with random elements. The distribution of the
        random numbers is uniform in the interval [0,1).
        
        Parameters
        -----------
        m : int
            the number of rows.
        n : int
            the number of columns.
        
        Returns
        --------
        output : DMatrix
            the random matrix.
        """

    @staticmethod
    def identity(self, m: int, n: int) -> DMatrix:
        """
        Returns a new identity matrix.
        
        Parameters
        -----------
        m : int
            the number of rows.
        n : int
            the number of columns.
        
        Returns
        --------
        output : DMatrix
            the identity matrix.
        """

    def equals(self, obj: Object) -> bool:
        """
    
        """

    def hashCode(self) -> int:
        """
    
        """

    def toString(self) -> String:
        """
    
        """
