from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.sgl import *


class SelectDragMode:
    """
    A mode for selecting and dragging nodes.
    """

    def __init__(self, modeManager: ModeManager) -> None:
        """
        Constructs a select-drag mode with specified manager.
        
        Parameters
        -----------
        modeManager : ModeManager
            the mode manager for this mode.
        """
