from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.awt import Mode


class ModeMenuItem:
    """
    A menu item for a mode. When the mode is active, the mode menu item
    appears to be selected.
    
    Ordinary menu items constructed with an action (such as a mode) update
    their appearance when the action is enabled or disabled. A mode menu
    item does that, and also updates its appearance when the mode is
    activated or deactivated.
    """

    def __init__(self, mode: Mode) -> None:
        """
        Constructs a mode menu item for the specified mode.
        
        Parameters
        -----------
        mode : Mode
            the mode.
        """
