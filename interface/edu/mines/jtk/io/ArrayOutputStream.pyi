from typing import overload
from edu.mines.jtk.mapping import *
from java.nio import ByteOrder


class ArrayOutputStream:
    """
    An output stream that implements {@link ArrayOutput}.
    @author Dave Hale, Colorado School of Mines
    @version 2006.08.05
    """

    @overload
    def __init__(self, os: OutputStream) -> None:
        """
        Constructs an array output stream for the specified stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        ----------
        os : OutputStream
            The description of OutputStream.
        """

    @overload
    def __init__(self, fos: FileOutputStream) -> None:
        """
        Constructs an array output stream for the specified file output stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        ----------
        fos : FileOutputStream
            The description of FileOutputStream.
        """

    @overload
    def __init__(self, name: str) -> None:
        """
        Constructs an array output stream for the specified file name.
        The default byte order is BIG_ENDIAN.

        Parameters
        -----------
        name : str
            the file name
        """

    @overload
    def __init__(self, file: File) -> None:
        """
        Constructs an array output stream for the specified file.
        The default byte order is BIG_ENDIAN.

        Parameters
        -----------
        file : File
            The file
        """

    @overload
    def __init__(self, os: OutputStream, bo: ByteOrder) -> None:
        """
        Constructs an array output stream for the specified stream and byte order.
        
        Parameters
        ----------
        os : OutputStream
            the output stream.
        bo : ByteOrder
            The description of ByteOrder.
        """

    @overload
    def __init__(self, name: str, bo: ByteOrder) -> None:
        """
        Constructs an array output stream for the specified file name
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
        Constructs an array output stream for the specified file name
        and byte order.

        The default byte order is BIG_ENDIAN.

        Parameters
        ----------
        file : File
            the file
        bo : ByteOrder
            The description of ByteOrder.
        """

    def close(self) -> None:
        """
        Closes this array output stream.
        """

    def getByteOrder(self) -> ByteOrder:
        """
        Gets the byte order for this stream.
        
        Parameters
        ----------
        
        Returns
        -------
        output : ByteOrder
            the byte order.
        """

    @overload
    def writeBytes(self, v: Byte1D, k: int, n: int) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        ----------
        v : Byte1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            The description of int.
        """

    @overload
    def writeBytes(self, v: Byte1D) -> None:
        """
        Writes byte elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        ----------
        v : Byte1D
            The description of Byte1D.
        """

    @overload
    def writeBytes(self, v: Byte2D) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        ----------
        v : Byte2D
            The description of Byte2D.
        """

    @overload
    def writeBytes(self, v: Byte3D) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        ----------
        v : Byte3D
            The description of Byte3D.
        """

    @overload
    def writeChars(self, v: Char1D, k: int, n: int) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        ----------
        v : Char1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            The description of int.
        """

    @overload
    def writeChars(self, v: Char1D) -> None:
        """
        Writes char elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        ----------
        v : Char1D
            The description of Char1D.
        """

    @overload
    def writeChars(self, v: Char2D) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        ----------
        v : Char2D
            The description of Char2D.
        """

    @overload
    def writeChars(self, v: Char3D) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        ----------
        v : Char3D
            The description of Char3D.
        """

    @overload
    def writeShorts(self, v: Short1D, k: int, n: int) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        ----------
        v : Short1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            The description of int.
        """

    @overload
    def writeShorts(self, v: Short1D) -> None:
        """
        Writes shorts elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        ----------
        v : Short1D
            The description of Short1D.
        """

    @overload
    def writeShorts(self, v: Short2D) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        ----------
        v : Short2D
            The description of Short2D.
        """

    @overload
    def writeShorts(self, v: Short3D) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        ----------
        v : Short3D
            The description of Short3D.
        """

    @overload
    def writeInts(self, v: Int1D, k: int, n: int) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        ----------
        v : Int1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            The description of int.
        """

    @overload
    def writeInts(self, v: Int1D) -> None:
        """
        Writes int elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        ----------
        v : Int1D
            The description of Int1D.
        """

    @overload
    def writeInts(self, v: Int2D) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        ----------
        v : Int2D
            The description of Int2D.
        """

    @overload
    def writeInts(self, v: Int3D) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        ----------
        v : Int3D
            The description of Int3D.
        """

    @overload
    def writeLongs(self, v: Long1D, k: int, n: int) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        ----------
        v : Long1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            The description of int.
        """

    @overload
    def writeLongs(self, v: Long1D) -> None:
        """
        Writes long elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        ----------
        v : Long1D
            The description of Long1D.
        """

    @overload
    def writeLongs(self, v: Long2D) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        ----------
        v : Long2D
            The description of Long2D.
        """

    @overload
    def writeLongs(self, v: Long3D) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        ----------
        v : Long3D
            The description of Long3D.
        """

    @overload
    def writeFloats(self, v: Float1D, k: int, n: int) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        ----------
        v : Float1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            The description of int.
        """

    @overload
    def writeFloats(self, v: Float1D) -> None:
        """
        Writes float elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        ----------
        v : Float1D
            The description of Float1D.
        """

    @overload
    def writeFloats(self, v: Float2D) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        ----------
        v : Float2D
            The description of Float2D.
        """

    @overload
    def writeFloats(self, v: Float3D) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        ----------
        v : Float3D
            The description of Float3D.
        """

    @overload
    def writeDoubles(self, v: Double1D, k: int, n: int) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        ----------
        v : Double1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            The description of int.
        """

    @overload
    def writeDoubles(self, v: Double1D) -> None:
        """
        Writes double elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        ----------
        v : Double1D
            The description of Double1D.
        """

    @overload
    def writeDoubles(self, v: Double2D) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        ----------
        v : Double2D
            The description of Double2D.
        """

    @overload
    def writeDoubles(self, v: Double3D) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        ----------
        v : Double3D
            The description of Double3D.
        """
