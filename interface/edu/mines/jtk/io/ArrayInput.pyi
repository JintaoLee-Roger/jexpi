from typing import overload
from edu.mines.jtk.mapping import *


class ArrayInput:
    """
    An interface for reading arrays of primitive values from a binary stream.
    This interfaces extends the standard interface {@link java.io.DataInput}.
    It adds methods for reading arrays of primitive values.
    """

    @overload
    def readFully(b: Byte1D) -> None:
        """
    
        """

    @overload
    def readFully(b: Byte1D, off: int, len: int) -> None:
        """
    
        """

    def skipBytes(n: int) -> int:
        """
    
        """

    def readBoolean() -> bool:
        """
    
        """

    def readByte() -> byte:
        """
    
        """

    def readUnsignedByte() -> int:
        """
    
        """

    def readShort() -> short:
        """
    
        """

    def readUnsignedShort() -> int:
        """
    
        """

    def readChar() -> char:
        """
    
        """

    def readInt() -> int:
        """
    
        """

    def readLong() -> long:
        """
    
        """

    def readFloat() -> float:
        """
    
        """

    def readDouble() -> double:
        """
    
        """

    def readLine() -> String:
        """
    
        """

    def readUTF() -> String:
        """
    
        """

    @overload
    def readBytes(v: Byte1D, k: int, n: int) -> None:
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
    def readBytes(v: Byte1D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Byte1D
            the array.
        """

    @overload
    def readBytes(v: Byte2D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Byte2D
            the array.
        """

    @overload
    def readBytes(v: Byte3D) -> None:
        """
        Reads byte elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Byte3D
            the array.
        """

    @overload
    def readChars(v: Char1D, k: int, n: int) -> None:
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
    def readChars(v: Char1D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Char1D
            the array.
        """

    @overload
    def readChars(v: Char2D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Char2D
            the array.
        """

    @overload
    def readChars(v: Char3D) -> None:
        """
        Reads char elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Char3D
            the array.
        """

    @overload
    def readShorts(v: Short1D, k: int, n: int) -> None:
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
    def readShorts(v: Short1D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Short1D
            the array.
        """

    @overload
    def readShorts(v: Short2D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Short2D
            the array.
        """

    @overload
    def readShorts(v: Short3D) -> None:
        """
        Reads short elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Short3D
            the array.
        """

    @overload
    def readInts(v: Int1D, k: int, n: int) -> None:
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
    def readInts(v: Int1D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Int1D
            the array.
        """

    @overload
    def readInts(v: Int2D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Int2D
            the array.
        """

    @overload
    def readInts(v: Int3D) -> None:
        """
        Reads int elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Int3D
            the array.
        """

    @overload
    def readLongs(v: Long1D, k: int, n: int) -> None:
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
    def readLongs(v: Long1D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Long1D
            the array.
        """

    @overload
    def readLongs(v: Long2D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Long2D
            the array.
        """

    @overload
    def readLongs(v: Long3D) -> None:
        """
        Reads long elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Long3D
            the array.
        """

    @overload
    def readFloats(v: Float1D, k: int, n: int) -> None:
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
    def readFloats(v: Float1D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Float1D
            the array.
        """

    @overload
    def readFloats(v: Float2D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Float2D
            the array.
        """

    @overload
    def readFloats(v: Float3D) -> None:
        """
        Reads float elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Float3D
            the array.
        """

    @overload
    def readDoubles(v: Double1D, k: int, n: int) -> None:
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
    def readDoubles(v: Double1D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Double1D
            the array.
        """

    @overload
    def readDoubles(v: Double2D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Double2D
            the array.
        """

    @overload
    def readDoubles(v: Double3D) -> None:
        """
        Reads double elements into a specified array.
        The array length equals the number of elements to read.
        
        Parameters
        -----------
        v : Double3D
            the array.
        """
