from typing import overload
from edu.mines.jtk.mapping import *
from java.nio import *


class ArrayInputStream:
    """
    An input stream that implements {@link ArrayInput}.
    """

    @overload
    def __init__(self, ist: InputStream) -> None:
        """
        Constructs an array input stream for the specified stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        is : InputStream
            the input stream.
        """

    @overload
    def __init__(self, fis: FileInputStream) -> None:
        """
        Constructs an array input stream for the specified file input stream.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        fis : FileInputStream
            the file input stream.
        """

    @overload
    def __init__(self, name: String) -> None:
        """
        Constructs an array input stream for the specified file name.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        name : String
            the file name.
        """

    @overload
    def __init__(self, file: File) -> None:
        """
        Constructs an array input stream for the specified file.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        file : File
            the file.
        """

    @overload
    def __init__(self, ist: InputStream, bo: ByteOrder) -> None:
        """
        Constructs an array input stream for the specified stream and byte order.
        
        Parameters
        -----------
        is : InputStream
            the input stream.
        bo : ByteOrder
            the byte order.
        """

    @overload
    def __init__(self, name: String, bo: ByteOrder) -> None:
        """
        Constructs an array input stream for the specified file name
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
        Constructs an array input stream for the specified file and byte order.
        The default byte order is BIG_ENDIAN.
        
        Parameters
        -----------
        file : File
            the file.
        bo : ByteOrder
            the byte order.
        """

    def close(self) -> None:
        """
        Closes this array input stream.
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
