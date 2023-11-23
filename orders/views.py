from django.shortcuts import render
from django.views.generic import DetailView
from .models import Order

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'
    pk_url_kwarg = 'order_id'