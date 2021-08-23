import pytest

from homework11.task2.discont_program import Order


def test_strategy():
    def morning_discount(order):
        discount = 0.4
        return order - order * discount

    def elder_discount(order):
        discount = 0.7
        return order - order * discount

    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 60
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 30


def test_wrong_price():
    def elder_discount(order):
        discount = 0.7
        return order - order * discount

    with pytest.raises(ValueError):
        Order(-1, elder_discount)
