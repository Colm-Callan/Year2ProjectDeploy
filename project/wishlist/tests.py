from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from shop.models import Product, Category
from .models import Wishlist, WishlistItem
from datetime import date, datetime

class WishlistTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.category = Category.objects.create(name="Test Category", description="Test Description", room="bedroom")
        self.product = Product.objects.create(name="Test Product", description="Test Description", category=self.category, price=10.0, stock=100)
        self.user = User.objects.create_user(username="test username", password="test password")

        
        self.wishlist = Wishlist.objects.create(user=self.user, product=self.product)
        self.wishlist_item = WishlistItem.objects.create(user=self.user, product=self.product)

        print(self.wishlist.created_at)
        print(datetime)


    # def test_Wishlist_creation(self):
        
    #     self.assertEqual(self.wishlist.created_at, datetime) 
        
        
    # def test_Wishlist_add(self):

    #     response = self.client.post(reverse('Wishlist:add_cart', args=[self.product.pk]))

        
