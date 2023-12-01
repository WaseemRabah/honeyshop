from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.views import View

from .forms import OrderForm

class CheckoutView(View):
    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in your bag at the moment")
            return redirect(reverse('products'))

        order_form = OrderForm()
        context = {'order_form': order_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        
        order_form = OrderForm(request.POST)
        
        return redirect(reverse('checkout_success'))

