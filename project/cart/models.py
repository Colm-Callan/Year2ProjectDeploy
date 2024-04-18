from django.db import models
from shop.models import Product
from users.models import CustomUser

class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'Cart'
        ordering = ['date_added']
    def __str__(self):
        return self.cart_id

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    
    class Meta:
        db_table = 'CartItem'
    
    
    def sub_total(self):
        subtotal = self.product.price * self.quantity
        if self.user and self.user.is_loyal:
            subtotal = self.product.loyal_price * self.quantity
        return subtotal
    
    def __str__(self):
        return str(self.product.name)