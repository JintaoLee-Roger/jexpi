class ByteOrder:
    """
    A typesafe enumeration for byte orders.
    """
    # Constant denoting big-endian byte order. In this order, the bytes of a multibyte value are ordered from most significant to least significant.
    BIG_ENDIAN = 1

    # Constant denoting little-endian byte order. In this order, the bytes of a multibyte value are ordered from least significant to most significant.
    LITTLE_ENDIAN = 0

    def __init__(self) -> None:
        ...

    def nativeOrder(self) -> ByteOrder:
        """
        Retrieves the native byte order of the underlying platform.

        This method is defined so that performance-sensitive Java code can 
        allocate direct buffers with the same byte order as the hardware. 
        Native code libraries are often more efficient when such buffers 
        are used.

        Returns
        --------
        output : ByteOrder
            The native byte order of the hardware upon which this 
            Java virtual machine is running
        """
        ...

    def toString(self) -> str:
        """
        Constructs a string describing this object.

        This method returns the string "BIG_ENDIAN" for BIG_ENDIAN 
        and "LITTLE_ENDIAN" for LITTLE_ENDIAN.
        """
        ...
