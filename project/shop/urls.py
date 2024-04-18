from django.urls import path
from . import views
from . views import ProductCreateView

app_name = 'shop'

urlpatterns = [
    path('', views.prod_list, name = 'all_products'),
    path('<uuid:category_id>/', views.prod_list, name = 'products_by_category'),
    path('room/bedroom', views.bedroom_list, name = 'bedroom'),
    path('room/kitchen', views.kitchen_list, name = 'kitchen'),
    path('room/living_room', views.living_room_list, name = 'living_room'),
    path('room/garden', views.garden_list, name = 'garden'),
    path('room/bathroom', views.bathroom_list, name = 'bathroom'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name = 'product_detail'),

   
   
    path('<uuid:product_id>/add_review/', views.add_review, name='add_review'),


    # path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name = 'product_detail'),
] 


