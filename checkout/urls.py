from django.urls import path
from .views import checkout, checkout_success
from .webhooks import webhook
from . import views

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('checkout/success/<uuid:order_number>/', checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
