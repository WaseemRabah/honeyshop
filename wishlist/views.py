from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import Wishlist
from products.models import Product

class WishlistView(View):
    template_name = 'wishlist/wishlist.html'

    @login_required
    def get(self, request):
        user = request.user

        try:
            wishlist = Wishlist.objects.get(user=user)
            wishlist_products = wishlist.get_all_products()
        except Wishlist.DoesNotExist:
            wishlist_products = []

        context = {
            'wishlist_products': wishlist_products
        }

        return render(request, self.template_name, context)


class WishlistActionView(View):
    def get(self, request, product_id, action):
        user = request.user
        product = get_object_or_404(Product, pk=product_id)

        try:
            wishlist = Wishlist.objects.get(user=user)
        except Wishlist.DoesNotExist:
            wishlist = Wishlist.objects.create(user=user)

        if action == 'add':
            wishlist.add_to_wishlist(product)
        elif action == 'remove':
            wishlist.remove_from_wishlist(product)

        return redirect('wishlist')
