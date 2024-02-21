from typing import overload


class BorderLayout:
    """
    A border layout lays out a container, arranging and resizing its 
    components to fit in five regions: north, south, east, west, and 
    center. Each region may contain no more than one component, and is 
    identified by a corresponding constant: NORTH, SOUTH, EAST, WEST, 
    and CENTER.
    """

    @overload
    def __init__(self) -> None:
        """Constructs a new border layout with no gaps between components."""

    @overload
    def __init__(self, hgap: int, vgap: int) -> None:
        """Constructs a border layout with the specified gaps between components."""
