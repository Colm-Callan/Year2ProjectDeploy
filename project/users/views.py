from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views.generic import ListView, TemplateView, CreateView, DetailView, DeleteView
from .models import CustomUser
from  django.shortcuts import render
from shop.models import Product
from django.shortcuts import get_object_or_404, redirect


class HomePageView(TemplateView):
    template_name = 'home.html'

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'registration/user_profile.html'

    def post(self, request, *args, **kwargs):
        object_instance = self.get_object()
        object_instance.is_loyal = True
        object_instance.save()
        success_message = "You have successfully signed up for the loyal customer."
        return render(request, self.template_name, {'object': object_instance, 'success_message': success_message})


class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'registration/user_delete.html'
    success_url = reverse_lazy('home')

def AdminUserListView(request):
    
    users= CustomUser.objects.all()
    return render(request, 'admin/admin_user_list.html', {'users':users})

def AdminUser_delete(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)
    if request.method == 'POST':    
        user.delete()
        return redirect('admin_user_list')
    return redirect('admin_user_list')

def AdminStock(request):
    products = Product.objects.all()
    return render(request, 'admin/admin_product_stock.html',{'product':products})

def AdminStock_add_1(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':    
        product.stock +=1
        product.save()
        return redirect('admin_product_stock')

def AdminStock_add_10(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':    
        product.stock +=10
        product.save()
        return redirect('admin_product_stock')

def AdminStock_delete_1(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':    
        product.stock -=1
        product.save()
        return redirect('admin_product_stock')

def AdminStock_delete_10(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':    
        product.stock -=10
        product.save()
        return redirect('admin_product_stock')    