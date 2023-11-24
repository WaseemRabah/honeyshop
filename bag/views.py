from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .contexts import Cart
from products.models import Product
from orders.models import Order

@login_required
@require_POST
def add_to_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('bag:cart')

@login_required
@require_POST
def remove_from_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('bag:cart')

@login_required
def view_cart(request):
    cart = Cart(request)
    return render(request, 'bag/cart.html', {'cart': cart})

@login_required
def make_order(request):
    cart = Cart(request)
    order = Order.objects.create(user=request.user)
    for item in cart:
        order.items.add(item.product, quantity=item.quantity)
    cart.clear()
    return render(request, 'bag/order_confirmation.html', {'order': order})
