from typing import overload
from edu.mines.jtk.mapping import *


class Selectable:
    """
    An interface implemented by nodes that can be selected. This interface
    serves as a <em>marker</em> interface, because its methods are implemented
    by the abstract base class {@link Node} for all nodes, whether selectable
    or not. The behavior of those implementations depends on whether or not
    the class that extends {@link Node} also implements this marker interface.
    """

    def isSelected(self) -> bool:
        """
        Determines whether this node is currently selected.
        Returns
        --------
        output : bool
            true, if selected; false, otherwise.
        """

    def setSelected(self, selected: bool) -> None:
        """
        Sets the selected state for this node.
        
        Parameters
        -----------
        selected : bool
            true, for selected; false, otherwise.
        """
