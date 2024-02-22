from typing import overload
from edu.mines.jtk.mapping import *
from enum import Enum


class AxisScale(Enum):
    """
    Simple enum containing axis scaling options. 
    """
    LINEAR = 0
    LOG10 = 1

    def isLinear(self) -> bool:
        ...

    def isLog(self) -> bool:
        ...
