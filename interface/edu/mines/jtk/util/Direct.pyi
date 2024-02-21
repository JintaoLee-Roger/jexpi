from typing import overload
from edu.mines.jtk.mapping import *


class Direct:
    """
    Utilities for direct (native) buffers. Unlike arrays and non-direct
    buffers that are backed by arrays, the contents of direct buffers
    cannot move during garbage-collection. This makes direct buffers
    useful in systems (e.g., OpenGL) that require native pointers to
    memory.
    
    Memory allocated for a direct buffer typically lies outside the
    garbage-collected Java heap. That memory is freed when the direct
    buffer is garbage collected. Unfortunately, garbage collection
    normally occurs when insufficient space is available <em>inside</em>
    the Java heap. If insufficient space <em>outside</em> the Java heap
    is available, then allocation of a new direct buffer may fail with
    a {@link java.lang.OutOfMemoryError}. This error may occur because
    direct buffers that are garbage have not yet been collected, perhaps
    because plenty of space is available inside the Java heap.
    
    A solution to this problem is to perform garbage collection when
    this error occurs. Normally, a {@link java.lang.OutOfMemoryError}
    is fatal. However, methods in this class that allocate direct buffers
    will catch this error and call {@link java.lang.System#gc()} before
    attempting to allocate the buffer a second time. If that second
    attempt fails, then no further attempts are made and the error is
    thrown again. There is no guarantee that this solution will work, but
    we have not yet seen it fail in tests that repeatedly allocate direct
    buffers that quickly become garbage.
    """

    @overload
    @staticmethod
    def newByteBuffer(self, capacity: int) -> ByteBuffer:
        """
        Returns a new direct byte buffer.
        
        Parameters
        -----------
        capacity : int
            the buffer capacity.
        
        Returns
        --------
        output : ByteBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newByteBuffer(self, a: Byte1D) -> ByteBuffer:
        """
        Returns a new direct byte buffer. Allocates the buffer with capacity
        equal to the length of the specified array, and copies all array
        elements to the buffer.
        
        Parameters
        -----------
        a : Byte1D
            the array.
        
        Returns
        --------
        output : ByteBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newDoubleBuffer(self, capacity: int) -> DoubleBuffer:
        """
        Returns a new direct double buffer.
        
        Parameters
        -----------
        capacity : int
            the buffer capacity.
        
        Returns
        --------
        output : DoubleBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newDoubleBuffer(self, a: Double1D) -> DoubleBuffer:
        """
        Returns a new direct double buffer. Allocates the buffer with capacity
        equal to the length of the specified array, and copies all array
        elements to the buffer.
        
        Parameters
        -----------
        a : Double1D
            the array.
        
        Returns
        --------
        output : DoubleBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newFloatBuffer(self, capacity: int) -> FloatBuffer:
        """
        Returns a new direct float buffer.
        
        Parameters
        -----------
        capacity : int
            the buffer capacity.
        
        Returns
        --------
        output : FloatBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newFloatBuffer(self, a: Float1D) -> FloatBuffer:
        """
        Returns a new direct float buffer. Allocates the buffer with capacity
        equal to the length of the specified array, and copies all array
        elements to the buffer.
        
        Parameters
        -----------
        a : Float1D
            the array.
        
        Returns
        --------
        output : FloatBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newIntBuffer(self, capacity: int) -> IntBuffer:
        """
        Returns a new direct int buffer.
        
        Parameters
        -----------
        capacity : int
            the buffer capacity.
        
        Returns
        --------
        output : IntBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newIntBuffer(self, a: Int1D) -> IntBuffer:
        """
        Returns a new direct int buffer. Allocates the buffer with capacity
        equal to the length of the specified array, and copies all array
        elements to the buffer.
        
        Parameters
        -----------
        a : Int1D
            the array.
        
        Returns
        --------
        output : IntBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newLongBuffer(self, capacity: int) -> LongBuffer:
        """
        Returns a new direct long buffer.
        
        Parameters
        -----------
        capacity : int
            the buffer capacity.
        
        Returns
        --------
        output : LongBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newLongBuffer(self, a: Long1D) -> LongBuffer:
        """
        Returns a new direct long buffer. Allocates the buffer with capacity
        equal to the length of the specified array, and copies all array
        elements to the buffer.
        
        Parameters
        -----------
        a : Long1D
            the array.
        
        Returns
        --------
        output : LongBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newShortBuffer(self, capacity: int) -> ShortBuffer:
        """
        Returns a new direct short buffer.
        
        Parameters
        -----------
        capacity : int
            the buffer capacity.
        
        Returns
        --------
        output : ShortBuffer
            the new buffer.
        """

    @overload
    @staticmethod
    def newShortBuffer(self, a: Short1D) -> ShortBuffer:
        """
        Returns a new direct short buffer. Allocates the buffer with capacity
        equal to the length of the specified array, and copies all array
        elements to the buffer.
        
        Parameters
        -----------
        a : Short1D
            the array.
        
        Returns
        --------
        output : ShortBuffer
            the new buffer.
        """
