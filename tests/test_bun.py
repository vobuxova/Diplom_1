import pytest
from praktikum.bun import Bun

class TestBun:
    def test_bun_creation_with_correct_data(self):
        
        bun = Bun(name="Sesame Bun", price=1.5)
        assert bun.get_name() == "Sesame Bun", "Имя булочки должно быть 'Sesame Bun'"
        assert bun.get_price() == 1.5, "Цена булочки должна быть 1.5"

    @pytest.mark.parametrize("name, price, expected_name, expected_price", [
        ("Sesame Bun", 1.5, "Sesame Bun", 1.5),  # Корректные данные
        (123, 1.5, 123, 1.5),                   # Нестроковое имя
        ("Sesame Bun", "1.5", "Sesame Bun", "1.5"),  # Нечисловая цена
        ("Sesame Bun", -1.5, "Sesame Bun", -1.5),    # Отрицательная цена
        ("", 1.5, "", 1.5),                     # Пустое имя
    ])
    def test_bun_with_various_data(self, name, price, expected_name, expected_price):
        
        bun = Bun(name=name, price=price)
        assert bun.get_name() == expected_name, f"Имя булочки должно быть {expected_name}"
        assert bun.get_price() == float(expected_price), f"Цена булочки должна быть {expected_price}"
