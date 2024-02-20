from typing import overload
from edu.mines.jtk.mapping import *
from java.nio import ByteOrder


class ArrayInputStream:
    """
    An input stream that implements {@link ArrayInput}.
    @author Dave Hale, Colorado School of Mines
    @version 2006.08.05
    """

    @overload
    def __init__(self, ist: InputStream) -> None:
        """
        Constructs an array input stream for the specified stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        ----------
        ist : InputStream
            The description of InputStream.
        """

    @overload
    def __init__(self, fis: FileInputStream) -> None:
        """
        Constructs an array input stream for the specified file input stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        ----------
        fis : FileInputStream
            The description of FileInputStream.
        """

    @overload
    def __init__(self, name: str) -> None:
        """
        Constructs an array input stream for the specified file name.
        The default byte order is BIG_ENDIAN.

        Parameters
        -----------
        name : str
            the file name
        """

    @overload
    def __init__(self, file: File) -> None:
        """
        Constructs an array input stream for the specified file.
        The default byte order is BIG_ENDIAN.

        Parameters
        -----------
        file : File
            The file
        """

    @overload
    def __init__(self, ist: InputStream, bo: ByteOrder) -> None:
        """
        Constructs an array input stream for the specified stream and byte order.
        
        Parameters
        ----------
        is : InputStream
            the input stream.
        bo : ByteOrder
            The description of ByteOrder.
        """

    @overload
    def __init__(self, name: str, bo: ByteOrder) -> None:
        """
        Constructs an array input stream for the specified file name
        and byte order.

        The default byte order is BIG_ENDIAN.

        Parameters
        ----------
        name : str
            the file name.
        bo : ByteOrder
            The description of ByteOrder.
        """

    @overload
    def __init__(self, file: File, bo: ByteOrder) -> None:
        """
        Constructs an array input stream for the specified file name
        and byte order.

        The default byte order is BIG_ENDIAN.

        Parameters
        ----------
        file : File
            the file
        bo : ByteOrder
            The description of ByteOrder.
        """

    def flush(self) -> None:
        ...

    def close(self) -> None:
        """
        Closes this array input stream.
        """

    def getByteOrder(self) -> ByteOrder:
        """
        Gets the byte order for this stream.
        
        Returns
        ----------
        bo : ByteOrder
            the byte order.
        """

    @overload
    def readBytes(self, v: Byte1D, k: int, n: int) -> None:
        """
        Reads byte elements into a specified array.
        
        Parameters
        ----------
        v : Byte1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            The description of int.
        """

    @overload
    def readBytes(self, v: Byte1D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Byte1D
            The description of Byte1D.
        """

    @overload
    def readBytes(self, v: Byte2D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Byte2D
            The description of Byte2D.
        """

    @overload
    def readBytes(self, v: Byte3D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Byte3D
            The description of Byte3D.
        """

    @overload
    def readChars(self, v: Char1D, k: int, n: int) -> None:
        """
        Reads char elements into a specified array.
        
        Parameters
        ----------
        v : Char1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            The description of int.
        """

    @overload
    def readChars(self, v: Char1D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Char1D
            The description of Char1D.
        """

    @overload
    def readChars(self, v: Char2D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Char2D
            The description of Char2D.
        """

    @overload
    def readChars(self, v: Char3D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Char3D
            The description of Char3D.
        """

    @overload
    def readShorts(self, v: Short1D, k: int, n: int) -> None:
        """
        Reads short elements into a specified array.
        
        Parameters
        ----------
        v : Short1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            The description of int.
        """

    @overload
    def readShorts(self, v: Short1D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Short1D
            The description of Short1D.
        """

    @overload
    def readShorts(self, v: Short2D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Short2D
            The description of Short2D.
        """

    @overload
    def readShorts(self, v: Short3D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Short3D
            The description of Short3D.
        """

    @overload
    def readInts(self, v: Int1D, k: int, n: int) -> None:
        """
        Reads int elements into a specified array.
        
        Parameters
        ----------
        v : Int1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            The description of int.
        """

    @overload
    def readInts(self, v: Int1D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Int1D
            The description of Int1D.
        """

    @overload
    def readInts(self, v: Int2D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Int2D
            The description of Int2D.
        """

    @overload
    def readInts(self, v: Int3D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Int3D
            The description of Int3D.
        """

    @overload
    def readLongs(self, v: Long1D, k: int, n: int) -> None:
        """
        Reads long elements into a specified array.
        
        Parameters
        ----------
        v : Long1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            The description of int.
        """

    @overload
    def readLongs(self, v: Long1D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Long1D
            The description of Long1D.
        """

    @overload
    def readLongs(self, v: Long2D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Long2D
            The description of Long2D.
        """

    @overload
    def readLongs(self, v: Long3D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Long3D
            The description of Long3D.
        """

    @overload
    def readFloats(self, v: Float1D, k: int, n: int) -> None:
        """
        Reads float elements into a specified array.
        
        Parameters
        ----------
        v : Float1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            The description of int.
        """

    @overload
    def readFloats(self, v: Float1D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Float1D
            The description of Float1D.
        """

    @overload
    def readFloats(self, v: Float2D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Float2D
            The description of Float2D.
        """

    @overload
    def readFloats(self, v: Float3D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Float3D
            The description of Float3D.
        """

    @overload
    def readDoubles(self, v: Double1D, k: int, n: int) -> None:
        """
        Reads double elements into a specified array.
        
        Parameters
        ----------
        v : Double1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            The description of int.
        """

    @overload
    def readDoubles(self, v: Double1D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Double1D
            The description of Double1D.
        """

    @overload
    def readDoubles(self, v: Double2D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Double2D
            The description of Double2D.
        """

    @overload
    def readDoubles(self, v: Double3D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        ----------
        v : Double3D
            The description of Double3D.
        """
