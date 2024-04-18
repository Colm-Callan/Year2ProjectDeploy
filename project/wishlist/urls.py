from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('detail/', views.wishlist_detail, name='wishlist_detail'),
    path('add/<uuid:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove/<uuid:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
