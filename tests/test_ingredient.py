import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    
    @pytest.mark.parametrize("ing_type, ing_name, ing_price", [
        ([INGREDIENT_TYPE_SAUCE, "кетчуп", 100.6]),  
        (INGREDIENT_TYPE_FILLING, "котлета", 200 ),                   
        (INGREDIENT_TYPE_FILLING, 123, "-" ),  
        (123, "сыр", "130" ), 
        (INGREDIENT_TYPE_FILLING, "", "80" ),
        (INGREDIENT_TYPE_SAUCE, "соленые огурчики", 90.5 )            
    ])   
    def test_add_ingredient(self, ing_type, ing_name, ing_price):
        ingredient = Ingredient(ingredient_type = ing_type, name = ing_name, price = ing_price)
        assert ingredient.get_type() == ing_type
        assert ingredient.get_name() == ing_name
        assert ingredient.get_price() == ing_price
        