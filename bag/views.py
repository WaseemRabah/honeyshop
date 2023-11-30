from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.generic import TemplateView, View
from django.urls import reverse
from .contexts import Cart, bag_contents
from products.models import Product
from orders.models import Order, OrderItem
from django.contrib import messages


class DisplayBagView(TemplateView):
    template_name = 'bag/cart.html'

    def get(self, request, *args, **kwargs):
        """ A view that renders the bag contents page """
        return self.render_to_response({})


class AddToBagView(View):
    def post(self, request, item_id):
        """ Add a quantity of the specified product to the shopping bag """
        product = Product.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

        request.session['bag'] = bag
        return redirect(redirect_url)


class AdjustBagView(View):
    def post(self, request, item_id):
        try:
            product = get_object_or_404(Product, pk=item_id)
            quantity = int(request.POST.get('quantity'))
            size = None
            if 'product_size' in request.POST:
                size = request.POST['product_size']

            bag = request.session.get('bag', {})

            if size:
                if quantity > 0:
                    bag[item_id]['items_by_size'][size] = quantity
                    messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
                else:
                    del bag[item_id]['items_by_size'][size]
                    if not bag[item_id]['items_by_size']:
                        bag.pop(item_id)
                        messages.success(request, f'Removed {product.name} from your bag')
            else:
                if quantity > 0:
                    bag[item_id] = quantity
                    messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
                else:
                    bag.pop(item_id)
                    messages.success(request, f'Removed {product.name} from your bag')

            request.session['bag'] = bag
            return redirect(reverse('bag:display_bag'))

        except Exception as e:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect(reverse('bag:display_bag'))


class RemoveFromBagView(View):
    def post(self, request, item_id):
        """Remove the item from the shopping bag"""
        try:
            size = None
            if 'product_size' in request.POST:
                size = request.POST['product_size']

            bag = request.session.get('bag', {})
            product = get_object_or_404(Product, pk=item_id)  # Add this line

            if size:
                del bag[item_id]['items_by_size'][size]
                if not bag[item_id]['items_by_size']:
                    bag.pop(item_id)
                    messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
            else:
                bag.pop(item_id)
                messages.success(request, f'Removed {product.name} from your bag')

            request.session['bag'] = bag
            return HttpResponse(status=200)

        except Exception as e:
            messages.error(request, f'Error removing item: {e}')
            return HttpResponse(status=500)


class CartView(TemplateView):
    template_name = 'bag/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve the user's cart
        user_cart = Cart(self.request)
        context['cart_items'] = user_cart.cart.values()
        return context
