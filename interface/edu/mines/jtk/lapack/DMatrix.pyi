from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.lapack import *


class DMatrix:
    """
    A double-precision matrix.
    Elements of an m-by-n matrix are stored contiguously in an array a[mn],
    such that array element a[i+jm] corresponds to the i'th row and the
    j'th column of the m-by-n matrix. For example, a 3-by-3 matrix is stored
    as:
    <pre><code>
    a[0] a[3] a[6]
    a[1] a[4] a[7]
    a[2] a[5] a[8]
    </code></pre>
    This is the column-major order required by LAPACK.
    
    Decompositions of a matrix A facilate the solutions of various problems.
    For example, the QR decomposition A = QR of a rectangular matrix A
    (where Q is orthogonal and R is upper right triangular) is useful in
    least-square approximations. Decompositions currently provided by this
    class include
    <ul>
    <li>LU decomposition of rectangular matrices</li>
    <li>QR decomposition of rectangular matrices</li>
    <li>singular value decomposition of rectangular matrices</li>
    <li>eigenvalue and eigenvector decomposition of square matrices</li>
    <li>Cholesky decomposition of symmetric positive-definite matrices</li>
    </ul>
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
    def __init__(self, m: int, n: int, a: Double1D) -> None:
        """
        Constructs a matrix from the specified array. Does not copy array
        elements into a new array. Rather, this matrix simply references
        the specified array.
        
        That array contains packed columns of this matrix. In other words,
        array element a[i+jm] corresponds to the i'th row and j'th column
        of this matrix.
        
        Parameters
        -----------
        m : int
            the number of rows.
        n : int
            the number of columns.
        a : Double1D
            the array.
        """

    @overload
    def __init__(self, a: Double2D) -> None:
        """
        Constructs a matrix from the specified array. Copies array elements
        a[i][j] to the i'th row and j'th column of this matrix. In other
        words, the specified array contains matrix elements ordered by rows.
        
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

    def getArray(self) -> Double1D:
        """
        Gets the array in which matrix elements are stored.
        Returns
        --------
        output : Double1D
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
            a matrix.
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
            a matrix.
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

    def det(self) -> double:
        """
        Returns the determinant of this matrix.
        Returns
        --------
        output : double
            the determinant.
        """

    def cond(self) -> double:
        """
        Returns the condition number of this matrix.
        Returns
        --------
        output : double
            the condition number.
        """

    def rank(self) -> double:
        """
        Returns the effective numerical rank of this matrix.
        Returns
        --------
        output : double
            the rank.
        """

    def trace(self) -> double:
        """
        Returns the trace (sum of diagonal elements) of this matrix.
        Returns
        --------
        output : double
            the trace.
        """

    def lud(self) -> DMatrixLud:
        """
        Returns the LU decomposition of this matrix.
        Returns
        --------
        output : DMatrixLud
            the LU decomposition.
        """

    def qrd(self) -> DMatrixQrd:
        """
        Returns the QR decomposition of this matrix.
        Returns
        --------
        output : DMatrixQrd
            the QR decomposition.
        """

    def chd(self) -> DMatrixChd:
        """
        Returns the Cholesky decomposition of this matrix.
        Returns
        --------
        output : DMatrixChd
            the Cholesky decomposition.
        """

    def evd(self) -> DMatrixEvd:
        """
        Returns the eigenvalue and eigenvector decomposition of this matrix.
        Returns
        --------
        output : DMatrixEvd
            the eigenvalue and eigenvector decomposition.
        """

    def svd(self) -> DMatrixSvd:
        """
        Returns the singular value decomposition of this matrix.
        Returns
        --------
        output : DMatrixSvd
            the singular value decomposition.
        """

    def solve(self, b: DMatrix) -> DMatrix:
        """
        Solves the system AX = B. Requires m&gt;=n for this m-by-n matrix A.
        If m&gt;n, then the returned solution X is a least-squares solution.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B of right-hand-side column vectors.
        
        Returns
        --------
        output : DMatrix
            the matrix X of solution vectors.
        """

    def inverse(self) -> DMatrix:
        """
        Returns the inverse of this matrix.
        If m&gt;n for this m-by-n matrix A, then returns the pseudo-inverse.
        Returns
        --------
        output : DMatrix
            the inverse matrix.
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

    def timesTranspose(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A  B', where A is this matrix and B' is B transposed.
        The number of columns in this matrix A must equal the number of
        columns in the specified matrix B.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A  B'.
        """

    def transposeTimes(self, b: DMatrix) -> DMatrix:
        """
        Returns C = A'  B, where A' is this matrix transposed.
        The number of rows in this matrix A must equal the number of
        rows in the specified matrix B.
        
        Parameters
        -----------
        b : DMatrix
            the matrix B.
        
        Returns
        --------
        output : DMatrix
            C = A'  B.
        """

    @overload
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

    @overload
    @staticmethod
    def random(self, n: int) -> DMatrix:
        """
        Returns a new square matrix with random elements. The distribution
        of the random numbers is uniform in the interval [0,1).
        
        Parameters
        -----------
        n : int
            the number of rows and columns.
        
        Returns
        --------
        output : DMatrix
            the random matrix.
        """

    @overload
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

    @overload
    @staticmethod
    def identity(self, n: int) -> DMatrix:
        """
        Returns a new square identity matrix.
        
        Parameters
        -----------
        n : int
            the number of rows and columns.
        
        Returns
        --------
        output : DMatrix
            the identity matrix.
        """

    @staticmethod
    def diagonal(self, d: Double1D) -> DMatrix:
        """
        Returns a new diagonal matrix with specified elements.
        
        Parameters
        -----------
        d : Double1D
            array of diagonal elements d[k] = A(k,k).
        
        Returns
        --------
        output : DMatrix
            the matrix.
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
