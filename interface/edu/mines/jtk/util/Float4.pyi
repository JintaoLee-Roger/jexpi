from typing import overload
from edu.mines.jtk.mapping import *


class Float4:
    """
    A generic interface for a 4-D array of floats. This interface enables
    getting and setting 1-, 2-, 3- and 4-D subarrays (slices) of elements
    from any data structure that can be indexed like a 4-D array. Unlike
    a 4-D array, that data structure need not reside entirely in memory.
    
    Logically, the 4-D array can be considered as float a[n4][n3][n2][n1],
    where n1 is the fastest array dimension, and n4 is the slowest.
    """

    def getN1(self) -> int:
        """
        Gets the number of elements in 1st dimension of this array.
        Returns
        --------
        output : int
            the number of elements in 1st dimension.
        """

    def getN2(self) -> int:
        """
        Gets the number of elements in 2nd dimension of this array.
        Returns
        --------
        output : int
            the number of elements in 2nd dimension.
        """

    def getN3(self) -> int:
        """
        Gets the number of elements in 3rd dimension of this array.
        Returns
        --------
        output : int
            the number of elements in 3rd dimension.
        """

    def getN4(self) -> int:
        """
        Gets the number of elements in 4th dimension of this array.
        Returns
        --------
        output : int
            the number of elements in 4th dimension.
        """

    def get1(self, m1: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Gets the specified subarray of elements into the specified 1-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m1] of elements of the specified subarray.
        """

    def get2(self, m2: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Gets the specified subarray of elements into the specified 1-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m2] of elements of the specified subarray.
        """

    def get3(self, m3: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Gets the specified subarray of elements into the specified 1-D array.
        
        Parameters
        -----------
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m3] of elements of the specified subarray.
        """

    def get4(self, m4: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Gets the specified subarray of elements into the specified 1-D array.
        
        Parameters
        -----------
        m4 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m4] of elements of the specified subarray.
        """

    def get12(self, m1: int, m2: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Gets the specified subarray of elements into the specified 2-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m2][m1] of elements of the specified subarray.
        """

    def get13(self, m1: int, m3: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Gets the specified subarray of elements into the specified 2-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m3][m1] of elements of the specified subarray.
        """

    def get14(self, m1: int, m4: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Gets the specified subarray of elements into the specified 2-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m4 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m4][m1] of elements of the specified subarray.
        """

    def get23(self, m2: int, m3: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Gets the specified subarray of elements into the specified 2-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m3][m2] of elements of the specified subarray.
        """

    def get24(self, m2: int, m4: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Gets the specified subarray of elements into the specified 2-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        m4 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m4][m2] of elements of the specified subarray.
        """

    def get123(self, m1: int, m2: int, m3: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Gets the specified subarray of elements into the specified 3-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m3][m2][m1] of elements of the specified subarray.
        """

    def get124(self, m1: int, m2: int, m4: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Gets the specified subarray of elements into the specified 3-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m4][m2][m1] of elements of the specified subarray.
        """

    def get134(self, m1: int, m3: int, m4: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Gets the specified subarray of elements into the specified 3-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m4][m3][m1] of elements of the specified subarray.
        """

    def get234(self, m2: int, m3: int, m4: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Gets the specified subarray of elements into the specified 3-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m4][m3][m2] of elements of the specified subarray.
        """

    @overload
    def get1234(self, m1: int, m2: int, m3: int, m4: int, j1: int, j2: int,
                j3: int, j4: int, s: Float4D) -> None:
        """
        Gets the specified subarray of elements into the specified 4-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float4D
            array[m4][m3][m2][m1] of elements of the specified subarray.
        """

    @overload
    def get1234(self, m1: int, m2: int, m3: int, m4: int, j1: int, j2: int,
                j3: int, j4: int, s: Float1D) -> None:
        """
        Gets the specified subarray of elements into the specified 1-D array.
        The length of the array must be at least m1m2m3m4.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m1m2m3m4] of elements of the specified subarray.
        """

    def set1(self, m1: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Sets the specified subarray of elements from the specified 1-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m1] of elements of the specified subarray.
        """

    def set2(self, m2: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Sets the specified subarray of elements from the specified 1-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m2] of elements of the specified subarray.
        """

    def set3(self, m3: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Sets the specified subarray of elements from the specified 1-D array.
        
        Parameters
        -----------
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m3] of elements of the specified subarray.
        """

    def set4(self, m4: int, j1: int, j2: int, j3: int, j4: int,
             s: Float1D) -> None:
        """
        Sets the specified subarray of elements from the specified 1-D array.
        
        Parameters
        -----------
        m4 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m4] of elements of the specified subarray.
        """

    def set12(self, m1: int, m2: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Sets the specified subarray of elements from the specified 2-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m2][m1] of elements of the specified subarray.
        """

    def set13(self, m1: int, m3: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Sets the specified subarray of elements from the specified 2-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m3][m1] of elements of the specified subarray.
        """

    def set14(self, m1: int, m4: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Sets the specified subarray of elements from the specified 2-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m4 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m4][m1] of elements of the specified subarray.
        """

    def set23(self, m2: int, m3: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Sets the specified subarray of elements from the specified 2-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m3][m2] of elements of the specified subarray.
        """

    def set24(self, m2: int, m4: int, j1: int, j2: int, j3: int, j4: int,
              s: Float2D) -> None:
        """
        Sets the specified subarray of elements from the specified 2-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        m4 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float2D
            array[m4][m2] of elements of the specified subarray.
        """

    def set123(self, m1: int, m2: int, m3: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Sets the specified subarray of elements from the specified 3-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m3][m2][m1] of elements of the specified subarray.
        """

    def set124(self, m1: int, m2: int, m4: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Sets the specified subarray of elements from the specified 3-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m4][m2][m1] of elements of the specified subarray.
        """

    def set134(self, m1: int, m3: int, m4: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Sets the specified subarray of elements from the specified 3-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m4][m3][m1] of elements of the specified subarray.
        """

    def set234(self, m2: int, m3: int, m4: int, j1: int, j2: int, j3: int,
               j4: int, s: Float3D) -> None:
        """
        Sets the specified subarray of elements from the specified 3-D array.
        
        Parameters
        -----------
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float3D
            array[m4][m3][m2] of elements of the specified subarray.
        """

    @overload
    def set1234(self, m1: int, m2: int, m3: int, m4: int, j1: int, j2: int,
                j3: int, j4: int, s: Float4D) -> None:
        """
        Sets the specified subarray of elements from the specified 4-D array.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float4D
            array[m4][m3][m2][m1] of elements of the specified subarray.
        """

    @overload
    def set1234(self, m1: int, m2: int, m3: int, m4: int, j1: int, j2: int,
                j3: int, j4: int, s: Float1D) -> None:
        """
        Sets the specified subarray of elements from the specified 1-D array.
        The length of the array must be at least m1m2m3m4.
        
        Parameters
        -----------
        m1 : int
            number of elements in 1st dimension of subarray.
        m2 : int
            number of elements in 2nd dimension of subarray.
        m3 : int
            number of elements in 3rd dimension of subarray.
        m4 : int
            number of elements in 4th dimension of subarray.
        j1 : int
            index of first element in 1st dimension of subarray.
        j2 : int
            index of first element in 2nd dimension of subarray.
        j3 : int
            index of first element in 3rd dimension of subarray.
        j4 : int
            index of first element in 4th dimension of subarray.
        s : Float1D
            array[m1m2m3m4] of elements of the specified subarray.
        """
