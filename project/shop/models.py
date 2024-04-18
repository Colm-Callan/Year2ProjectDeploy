from django.db import models
import uuid
from django.urls import reverse
from users.models import CustomUser

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'category', blank=True)
    
    ROOM_CHOICES = [
        ('bedroom', 'Bedroom'),
        ('kitchen', 'Kitchen'),
        ('living_room', 'Living Room'),
        ('bathroom', 'Bathroom'),
        ('garden', 'Garden'),
    ]
    
    room = models.CharField(max_length=200, choices=ROOM_CHOICES, default=None)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('shop:products_by_category', args=[self.id])
    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)

    name = models.CharField(max_length=120, unique=True)
    description = models.TextField(blank = True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to = 'product', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    loyal_product = models.BooleanField(default=False)
    loyal_price = models.DecimalField(max_digits=10,decimal_places=2, blank=True, null=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        
    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.category.id, self.id])
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.loyal_price is None:
            self.loyal_price = float(self.price) * 0.9  
        super().save(*args, **kwargs)



class Review(models.Model):
    user = models.ForeignKey(CustomUser, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    comment = models.TextField(max_length=250)
    rate = models.IntegerField(default=0)
    posted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)
   
