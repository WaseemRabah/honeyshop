from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import WishlistItem
from products.models import Product


def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = WishlistItem.objects.get_or_create(user=request.user, product=product)
    
    if created:
        print(f"Product '{product.name}' added to wishlist for user {request.user}")
    else:
        print(f"Product '{product.name}' already in wishlist for user {request.user}")

    return redirect('wishlist')

@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id, user=request.user)
    wishlist_item.delete()
    return redirect('wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/view_wishlist.html', {'wishlist_items': wishlist_items})
