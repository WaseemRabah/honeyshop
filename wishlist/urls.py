from django.urls import path
from .views import add_to_wishlist, remove_from_wishlist, view_wishlist

urlpatterns = [
    path('add-to-wishlist/<int:product_id>/', add_to_wishlist, name='add_to_wishlist'),
    path('remove-from-wishlist/<int:wishlist_item_id>/', remove_from_wishlist, name='remove_from_wishlist'),
    path('view_wishlist/', view_wishlist, name='view_wishlist'),
]