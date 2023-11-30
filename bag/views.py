from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .contexts import Cart, bag_contents
from products.models import Product
from orders.models import Order, OrderItem
from django.views.generic import TemplateView



@login_required
def view_cart(request):
    cart = Cart(request)
    context = bag_contents(cart)
    return render(request, 'bag/cart.html', context)


@login_required
@require_POST
def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)


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

    # Create a new order
    order = Order.objects.create(user=request.user)

    # Move cart items to the order
    for item in cart:
        OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)

    # Clear the user's cart
    cart.clear()

    return render(request, 'products/product_list.html', {'order': order})


class CartView(TemplateView):
    template_name = 'bag/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Retrieve the user's cart
        user_cart = Cart(self.request)
        
        context['cart_items'] = user_cart.cart.values()

        return context
