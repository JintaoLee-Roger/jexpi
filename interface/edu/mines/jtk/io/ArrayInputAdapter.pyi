from typing import overload
from edu.mines.jtk.mapping import *
from java.nio import *


class ArrayInputAdapter:
    """
    Implements {@link ArrayInput} by wrapping {@link java.io.DataInput}.
    This adapter wraps a specified data input to provide methods for reading
    values and arrays of values with an optionally specified byte order.
    
    Byte order should rarely be specified. Most applications should simply
    use the default BIG_ENDIAN byte order.
    
    When an adapter is constructed from an object that has a file channel,
    the channel enables more efficient reads of arrays of values.
    """

    @overload
    def __init__(self, input: DataInput) -> None:
        """
        Constructs an adapter for the specified data input.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        input : DataInput
            the data input.
        """

    @overload
    def __init__(self, file: RandomAccessFile) -> None:
        """
        Constructs an adapter for the specified random-access file.
        The file channel of the random-access file enables more efficient reads.
        
        Parameters
        -----------
        file : RandomAccessFile
            the random-access file.
        """

    @overload
    def __init__(self, stream: FileInputStream) -> None:
        """
        Constructs an adapter for the specified file input stream and byte order.
        The file channel of the file input stream enables more efficient reads.
        
        Parameters
        -----------
        stream : FileInputStream
            the file input stream.
        """

    @overload
    def __init__(self, input: DataInput, order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified data input and byte order.
        
        Parameters
        -----------
        input : DataInput
            the data input.
        order : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, file: RandomAccessFile, order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified random-access file and byte order.
        The file channel of the random-access file enables more efficient reads.
        
        Parameters
        -----------
        file : RandomAccessFile
            the random-access file.
        order : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, stream: FileInputStream, order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified file input stream and byte order.
        The file channel of the file input stream enables more efficient reads.
        
        Parameters
        -----------
        stream : FileInputStream
            the file input stream.
        order : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, channel: ReadableByteChannel, input: DataInput,
                 order: ByteOrder) -> None:
        """
        Constructs an adapter for the specified channel, input, and byte order.
        If not null, the readable byte channel enables more efficient reads.
        
        Parameters
        -----------
        channel : ReadableByteChannel
            the readable byte channel; null, if none.
        input : DataInput
            the data input.
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
    def readFully(self, b: Byte1D) -> None:
        """
    
        """

    @overload
    def readFully(self, b: Byte1D, off: int, len: int) -> None:
        """
    
        """

    def skipBytes(self, n: int) -> int:
        """
    
        """

    def readBoolean(self) -> bool:
        """
    
        """

    def readByte(self) -> byte:
        """
    
        """

    def readUnsignedByte(self) -> int:
        """
    
        """

    def readShort(self) -> short:
        """
    
        """

    def readUnsignedShort(self) -> int:
        """
    
        """

    def readChar(self) -> char:
        """
    
        """

    def readInt(self) -> int:
        """
    
        """

    def readLong(self) -> long:
        """
    
        """

    def readFloat(self) -> float:
        """
    
        """

    def readDouble(self) -> double:
        """
    
        """

    def readLine(self) -> String:
        """
    
        """

    def readUTF(self) -> String:
        """
    
        """

    @overload
    def readBytes(self, v: Byte1D, k: int, n: int) -> None:
        """
        Reads byte elements into a specified array.
        
        Parameters
        -----------
        v : Byte1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            the number of elements to read.
        """

    @overload
    def readBytes(self, v: Byte1D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Byte1D
            the array.
        """

    @overload
    def readBytes(self, v: Byte2D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Byte2D
            the array.
        """

    @overload
    def readBytes(self, v: Byte3D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Byte3D
            the array.
        """

    @overload
    def readChars(self, v: Char1D, k: int, n: int) -> None:
        """
        Reads char elements into a specified array.
        
        Parameters
        -----------
        v : Char1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            the number of elements to read.
        """

    @overload
    def readChars(self, v: Char1D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Char1D
            the array.
        """

    @overload
    def readChars(self, v: Char2D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Char2D
            the array.
        """

    @overload
    def readChars(self, v: Char3D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Char3D
            the array.
        """

    @overload
    def readShorts(self, v: Short1D, k: int, n: int) -> None:
        """
        Reads short elements into a specified array.
        
        Parameters
        -----------
        v : Short1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            the number of elements to read.
        """

    @overload
    def readShorts(self, v: Short1D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Short1D
            the array.
        """

    @overload
    def readShorts(self, v: Short2D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Short2D
            the array.
        """

    @overload
    def readShorts(self, v: Short3D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Short3D
            the array.
        """

    @overload
    def readInts(self, v: Int1D, k: int, n: int) -> None:
        """
        Reads int elements into a specified array.
        
        Parameters
        -----------
        v : Int1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            the number of elements to read.
        """

    @overload
    def readInts(self, v: Int1D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Int1D
            the array.
        """

    @overload
    def readInts(self, v: Int2D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Int2D
            the array.
        """

    @overload
    def readInts(self, v: Int3D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Int3D
            the array.
        """

    @overload
    def readLongs(self, v: Long1D, k: int, n: int) -> None:
        """
        Reads long elements into a specified array.
        
        Parameters
        -----------
        v : Long1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            the number of elements to read.
        """

    @overload
    def readLongs(self, v: Long1D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Long1D
            the array.
        """

    @overload
    def readLongs(self, v: Long2D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Long2D
            the array.
        """

    @overload
    def readLongs(self, v: Long3D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Long3D
            the array.
        """

    @overload
    def readFloats(self, v: Float1D, k: int, n: int) -> None:
        """
        Reads float elements into a specified array.
        
        Parameters
        -----------
        v : Float1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            the number of elements to read.
        """

    @overload
    def readFloats(self, v: Float1D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Float1D
            the array.
        """

    @overload
    def readFloats(self, v: Float2D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Float2D
            the array.
        """

    @overload
    def readFloats(self, v: Float3D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Float3D
            the array.
        """

    @overload
    def readDoubles(self, v: Double1D, k: int, n: int) -> None:
        """
        Reads double elements into a specified array.
        
        Parameters
        -----------
        v : Double1D
            the array.
        k : int
            the index of the first element to read.
        n : int
            the number of elements to read.
        """

    @overload
    def readDoubles(self, v: Double1D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Double1D
            the array.
        """

    @overload
    def readDoubles(self, v: Double2D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Double2D
            the array.
        """

    @overload
    def readDoubles(self, v: Double3D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Double3D
            the array.
        """
