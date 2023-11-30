from django.urls import path
from .views import DisplayBagView, AddToBagView, AdjustBagView, RemoveFromBagView

app_name = 'bag'

urlpatterns = [
    path('display_bag/', DisplayBagView.as_view(), name='display_bag'),
    path('add/<item_id>/', AddToBagView.as_view(), name='add_to_bag'),
    path('adjust/<item_id>/', AdjustBagView.as_view(), name='adjust_bag'),
    path('remove/<item_id>/', RemoveFromBagView.as_view(), name='remove_from_bag'),
    # path('make-order/', views.MakeOrderView.as_view(), name='make_order'),
]
