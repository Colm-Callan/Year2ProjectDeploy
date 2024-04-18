from django.test import TestCase
from .models import Order, OrderItem

class OrderTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            token="test_token",
            total=100.0,
            emailAddress="test@example.com",
            billingName="Test Billing Name",
            billingAddress1="Test Billing Address",
            billingCity="Test Billing City",
            billingPostcode="12345",
            billingCountry="Test Billing Country",
            shippingName="Test Shipping Name",
            shippingAddress1="Test Shipping Address",
            shippingCity="Test Shipping City",
            shippingPostcode="54321",
            shippingCountry="Test Shipping Country"
        )

    def test_order_str(self):
        self.assertEqual(str(self.order), str(self.order.id))

class OrderItemTestCase(TestCase):
    def setUp(self):
        self.order = Order.objects.create(
            token="test_token",
            total=100.0,
            emailAddress="test@example.com",
            billingName="Test Billing Name",
            billingAddress1="Test Billing Address",
            billingCity="Test Billing City",
            billingPostcode="12345",
            billingCountry="Test Billing Country",
            shippingName="Test Shipping Name",
            shippingAddress1="Test Shipping Address",
            shippingCity="Test Shipping City",
            shippingPostcode="54321",
            shippingCountry="Test Shipping Country"
        )

        self.order_item = OrderItem.objects.create(
            product="Test Product",
            quantity=2,
            price=50.0,
            order=self.order
        )

    def test_order_item_sub_total(self):
        expected_sub_total = self.order_item.quantity * self.order_item.price
        self.assertEqual(self.order_item.sub_total(), expected_sub_total)

    def test_order_item_str(self):
        self.assertEqual(str(self.order_item), self.order_item.product)
