"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""
from typing import Any, Dict


class SimplifiedEnum(type):
    """Convert __keys (iterable) to separate attributes"""

    def __new__(cls, name: Any, bases: Any, dct: Dict, **kwargs):
        """Convert __keys (iterable) to separate attributes"""
        key = f"_{name}__keys"
        if key in dct:
            for value in dct[key]:
                dct[value] = value
        cls_inst = super().__new__(cls, name, bases, dct, **kwargs)
        return cls_inst
