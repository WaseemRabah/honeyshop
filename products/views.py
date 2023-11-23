from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView, DetailView
from .models import Category, Product

class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    model = Product

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            return Product.objects.filter(category=category, stock__gt=0, user=self.request.user)
        else:
            return Product.objects.filter(stock__gt=0, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs.get('category_slug')
        
        if category_slug:
            context['category'] = get_object_or_404(Category, slug=category_slug)
        else:
            context['category'] = None

        return context

class ProductDetailView(DetailView):
    template_name = 'products/product_detail.html'
    model = Product
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(stock__gt=0)
