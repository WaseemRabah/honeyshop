from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishlistItem
from products.models import Product
from django.contrib import messages
from django.urls import reverse


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if WishlistItem.objects.filter(user=request.user, product=product).exists():
        messages.warning(request, f"The product '{product.name}' is already in your wishlist.")
    else:
        WishlistItem.objects.create(user=request.user, product=product)
        messages.success(request, f"The product '{product.name}' has been added to your wishlist.")

    return redirect(reverse('products:products'))

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id, user=request.user)
    wishlist_item.delete()
    return redirect('view_wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/view_wishlist.html', {'wishlist_items': wishlist_items})
