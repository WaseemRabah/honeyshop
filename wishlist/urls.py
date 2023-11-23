from django.urls import path
from .views import WishlistListView, WishlistDetailView, add_to_wishlist, WishlistCreateView

app_name = 'wishlist'

urlpatterns = [
    path('list/', WishlistListView.as_view(), name='wishlist-list'),
    path('detail/<int:pk>/', WishlistDetailView.as_view(), name='wishlist-detail'),
    path('add/<int:product_id>/', add_to_wishlist, name='add-to-wishlist'),
    path('create/', WishlistCreateView.as_view(), name='wishlist-create'),
    
]