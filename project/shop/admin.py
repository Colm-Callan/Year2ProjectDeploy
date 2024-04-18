from django.contrib import admin
from .models import Category, Product, Review

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description', 'category', 'stock',
    'available', 'loyal_product']
    list_editable = ['price', 'stock', 'available']
    list_per_page = 20
admin.site.register(Product, ProductAdmin)

    
class ReviewAdmin(admin.ModelAdmin):
    list_display= ['comment','rate']
    # list_editable = ['comment','rate']
admin.site.register(Review, ReviewAdmin)




