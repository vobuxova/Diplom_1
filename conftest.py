import pytest
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient

@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


