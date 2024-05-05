from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import handler404, handler500



urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(('products.urls', 'products'))),
    path('orders/', include(('orders.urls', 'orders'))),
    path('wishlist/', include('wishlist.urls')),
    path('bag/', include(('bag.urls', 'bag'), namespace='bag')),
    path('checkout/', include(('checkout.urls', 'checkout'), namespace='checkout')),
    path('', include('home.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('allauth.account.urls')),
    path('newsletter/', include('newsletter.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'ecommerceproject.views.handler404'
handler500 = 'ecommerceproject.views.handler500'