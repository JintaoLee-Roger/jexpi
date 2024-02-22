from typing import overload
from edu.mines.jtk.mapping import *


class ArrayOutput:
    """
    An interface for writing arrays of primitive values to a binary stream.
    This interfaces extends the standard interface {@link java.io.DataOutput}.
    It adds methods for writing arrays of primitive values.
    """

    @overload
    def write(b: int) -> None:
        """
    
        """

    @overload
    def write(b: Byte1D) -> None:
        """
    
        """

    @overload
    def write(b: Byte1D, off: int, len: int) -> None:
        """
    
        """

    def writeBoolean(v: bool) -> None:
        """
    
        """

    def writeByte(v: int) -> None:
        """
    
        """

    def writeShort(v: int) -> None:
        """
    
        """

    def writeChar(v: int) -> None:
        """
    
        """

    def writeInt(v: int) -> None:
        """
    
        """

    def writeLong(v: long) -> None:
        """
    
        """

    def writeFloat(v: float) -> None:
        """
    
        """

    def writeDouble(v: double) -> None:
        """
    
        """

    @overload
    def writeBytes(s: String) -> None:
        """
    
        """

    @overload
    def writeChars(s: String) -> None:
        """
    
        """

    def writeUTF(s: String) -> None:
        """
    
        """

    @overload
    def writeBytes(v: Byte1D, k: int, n: int) -> None:
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
    def writeBytes(v: Byte1D) -> None:
        """
        Writes byte elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Byte1D
            the array.
        """

    @overload
    def writeBytes(v: Byte2D) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        -----------
        v : Byte2D
            the array.
        """

    @overload
    def writeBytes(v: Byte3D) -> None:
        """
        Writes byte elements from a specified array.
        
        Parameters
        -----------
        v : Byte3D
            the array.
        """

    @overload
    def writeChars(v: Char1D, k: int, n: int) -> None:
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
    def writeChars(v: Char1D) -> None:
        """
        Writes char elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Char1D
            the array.
        """

    @overload
    def writeChars(v: Char2D) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        -----------
        v : Char2D
            the array.
        """

    @overload
    def writeChars(v: Char3D) -> None:
        """
        Writes char elements from a specified array.
        
        Parameters
        -----------
        v : Char3D
            the array.
        """

    @overload
    def writeShorts(v: Short1D, k: int, n: int) -> None:
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
    def writeShorts(v: Short1D) -> None:
        """
        Writes shorts elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Short1D
            the array.
        """

    @overload
    def writeShorts(v: Short2D) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        -----------
        v : Short2D
            the array.
        """

    @overload
    def writeShorts(v: Short3D) -> None:
        """
        Writes short elements from a specified array.
        
        Parameters
        -----------
        v : Short3D
            the array.
        """

    @overload
    def writeInts(v: Int1D, k: int, n: int) -> None:
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
    def writeInts(v: Int1D) -> None:
        """
        Writes int elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Int1D
            the array.
        """

    @overload
    def writeInts(v: Int2D) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        -----------
        v : Int2D
            the array.
        """

    @overload
    def writeInts(v: Int3D) -> None:
        """
        Writes int elements from a specified array.
        
        Parameters
        -----------
        v : Int3D
            the array.
        """

    @overload
    def writeLongs(v: Long1D, k: int, n: int) -> None:
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
    def writeLongs(v: Long1D) -> None:
        """
        Writes long elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Long1D
            the array.
        """

    @overload
    def writeLongs(v: Long2D) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        -----------
        v : Long2D
            the array.
        """

    @overload
    def writeLongs(v: Long3D) -> None:
        """
        Writes long elements from a specified array.
        
        Parameters
        -----------
        v : Long3D
            the array.
        """

    @overload
    def writeFloats(v: Float1D, k: int, n: int) -> None:
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
    def writeFloats(v: Float1D) -> None:
        """
        Writes float elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Float1D
            the array.
        """

    @overload
    def writeFloats(v: Float2D) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        -----------
        v : Float2D
            the array.
        """

    @overload
    def writeFloats(v: Float3D) -> None:
        """
        Writes float elements from a specified array.
        
        Parameters
        -----------
        v : Float3D
            the array.
        """

    @overload
    def writeDoubles(v: Double1D, k: int, n: int) -> None:
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
    def writeDoubles(v: Double1D) -> None:
        """
        Writes double elements from a specified array.
        The array length equals the number of elements to write.
        
        Parameters
        -----------
        v : Double1D
            the array.
        """

    @overload
    def writeDoubles(v: Double2D) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        -----------
        v : Double2D
            the array.
        """

    @overload
    def writeDoubles(v: Double3D) -> None:
        """
        Writes double elements from a specified array.
        
        Parameters
        -----------
        v : Double3D
            the array.
        """
