from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from shop.models import Product, Category
from .models import Cart, CartItem
from datetime import date

class CartTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.category = Category.objects.create(name="Test Category", description="Test Description", room="bedroom")
        self.product = Product.objects.create(name="Test Product", description="Test Description", category=self.category, price=10.0, stock=100)
        self.user = User.objects.create_user(username="test username", password="test password")

        
        self.cart = Cart.objects.create()
        self.cart_item = CartItem.objects.create(product=self.product, cart=self.cart, quantity=4, active=True, user=self.user)

    def test_cart_creation(self):
        self.assertEqual(self.cart.date_added, date.today() )
        
    def test_cart_add(self):

        response = self.client.post(reverse('cart:add_cart', args=[self.product.pk]))

        

    # def test_cart_remove(self):
    #     response = self.client.post(reverse('cart:cart_remove', args=[self.product.id]))
