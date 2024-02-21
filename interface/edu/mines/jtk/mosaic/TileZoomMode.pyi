from typing import overload
from edu.mines.jtk.mapping import *


class TileZoomMode:
    """
    A mode for zooming tiles and tile axes.
    """

    def __init__(self, modeManager: ModeManager) -> None:
        """
        Constructs a tile zoom mode with specified manager.
        
        Parameters
        -----------
        modeManager : ModeManager
            the mode manager for this mode.
        """
