from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .models import Wishlist, WishlistItem
from products.models import Product
from django.urls import reverse_lazy

class WishlistListView(LoginRequiredMixin, ListView):
    model = Wishlist
    template_name = 'wishlist/wishlist_list.html'
    context_object_name = 'wishlists'

    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_products'] = Product.objects.all()  
        return context

class WishlistDetailView(LoginRequiredMixin, DetailView):
    model = Wishlist
    template_name = 'wishlist/wishlist_detail.html'
    context_object_name = 'wishlist'

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user=request.user)
    WishlistItem.objects.create(wishlist=wishlist, product=product)
    return redirect('wishlist:wishlist-list')

class WishlistCreateView(LoginRequiredMixin, CreateView):
    model = Wishlist
    template_name = 'wishlist/wishlist_form.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('wishlist:wishlist-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
