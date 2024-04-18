from django.shortcuts import redirect, render
from .models import Wishlist, WishlistItem
from shop.models import Product
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings

def wishlist_detail(request, wishlist_items=None):
    if not request.user.is_authenticated:
        return redirect('login')

    try:
        wishlist_items = WishlistItem.objects.filter(user=request.user)

    except ObjectDoesNotExist:
        pass

    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})



def add_to_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = Product.objects.get(id=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    if created:
        pass
    else:
        pass
    return redirect('wishlist:wishlist_detail')

def remove_from_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = Product.objects.get(id=product_id)
    try:
        wishlist_item = WishlistItem.objects.get(user=request.user, product=product)
        wishlist_item.delete()
    except WishlistItem.DoesNotExist:
        pass
    return redirect('wishlist:wishlist_detail')
