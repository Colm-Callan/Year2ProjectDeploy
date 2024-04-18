from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('placed/<int:order_id>/', views.order_placed, name='order_placed'),
    path('history/', views.orderHistory.as_view(), name='order_history'),
    path('<int:order_id>/', views.orderDetail.as_view(), name='order_detail'),
] 