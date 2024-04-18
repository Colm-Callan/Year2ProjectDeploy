from django.urls import path
from .views import SignUpView, HomePageView, UserProfileView, UserDeleteView, AdminUserListView, AdminUser_delete, AdminStock, AdminStock_add_1, AdminStock_add_10, AdminStock_delete_1,AdminStock_delete_10

urlpatterns =[
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', HomePageView.as_view(), name='home'),
    path('<int:pk>/', UserProfileView.as_view(), name='user_profile'),
    path('<int:pk>/delete', UserDeleteView.as_view(), name='user_delete'),
    path('staff/users', AdminUserListView ,name='admin_user_list'),
    path('staff/users/delete/<int:user_id>/', AdminUser_delete ,name='admin_user_delete'),
    path('staff/product', AdminStock ,name='admin_product_stock'),
    path('staff/product/add_1/<uuid:product_id>/', AdminStock_add_1 ,name='admin_product_stock_add_1'),
    path('staff/product/add_10/<uuid:product_id>/', AdminStock_add_10 ,name='admin_product_stock_add_10'),

    path('staff/product/delete_1/<uuid:product_id>/', AdminStock_delete_1 ,name='admin_product_stock_delete_1'),
    path('staff/product/delete_10/<uuid:product_id>/', AdminStock_delete_10 ,name='admin_product_stock_delete_10'),


]