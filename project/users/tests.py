from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from shop.models import Product, Category

class LoginTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_with_valid_credentials(self):
        response = self.client.post(reverse('login'), {'username': self.username, 'password': self.password})
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_login_with_invalid_credentials(self):
        response = self.client.post(reverse('login'), {'username': 'invaliduser', 'password': 'invalidpassword'})
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_logout(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get(reverse('logout'))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def tearDown(self):
        self.user.delete()

class AdminStockTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="Test Description", room="bedroom")
        self.product = Product.objects.create(name="Test Product", description="Test Description", category=self.category, price=10.0, stock=10)


    def test_add_stock_1(self):
        initial_stock = self.product.stock

        response = self.client.post(reverse('admin_product_stock_add_1', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        
        updated = Product.objects.get(pk=self.product.pk)
      
        self.assertEqual(updated.stock, initial_stock+1)
        
    def test_add_stock_10(self):
        initial_stock = self.product.stock

        response = self.client.post(reverse('admin_product_stock_add_10', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        
        updated = Product.objects.get(pk=self.product.pk)
      
        self.assertEqual(updated.stock, initial_stock+10)
        
    def test_delete_stock_1(self):
        initial_stock = self.product.stock

        response = self.client.post(reverse('admin_product_stock_delete_1', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        
        updated = Product.objects.get(pk=self.product.pk)
      
        self.assertEqual(updated.stock, initial_stock-1)
        
    def test_delete_stock_10(self):
        initial_stock = self.product.stock

        response = self.client.post(reverse('admin_product_stock_delete_10', args=[self.product.pk]))
        self.assertEqual(response.status_code, 302)
        
        updated = Product.objects.get(pk=self.product.pk)
      
        self.assertEqual(updated.stock, initial_stock-10)
        