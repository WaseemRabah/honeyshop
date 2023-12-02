from django.urls import path
from .views import checkout, checkout_success

urlpatterns = [
    path('checkout/', checkout, name='checkout'),
    path('checkout/success/<uuid:order_number>/', checkout_success, name='checkout_success'),
]
