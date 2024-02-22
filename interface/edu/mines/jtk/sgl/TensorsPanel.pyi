from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class TensorsPanel:
    """
    An axis-aligned panel that displays a slice of a 3D metric tensor field.
    The tensors correspond to symmetric positive-definite 3x3 matrices, and
    are rendered as ellipsoids.
    """

    @overload
    def __init__(self, et: EigenTensors3) -> None:
        """
        Constructs a tensors panel for the specified tensor field.
        Assumes default unit samplings.
        
        Parameters
        -----------
        et : EigenTensors3
            the eigentensors; by reference, not by copy.
        """

    @overload
    def __init__(self, s1: Sampling, s2: Sampling, s3: Sampling,
                 et: EigenTensors3) -> None:
        """
        Constructs a tensors panel for the specified tensor field.
        
        Parameters
        -----------
        s1 : Sampling
            sampling of 1st dimension (Z axis).
        s2 : Sampling
            sampling of 2nd dimension (Y axis).
        s3 : Sampling
            sampling of 3rd dimension (X axis).
        et : EigenTensors3
            the eigentensors; by reference, not by copy.
        """

    def update(self) -> None:
        """
        Updates the panel.
        This method should be called when the tensor field
        referenced by this tensors panel has been modified.
        """

    def setEllipsoidSize(self, size: int) -> None:
        """
        Sets the maximum size of the ellipsoids.
        As this size is increased, the number of ellipsoids decreases.
        
        Parameters
        -----------
        size : int
            the maximum ellipsoid size, in samples.
        """
