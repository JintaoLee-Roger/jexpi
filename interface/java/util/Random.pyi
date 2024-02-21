from typing import overload


class Random:

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, seed: int) -> None:
        ...
