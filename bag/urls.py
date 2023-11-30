from django.urls import path
from . import views
from .views import CartView, view_cart



urlpatterns = [
    path('add_to_bag/<int:item_id>/', views.add_to_bag, name='add_to_bag'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove-from-cart'),
    path('view-cart/', view_cart, name='view-cart'),
    path('make-order/', views.make_order, name='make-order'),
    path('cart/', views.view_cart, name='cart'),
]
