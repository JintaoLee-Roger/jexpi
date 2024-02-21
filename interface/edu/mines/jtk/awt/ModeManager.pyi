from typing import overload
from edu.mines.jtk.mapping import *


class ModeManager:
    """
    A manager for a set of modes and components. A mode manager handles
    activation and deactivation for all modes in its set of modes. It does
    this by passing the active state (true or false) to its modes, for each
    of the components in its set of components. Typically, when activated,
    a mode adds input event listeners to the specified components. Then,
    when deactivated, such a mode removes those event listeners.
    """

    def __init__(self) -> None:
        """
        Constructs a mode manager with an empty set of modes.
        """

    def add(self, c: Component) -> None:
        """
        Adds the specified component.
        
        Parameters
        -----------
        c : Component
            the component.
        """

    def remove(self, c: Component) -> None:
        """
        Removes the specified component.
        
        Parameters
        -----------
        c : Component
            the component.
        """
