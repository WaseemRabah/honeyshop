from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('orders/', include(('orders.urls', 'orders'))),
    path('wishlist/', include('wishlist.urls')),
    path('bag/', include('bag.urls', namespace='bag')),
    path('checkout/', include('checkout.urls', namespace='checkout')),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.account.urls')),
]
