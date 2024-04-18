from django.test import TestCase
from django.urls import reverse
from .models import Category, Product, Review
from users.models import CustomUser

class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="Test Description", room="bedroom")

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Test Category")
        self.assertEqual(self.category.description, "Test Description")
        self.assertEqual(self.category.room, "bedroom")

    def test_category_absolute_url(self):
        expected_url = reverse('shop:products_by_category', args=[self.category.id])
        self.assertEqual(self.category.get_absolute_url(), expected_url)


class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category", description="Test Description", room="bedroom")
        self.product = Product.objects.create(name="Test Product", description="Test Description", category=self.category, price=10.0, stock=100)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(self.product.description, "Test Description")
        self.assertEqual(self.product.category, self.category)
        self.assertEqual(float(self.product.loyal_price), 9.0)

    def test_product_absolute_url(self):
        expected_url = reverse('shop:product_detail', args=[self.category.id, self.product.id])
        self.assertEqual(self.product.get_absolute_url(), expected_url)


class ReviewTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="testuser", email="test@example.com", password="testpassword")
        self.category = Category.objects.create(name="Test Category", description="Test Description", room="bedroom")
        self.product = Product.objects.create(name="Test Product", description="Test Description", category=self.category, price=10.0, stock=100)

    def test_review_creation_normal(self):
        self.review = Review.objects.create(user=self.user, product=self.product, comment="Test Comment", rate=5)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.comment, "Test Comment")
        self.assertEqual(self.review.rate, 5)

    def test_review_creation_negative(self):
        self.review = Review.objects.create(user=self.user, product=self.product, comment="Test Comment", rate=-1)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.comment, "Test Comment")
        self.assertEqual(self.review.rate, -1)

    def test_review_creation_above(self):
        self.review = Review.objects.create(user=self.user, product=self.product, comment="Test Comment", rate=10)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.comment, "Test Comment")
        self.assertEqual(self.review.rate, 10)

    def test_review_creation_fraction(self):
        self.review = Review.objects.create(user=self.user, product=self.product, comment="Test Comment", rate=4.5)
        self.assertEqual(self.review.user, self.user)
        self.assertEqual(self.review.product, self.product)
        self.assertEqual(self.review.comment, "Test Comment")
        self.assertEqual(self.review.rate, 4.5)

