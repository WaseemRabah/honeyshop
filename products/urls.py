from django.urls import path
from .views import review_detail
from .views import (
    all_products,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    AddReviewView,
    EditReviewView, 
    DeleteReviewView,
)

urlpatterns = [
    path('', all_products, name='products'),
    path('category/<slug:category_slug>/', ProductListView.as_view(), name='product_list_by_category'),
    path('products/<slug:product_slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:product_id>/add_review/', AddReviewView.as_view(), name='add_review'),
    path('products/reviews/edit/<int:product_id>/', EditReviewView.as_view(), name='edit_review'),
    path('products/reviews/delete/<int:pk>/', DeleteReviewView.as_view(), name='delete_review'),
    path('reviews/<int:pk>/', review_detail, name='review_detail'),
]