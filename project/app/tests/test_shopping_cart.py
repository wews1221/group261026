from os import name

from models import shopping_cart
from models.shopping_cart import ShoppingCart

class TestShoppingCart:
    def test_shopping_cart(self):
        cart = ShoppingCart()
        assert cart.item == []

class TestAddCartItems:
    def test_add_new_item(self):
        cart = ShoppingCart()
        cart.add_item('Яблуко', 10, 5)
        assert cart.item[0] == {
            'name' : 'Яблуко',
            'price': 10,
            'quantity' : 5
        }

    def test_add_existing_item(self):
        cart = ShoppingCart()
        cart.add_item('Яблуко',10, 5)
        cart.add_item('Яблуко', 11, 3)
        assert cart.item[0]['quantity'] == 8
        assert cart.item[0]['price'] == 11

class TestRemoveShoppingCart:
    def test_remove_existing_item(self):
        cart = ShoppingCart()
        cart.add_item('Молоко', 35, 1)
        cart.remove_item('Молоко')

        assert cart.item == []

    def test_remove_no_existing_item(self):
        cart = ShoppingCart()
        cart.add_item('Молоко', 35, 1)
        cart.remove_item('Хліб')