from homework11.task1.enum_class import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_simplified_enum():
    assert ColorsEnum.RED == "RED"
    assert SizesEnum.XL == "XL"
