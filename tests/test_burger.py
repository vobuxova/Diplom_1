import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestBurger:
    
    def test_burger_creation(self):
        burger = Burger()
        assert burger.bun == None
        assert burger.ingredients == []
        
        
    @pytest.mark.parametrize("ing_type, ing_name, ing_price", [
        (INGREDIENT_TYPE_SAUCE, "кетчуп", 100.6),
        (INGREDIENT_TYPE_FILLING, "котлета", 200.0),
        (INGREDIENT_TYPE_SAUCE, "майонез", 130.0),
        (INGREDIENT_TYPE_FILLING, "сыр", 120.0),
        (INGREDIENT_TYPE_SAUCE, "соленые огурчики", 90.5)
    ])
    def test_add_ingredient(self, burger, ing_type, ing_name, ing_price):
        ingredient = Mock()
        ingredient.get_type.return_value = ing_type
        ingredient.get_name.return_value = ing_name
        ingredient.price = ing_price
        burger.add_ingredient(ingredient)

        assert ingredient in burger.ingredients
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self, burger):
        ingredient1 = Mock()
        ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient1.get_name.return_value = "кетчуп"
        ingredient1.price = 100.6

        ingredient2 = Mock()
        ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient2.get_name.return_value = "котлета"
        ingredient2.price = 200.0

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.remove_ingredient(1)

        assert ingredient2 not in burger.ingredients
        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient1

    def test_move_ingredient(self, burger):
        ingredient1 = Mock()
        ingredient1.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient1.get_name.return_value = "кетчуп"
        ingredient1.price = 100.6

        ingredient2 = Mock()
        ingredient2.get_type.return_value = INGREDIENT_TYPE_FILLING
        ingredient2.get_name.return_value = "котлета"
        ingredient2.price = 200.0

        burger.add_ingredient(ingredient1)
        burger.add_ingredient(ingredient2)

        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == ingredient2

    def test_get_price(self, burger):
        ingredient = Mock()
        ingredient.price = 100.6
        ingredient.get_price.return_value = 100.6
        bun = Bun(name="Sesame Bun", price=30.5)
        burger.set_buns(bun)  
        burger.add_ingredient(ingredient)
        price = burger.get_price()
        total_price = ingredient.price + bun.get_price() * 2
        assert price == total_price
        assert price == 161.6

    def test_get_receipt(self, burger):
        ingredient = Mock()
        ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        ingredient.get_name.return_value = "кетчуп"
        ingredient.price = 100.6
        ingredient.get_price.return_value = 100.6
        bun = Bun(name="Sesame Bun", price=30.5)
        burger.set_buns(bun)  
        burger.add_ingredient(ingredient)
        receipt = burger.get_receipt()
        expected_receipt = (
            "(==== Sesame Bun ====)\n"
            "= sauce кетчуп =\n"
            "(==== Sesame Bun ====)\n\n"
            "Price: 161.6"
        )
        assert receipt == expected_receipt
