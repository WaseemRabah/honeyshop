from django.urls import path
from .views import SubscribeView, SuccessPageView


urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('success/', SuccessPageView.as_view(), name='success_page'),
]
