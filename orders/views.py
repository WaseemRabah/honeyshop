from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .models import Order
from django.views import View
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Order, OrderItem
from wishlist.models import Wishlist, WishlistItem
from django.db import transaction


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'


class MakeOrderView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        wishlist_items = WishlistItem.objects.filter(wishlist__user=request.user)

        if not wishlist_items.exists():
            messages.warning(request, 'Your wishlist is empty. Add some items before making an order.')
            return redirect(reverse('wishlist:wishlist-list'))

        context = {'wishlist_items': wishlist_items}
        return render(request, 'orders/make_order.html', context)

    def post(self, request, *args, **kwargs):
        wishlist_items = WishlistItem.objects.filter(wishlist__user=request.user)

        if not wishlist_items.exists():
            messages.warning(request, 'Your wishlist is empty. Add some items before making an order.')
            return redirect(reverse('wishlist:wishlist-list'))

        try:
            with transaction.atomic():
                # Create a new order
                order = Order.objects.create(user=request.user)

                # Move wishlist items to the order
                for wishlist_item in wishlist_items:
                    OrderItem.objects.create(order=order, product=wishlist_item.product)

                # Clear the user's wishlist
                WishlistItem.objects.filter(wishlist__user=request.user).delete()

                messages.success(request, 'Order successfully placed!')
                return redirect(reverse('orders:order-detail', kwargs={'order_id': order.id}))

        except Exception as e:
            messages.error(request, f'Failed to create the order. Error: {str(e)}')
            return redirect(reverse('wishlist:wishlist-list'))