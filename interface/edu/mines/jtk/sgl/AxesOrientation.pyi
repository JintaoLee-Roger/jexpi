from typing import overload
from edu.mines.jtk.mapping import *
from enum import Enum


class AxesOrientation(Enum):
    XRIGHT_YUP_ZOUT = 0
    XRIGHT_YOUT_ZDOWN = 1
    XRIGHT_YIN_ZDOWN = 2
    XOUT_YRIGHT_ZUP = 3
    XDOWN_YRIGHT_ZOUT = 4
    XUP_YLEFT_ZOUT = 5
    XUP_YRIGHT_ZOUT = 6
