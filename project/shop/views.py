from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Review
from django.views.generic.edit import CreateView
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from decimal import Decimal

def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)

    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=category)

    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price:
        try:
            min_price = Decimal(min_price)
            products = products.filter(price__gte=min_price)
        except Decimal.InvalidOperation:
            pass

    if max_price:
        try:
            max_price = Decimal(max_price)
            products = products.filter(price__lte=max_price)
        except Decimal.InvalidOperation:
            pass

    sort_order = request.GET.get('sort')
    if sort_order == 'low_to_high':
        products = products.order_by('price')
    elif sort_order == 'high_to_low':
        products = products.order_by('-price')

    return render(request, 'shop/category.html', {'category': category, 'prods': products})


def product_detail(request, category_id, product_id):
    products = Product.objects.all()
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    product_reviews = Review.objects.filter(product_id=product_id)
    return render(request, 'shop/product.html', {'product': product, 'product_reviews': product_reviews, 'products':products})

def bedroom_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    return render(request, 'rooms/bedroom.html',{'category':category, 'prods':products})


def kitchen_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    return render(request, 'rooms/kitchen.html',{'category':category, 'prods':products})


def garden_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    return render(request, 'rooms/garden.html',{'category':category, 'prods':products})

    
def living_room_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    return render(request, 'rooms/living_room.html',{'category':category, 'prods':products})

    
def bathroom_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    return render(request, 'rooms/bathroom.html',{'category':category, 'prods':products})

    
class ProductCreateView(CreateView):
    model = Product
    template_name = 'shop/product_create.html'
    fields = ['name', 'description', 'category', 'price', 'image', 'stock', 'available','loyal_product']

@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    category_id = product.category.id


    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            rate = form.cleaned_data['rate']
            comment = form.cleaned_data['comment']
            Review.objects.create(product=product, user=request.user, rate=rate, comment=comment)

            return redirect('shop:product_detail', category_id=category_id, product_id=product_id)
    else:
        form = ReviewForm()

    return render(request, 'shop/add_review.html', {'form': form})