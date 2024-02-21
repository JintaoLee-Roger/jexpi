from typing import overload
from edu.mines.jtk.mapping import *
from java.nio import *


class ArrayOutputStream:
    """
    An output stream that implements {@link ArrayOutput}.
    """

    @overload
    def __init__(self, os: OutputStream) -> None:
        """
        Constructs an array output stream for the specified stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        os : OutputStream
            the output stream.
        """

    @overload
    def __init__(self, fos: FileOutputStream) -> None:
        """
        Constructs an array output stream for the specified file output stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        fos : FileOutputStream
            the file output stream.
        """

    @overload
    def __init__(self, name: String) -> None:
        """
        Constructs an array output stream for the specified file name.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        name : String
            the file name.
        """

    @overload
    def __init__(self, file: File) -> None:
        """
        Constructs an array output stream for the specified file.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        file : File
            the file.
        """

    @overload
    def __init__(self, os: OutputStream, bo: ByteOrder) -> None:
        """
        Constructs an array output stream for the specified stream and byte order.
        
        Parameters
        -----------
        os : OutputStream
            the output stream.
        bo : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, name: String, bo: ByteOrder) -> None:
        """
        Constructs an array output stream for the specified file name
        and byte order.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        name : String
            the file name.
        bo : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, file: File, bo: ByteOrder) -> None:
        """
        Constructs an array output stream for the specified file and byte order.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        file : File
            the file.
        bo : ByteOrder
            the byte order.
        """

    def flush(self) -> None:
        """
    
        """

    def close(self) -> None:
        """
        Closes this array output stream.
        """

    def getByteOrder(self) -> ByteOrder:
        """
        Gets the byte order for this stream.
        Returns
        --------
        output : ByteOrder
            the byte order.
        """

    @overload
    def write(self, b: int) -> None:
        """
    
        """

    @overload
    def write(self, b: Byte1D) -> None:
        """
    
        """

    @overload
    def write(self, b: Byte1D, off: int, len: int) -> None:
        """
    
        """

    def writeBoolean(self, v: bool) -> None:
        """
    
        """

    def writeByte(self, v: int) -> None:
        """
    
        """

    def writeShort(self, v: int) -> None:
        """
    
        """

    def writeChar(self, v: int) -> None:
        """
    
        """

    def writeInt(self, v: int) -> None:
        """
    
        """

    def writeLong(self, v: long) -> None:
        """
    
        """

    def writeFloat(self, v: float) -> None:
        """
    
        """

    def writeDouble(self, v: double) -> None:
        """
    
        """

    @overload
    def writeBytes(self, s: String) -> None:
        """
    
        """

    @overload
    def writeChars(self, s: String) -> None:
        """
    
        """

    def writeUTF(self, s: String) -> None:
        """
    
        """

    @overload
    def writeBytes(self, v: Byte1D, k: int, n: int) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        -----------
        v : Byte1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            the number of elements to write.
        """

    @overload
    def writeBytes(self, v: Byte1D) -> None:
        """
        Writes byte elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Byte1D
            the array.
        """

    @overload
    def writeBytes(self, v: Byte2D) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        -----------
        v : Byte2D
            the array.
        """

    @overload
    def writeBytes(self, v: Byte3D) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        -----------
        v : Byte3D
            the array.
        """

    @overload
    def writeChars(self, v: Char1D, k: int, n: int) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        -----------
        v : Char1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            the number of elements to write.
        """

    @overload
    def writeChars(self, v: Char1D) -> None:
        """
        Writes char elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Char1D
            the array.
        """

    @overload
    def writeChars(self, v: Char2D) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        -----------
        v : Char2D
            the array.
        """

    @overload
    def writeChars(self, v: Char3D) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        -----------
        v : Char3D
            the array.
        """

    @overload
    def writeShorts(self, v: Short1D, k: int, n: int) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        -----------
        v : Short1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            the number of elements to write.
        """

    @overload
    def writeShorts(self, v: Short1D) -> None:
        """
        Writes shorts elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Short1D
            the array.
        """

    @overload
    def writeShorts(self, v: Short2D) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        -----------
        v : Short2D
            the array.
        """

    @overload
    def writeShorts(self, v: Short3D) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        -----------
        v : Short3D
            the array.
        """

    @overload
    def writeInts(self, v: Int1D, k: int, n: int) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        -----------
        v : Int1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            the number of elements to write.
        """

    @overload
    def writeInts(self, v: Int1D) -> None:
        """
        Writes int elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Int1D
            the array.
        """

    @overload
    def writeInts(self, v: Int2D) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        -----------
        v : Int2D
            the array.
        """

    @overload
    def writeInts(self, v: Int3D) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        -----------
        v : Int3D
            the array.
        """

    @overload
    def writeLongs(self, v: Long1D, k: int, n: int) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        -----------
        v : Long1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            the number of elements to write.
        """

    @overload
    def writeLongs(self, v: Long1D) -> None:
        """
        Writes long elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Long1D
            the array.
        """

    @overload
    def writeLongs(self, v: Long2D) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        -----------
        v : Long2D
            the array.
        """

    @overload
    def writeLongs(self, v: Long3D) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        -----------
        v : Long3D
            the array.
        """

    @overload
    def writeFloats(self, v: Float1D, k: int, n: int) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        -----------
        v : Float1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            the number of elements to write.
        """

    @overload
    def writeFloats(self, v: Float1D) -> None:
        """
        Writes float elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Float1D
            the array.
        """

    @overload
    def writeFloats(self, v: Float2D) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        -----------
        v : Float2D
            the array.
        """

    @overload
    def writeFloats(self, v: Float3D) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        -----------
        v : Float3D
            the array.
        """

    @overload
    def writeDoubles(self, v: Double1D, k: int, n: int) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        -----------
        v : Double1D
            the array.
        k : int
            the index of the first element to write.
        n : int
            the number of elements to write.
        """

    @overload
    def writeDoubles(self, v: Double1D) -> None:
        """
        Writes double elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Double1D
            the array.
        """

    @overload
    def writeDoubles(self, v: Double2D) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        -----------
        v : Double2D
            the array.
        """

    @overload
    def writeDoubles(self, v: Double3D) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        -----------
        v : Double3D
            the array.
        """
