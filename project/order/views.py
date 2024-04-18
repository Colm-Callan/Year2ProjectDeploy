from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from shop.models import Product


def order_placed(request, order_id):
 if order_id:
    customer_order = get_object_or_404(Order, id=order_id)
    products = Product.objects.all()
 return render(request, 'order/order_placed.html',{'customer_order': customer_order, 'products': products})

class orderHistory(LoginRequiredMixin, View):
    def get (self, request):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order_details = Order.objects.filter(emailAddress=email)
        return render(request, 'order/order_list.html', {'order_details': order_details})

class orderDetail(LoginRequiredMixin, View):
    def get(self, request, order_id):
        if request.user.is_authenticated:
            email = str(request.user.email)
            order = Order.objects.get(id=order_id, emailAddress=email)
            order_items = OrderItem.objects.filter(order=order)

        return render(request, 'order/order_detail.html', {'order': order, 'order_items': order_items})