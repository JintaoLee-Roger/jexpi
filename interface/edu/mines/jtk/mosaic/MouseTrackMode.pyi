from typing import overload
from edu.mines.jtk.mapping import *


class MouseTrackMode:
    """
    A mode for tracking the mouse location. When this mode is active,
    then mouse movement within any tile is highlighted in any tile axes
    in that tile's row and column. This mode is not exclusive.
    """

    def __init__(self, modeManager: ModeManager) -> None:
        """
        Constructs a mouse track mode with specified manager.
        
        Parameters
        -----------
        modeManager : ModeManager
            the mode manager for this mode.
        """

    def isExclusive(self) -> bool:
        """
        Returns false, to indicate that mouse track mode is not exclusive.
        Returns
        --------
        output : bool
            false.
        """
