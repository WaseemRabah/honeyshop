from django.urls import path
from .views import WishlistView, WishlistActionView

app_name = 'wishlist'

urlpatterns = [
    path('wishlist/', WishlistView.as_view(), name='wishlist'),
    path('wishlist-action/<int:product_id>/<str:action>/', WishlistActionView.as_view(), name='wishlist_action'),
    
]