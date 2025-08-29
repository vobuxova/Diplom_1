from praktikum.database import Database
from praktikum.ingredient import Ingredient


class TestDataBase:
    def test_create_database(self):
        database = Database()
        buns_list = database.available_buns()
        ingredients_list = database.available_ingredients()
        assert len(buns_list) == 3
        assert len(ingredients_list) == 6
        assert buns_list[0].get_name() == "black bun"
        assert buns_list[0].get_price() == 100
        assert buns_list[1].get_name() == "white bun"
        assert buns_list[1].get_price() == 200
        assert buns_list[2].get_name() == "red bun"
        assert buns_list[2].get_price() == 300
        assert ingredients_list[0].get_name() == "hot sauce"
        assert ingredients_list[1].get_name() == "sour cream"
        assert ingredients_list[3].get_name() == "cutlet"