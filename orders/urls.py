from django.urls import path
from .views import OrderDetailView, MakeOrderView

urlpatterns = [
    path('order/<int:order_id>/', OrderDetailView.as_view(), name='order_detail'),
    path('make_order/', MakeOrderView.as_view(), name='make-order'),
    
]