from typing import overload
from edu.mines.jtk.mapping import *
from java.nio import *


class ArrayFile:
    """
    An array file expands the capabilities of {@link java.io.RandomAccessFile}.
    Specifically, an array file has methods for efficiently reading and writing
    arrays of primitive values, such as ints and floats. Also, array files may
    be read or written with either BIG_ENDIAN or LITTLE_ENDIAN byte orders.
    
    An array file implements the interfaces {@link ArrayInput} and
    {@link ArrayOutput}, which extend the standard Java interfaces
    {@link java.io.DataInput} and {@link java.io.DataOutput}, respectively.
    
    An array file can be constructed by specifying a file name and access mode
    (as for a {@link java.io.RandomAccessFile}). Alternatively, an array file
    can be constructed from an existing {@link java.io.RandomAccessFile}.
    """

    @overload
    def __init__(self, name: String, mode: String) -> None:
        """
        Constructs an array file with specified name and access mode.
        
        Parameters
        -----------
        name : String
            the file name.
        mode : String
            the access mode; "r", "rw", "rws", or "rwd".
        """

    @overload
    def __init__(self, file: File, mode: String) -> None:
        """
        Constructs an array file with specified file and access mode.
        
        Parameters
        -----------
        file : File
            the file.
        mode : String
            the access mode; "r", "rw", "rws", or "rwd".
        """

    @overload
    def __init__(self, name: String, mode: String, bor: ByteOrder,
                 bow: ByteOrder) -> None:
        """
        Constructs an array file with specified name, access mode, and byte orders.
        
        Parameters
        -----------
        name : String
            the file name.
        mode : String
            the access mode; "r", "rw", "rws", or "rwd".
        bor : ByteOrder
            the byte order for reading.
        bow : ByteOrder
            the byte order for writing.
        """

    @overload
    def __init__(self, file: File, mode: String, bor: ByteOrder,
                 bow: ByteOrder) -> None:
        """
        Constructs an array file with specified file, access mode, and byte orders.
        
        Parameters
        -----------
        file : File
            the file.
        mode : String
            the access mode; "r", "rw", "rws", or "rwd".
        bor : ByteOrder
            the byte order for reading.
        bow : ByteOrder
            the byte order for writing.
        """

    @overload
    def __init__(self, raf: RandomAccessFile, bor: ByteOrder,
                 bow: ByteOrder) -> None:
        """
        Constructs an array file for a specified random-access file
        and byte orders.
        
        Parameters
        -----------
        raf : RandomAccessFile
            the random-access file.
        bor : ByteOrder
            the byte order for reading.
        bow : ByteOrder
            the byte order for writing.
        """

    def getByteOrderRead(self) -> ByteOrder:
        """
        Gets the byte order for reading data.
        Returns
        --------
        output : ByteOrder
            the byte order.
        """

    def getByteOrderWrite(self) -> ByteOrder:
        """
        Gets the byte order for writing data.
        Returns
        --------
        output : ByteOrder
            the byte order.
        """

    @overload
    def read(self) -> int:
        """
        Reads a byte value from this file.
        The returned value will be in the range 0 to 255.
        Returns
        --------
        output : int
            the byte value.
        """

    @overload
    def read(self, b: Byte1D) -> int:
        """
        Reads up to b.length bytes from this file.
        
        Parameters
        -----------
        b : Byte1D
            array into which to read bytes.
        
        Returns
        --------
        output : int
            the number of bytes read; -1 if end of file.
        """

    @overload
    def read(self, b: Byte1D, off: int, len: int) -> int:
        """
        Reads up to len bytes from this file.
        
        Parameters
        -----------
        b : Byte1D
            array into which to read bytes.
        off : int
            array index of first byte to read.
        len : int
            the number of bytes to read.
        
        Returns
        --------
        output : int
            the number of bytes read; -1 if end of file.
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

    def getFilePointer(self) -> long:
        """
        Gets the file pointer (byte offset) for this file. The next read or
        write begins at this offset.
        Returns
        --------
        output : long
            the file pointer.
        """

    def seek(self, off: long) -> None:
        """
        Sets the file pointer (byte offset) for this file. The next read or
        or write begins at this offset.
        
        The offset may be set beyond the end of the file. Setting the offset
        beyond the end of the file does not increase the file length. The file
        length increases only by writing beyond the end of the file.
        beginning of the file.
        
        Parameters
        -----------
        off : long
            the file pointer, the offset in bytes from the
        """

    def length(self) -> long:
        """
        Returns the length of this file.
        Returns
        --------
        output : long
            the file length, in bytes.
        """

    def setLength(self, newLength: long) -> None:
        """
        Sets the length of this file. If the current file length exceeds
        the specified new length, then the file will be truncated. In this
        case, if the file pointer exceeds the new length, then that pointer
        will equal to the new length when this methods returns.
        
        If the current file length is less than the specified new length,
        then this file will extended. The content of the extended portion
        is undefined.
        
        Parameters
        -----------
        newLength : long
            the new length.
        """

    def close(self) -> None:
        """
        Closes this data file, releasing any associated system resources.
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
