from typing import overload
from edu.mines.jtk.mapping import *
from java.nio import *


class ArrayOutputAdapter:
    """
    Implements {@link ArrayOutput} by wrapping {@link java.io.DataOutput}.
    This adapter wraps a specified data output to provide methods for writing
    values and arrays of values with an optionally specified byte order.
    
    Byte order should rarely be specified. Most applications should simply
    use the default BIG_ENDIAN byte order.
    
    When an adapter is constructed from an object that has a file channel,
    the channel enables more efficient writes of arrays of values.
    """

    @overload
    def __init__(self, output: DataOutput) -> None:
        """
        Constructs an adapter for the specified data output.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        output : DataOutput
            the data output.
        """

    @overload
    def __init__(self, file: RandomAccessFile) -> None:
        """
        Constructs an adapter for the specified random-access file.
        The file channel of the random-access file enables more efficient writes.
        
        Parameters
        -----------
        file : RandomAccessFile
            the random-access file.
        """

    @overload
    def __init__(self, stream: FileOutputStream) -> None:
        """
        Constructs an adapter for the specified file output stream and byte order.
        The file channel of the file output stream enables more efficient writes.
        
        Parameters
        -----------
        stream : FileOutputStream
            the file output stream.
        """

    @overload
    def __init__(self, output: DataOutput, order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified data output and byte order.
        
        Parameters
        -----------
        output : DataOutput
            the data output.
        order : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, file: RandomAccessFile, order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified random-access file and byte order.
        The file channel of the random-access file enables more efficient writes.
        
        Parameters
        -----------
        file : RandomAccessFile
            the random-access file.
        order : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, stream: FileOutputStream, order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified file output stream and byte order.
        The file channel of the file output stream enables more efficient writes.
        
        Parameters
        -----------
        stream : FileOutputStream
            the file output stream.
        order : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, channel: WritableByteChannel, output: DataOutput,
                 order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified channel, output, and byte order.
        If not null, the writable byte channel enables more efficient writes.
        
        Parameters
        -----------
        channel : WritableByteChannel
            the writable byte channel; null, if none.
        output : DataOutput
            the data output.
        order : ByteOrder
            the byte order.
        """

    def getByteOrder(self) -> ByteOrder:
        """
        Gets the byte order for this adapter.
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
