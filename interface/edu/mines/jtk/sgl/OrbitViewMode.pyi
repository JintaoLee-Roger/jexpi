from typing import overload
from edu.mines.jtk.mapping import *


class OrbitViewMode:
    """
    A mode for manipulating an orbit view.
    """

    def __init__(self, modeManager: ModeManager) -> None:
        """
        Constructs an orbit view mode with specified manager.
        
        Parameters
        -----------
        modeManager : ModeManager
            the mode manager for this mode.
        """
