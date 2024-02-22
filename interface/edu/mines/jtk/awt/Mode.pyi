from typing import overload
from edu.mines.jtk.mapping import *
from edu.mines.jtk.awt import ModeManager


class Mode:
    """
    An abstract mode of interaction.
    
    A mode can be activated or deactivated, by setting its active state.
    An active mode responds to input events in some mode-specific manner.
    An inactive mode ignores all input events.
    
    A mode is an action, so it can be used to construct toggle buttons and
    menu items. A mode, like any action, may be enabled or disabled. While
    enabled, a mode may be active or inactive. While disabled, a mode is
    inactive, and cannot be activated.
    
    A mode has a manager, which coordinates the activation of modes that may
    be mutually exclusive. When an exclusive mode is activated, the mode's
    manager first deactivates any other exclusive modes, thereby ensuring
    that no more than one exclusive mode is active at any time. By default,
    modes are exclusive, but this property may be overridden.
    """

    def __init__(self, manager: ModeManager) -> None:
        """
        Constructs a mode with specified manager, name, and icon.
        
        Parameters
        -----------
        manager : ModeManager
            the manager.
        """

    def setActive(self, active: bool) -> None:
        """
        Activates or deactivates this mode. If this mode is not enabled,
        this method does nothing.
        
        Parameters
        -----------
        active : bool
            true, to activate; false, to deactivate.
        """

    def isActive(self) -> bool:
        """
        Determines whether this mode is active.
        Returns
        --------
        output : bool
            true, if active; false, if inactive.
        """

    def isExclusive(self) -> bool:
        """
        Determines whether or not this mode is exclusive. Exclusive modes
        cannot coexist with other exclusive modes that have the same manager.
        This implementation simply returns true. Non-exclusive modes should
        override this method to return false.
        Returns
        --------
        output : bool
            true, if exclusive; false, otherwise.
        """

    def actionPerformed(self, event: ActionEvent) -> None:
        """
        Toggles the active state of this mode.
        
        Parameters
        -----------
        event : ActionEvent
            the action event (ignored).
        """

    def setEnabled(self, enabled: bool) -> None:
        """
    
        """

    def setName(self, name: String) -> None:
        """
        Sets the name (text) for this mode.
        Used for mode menu items.
        
        Typically, this method is called by constructors in classes that
        extend this abstract base class.
        
        Parameters
        -----------
        name : String
            the name.
        """

    def setIcon(self, icon: Icon) -> None:
        """
        Sets the icon for this mode.
        Used for mode toggle buttons.
        
        Typically, this method is called by constructors in classes that
        extend this abstract base class.
        
        Parameters
        -----------
        icon : Icon
            the icon.
        """

    def setMnemonicKey(self, mk: int) -> None:
        """
        Sets the mnemonic key for this mode.
        Used for mode menu items.
        
        Typically, this method is called by constructors in classes that
        extend this abstract base class.
        
        Parameters
        -----------
        mk : int
            the mnemonic key; e.g., KeyEvent.VK_K.
        """

    def setAcceleratorKey(self, ak: KeyStroke) -> None:
        """
        Sets the accelerator key stroke for this mode.
        
        Typically, this method is called by constructors in classes that
        extend this abstract base class.
        
        Parameters
        -----------
        ak : KeyStroke
            the accelerator key stroke.
        """

    def setShortDescription(self, sd: String) -> None:
        """
        Sets the short description for this mode.
        Used in tool tips for mode menu items and toggle buttons.
        
        Typically, this method is called by constructors in classes that
        extend this abstract base class.
        
        Parameters
        -----------
        sd : String
            the short description.
        """

    def setLongDescription(self, ld: String) -> None:
        """
        Sets the long description for this mode.
        
        Typically, this method is called by constructors in classes that
        extend this abstract base class.
        
        Parameters
        -----------
        ld : String
            the long description.
        """

    def setCursor(self, cursor: Cursor) -> None:
        """
        Sets the cursor for this mode.
        If not null, the specified cursor is used when this mode is active.
        
        Parameters
        -----------
        cursor : Cursor
            the cursor; null, if the default cursor should be used.
        """

    def getCursor(self) -> Cursor:
        """
        Gets the cursor for this mode.
        Returns
        --------
        output : Cursor
            the cursor; null, if the default cursor should be used.
        """
