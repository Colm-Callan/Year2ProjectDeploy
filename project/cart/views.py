from django.shortcuts import redirect, render, get_object_or_404
from shop.models import Product
from .models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist
from order.models import Order, OrderItem
from django.conf import settings
import stripe


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')

    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if (cart_item.quantity < cart_item.product.stock):
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1,cart=cart,user=request.user)
    return redirect('cart:cart_detail')

def cart_detail(request, total=0, counter=0, cart_items = None):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            if request.user.is_loyal:
                total += (cart_item.product.loyal_price * cart_item.quantity)
            else:
                total += (cart_item.product.price * cart_item.quantity)
                counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe_total = int(total*100)
    description = 'Furniture Store - New Order'
    data_key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method=='POST':
        print(request.POST)
        try:
            token = request.POST['stripeToken']
            email = request.POST['stripeEmail']
            billingName = request.POST['stripeBillingName']
            billingAddress1 = request.POST['stripeBillingAddressLine1']
            billingcity = request.POST['stripeBillingAddressCity']
            billingCountry = request.POST['stripeBillingAddressCountryCode']
            shippingName = request.POST['stripeShippingName']
            shippingAddress1 = request.POST['stripeShippingAddressLine1']
            shippingcity = request.POST['stripeShippingAddressCity']
            shippingCountry = request.POST['stripeShippingAddressCountryCode']
            customer = stripe.Customer.create(email=email, source=token)
            stripe.Charge.create(amount=stripe_total,
                                 currency="eur",
                                 description=description,
                                 customer=customer.id)
            
            try:
                order_details = Order.objects.create(
                        token = token,
                        total = total,
                        emailAddress = email,
                        billingName = billingName,
                        billingAddress1 = billingAddress1,
                        billingCity = billingcity,
                        billingCountry = billingCountry,
                        shippingName = shippingName,
                        shippingAddress1 = shippingAddress1,
                        shippingCity = shippingcity,
                        shippingCountry = shippingCountry
                    )
                order_details.save()
                for order_item in cart_items:
                    if request.user.is_loyal:
                        price = order_item.product.loyal_price
                    else:
                        price = order_item.product.price

                    oi = OrderItem.objects.create(
                        product = order_item.product.name,
                        quantity = order_item.quantity,
                        price = price,
                        order = order_details)
                    oi.save
                    
                    products = Product.objects.get(id=order_item.product.id)
                    products.stock = int(order_item.product.stock -
                    order_item.quantity)
                    products.save()
                    order_item.delete()
        
                    print('The order has been created')
                return redirect ('order:order_placed', order_details.id) 
            except ObjectDoesNotExist:
                pass

        except stripe.error.CardError as e:
            return e
        
    return render(request, 'cart/cart.html', {'cart_items':cart_items,'total':total, 'counter':counter, 'data_key':data_key, 'description':description})

def cart_remove(request, product_id):
    cart= Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
def full_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')