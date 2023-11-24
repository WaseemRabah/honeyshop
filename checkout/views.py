from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from orders.models import Order

class CheckoutView(View):
    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        
        order = create_order(request.user)

        
        clear_cart(request.user)

        messages.success(request, 'Order placed successfully!')
        return redirect('home')  

def create_order(user):
    
    
    order = Order.objects.create(user=user)
    cart_items = user.cart_items.all()

    
    order.items.set(cart_items)

    
    total_price = sum(item.product.price for item in cart_items)
    order.total_price = total_price
    order.save()

def clear_cart(user):
    
    user.cart_items.clear()
