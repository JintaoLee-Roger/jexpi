from typing import overload
from edu.mines.jtk.mapping import *


class ModeToggleButton:
    """
    A toggle button for a mode. When the mode is active, the mode toggle
    button appears to be selected.
    
    Ordinary toggle buttons constructed with an action (such as a mode)
    update their appearance when the action is enabled or disabled. A mode
    toggle button does that, and also updates its appearance when the mode
    is activated or deactivated.
    """

    def __init__(self, mode: Mode) -> None:
        """
        Constructs a mode toggle button for the specified mode.
        
        Parameters
        -----------
        mode : Mode
            the mode.
        """
