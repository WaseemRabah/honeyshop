from django.shortcuts import render,  redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Avg
from django.views import View
from django.views.generic import CreateView, ListView, DetailView
from .models import Category, Product, Review
from .forms import ProductForm, ReviewForm
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.db.models.functions import Lower 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


""" A view to show all products, including sorting and search queries """
def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
            
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


class ProductListView(ListView):
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    model = Product

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(Category, slug=category_slug)
            return Product.objects.filter(stock__gt=0, user=self.request.user)
        else:
            return Product.objects.filter(stock__gt=0)

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
    slug_url_kwarg = 'product_slug'

    def get_queryset(self):
        return Product.objects.filter(stock__gt=0)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        reviews = Review.objects.filter(product=product)
        avg_rating = reviews.aggregate(Avg('stars'))['stars__avg']
        
        # Pre-render stars
        for review in reviews:
            review.full_stars = range(review.stars)
            review.empty_stars = range(5 - review.stars)
        
        context['reviews'] = reviews
        context['avg_rating'] = avg_rating
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('products:product_list')  
    template_name = 'products/product_confirm_delete.html'


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        
        user_review = Review.objects.filter(product=product, user=request.user)
        if user_review.exists():
            messages.error(request, 'You have already given your review on this product.')
            return redirect('products:product_detail', product_slug=product.slug)
        
        form = ReviewForm(request.POST)
        if form.is_valid():
            stars = form.cleaned_data['stars']
            comment = form.cleaned_data['comment']
            user = request.user 
            review = Review(product=product, stars=stars, comment=comment, user=user) 
            review.save()
            return redirect('products:product_detail', product_slug=product.slug)
        else:
            
            return render(request, 'products/product_detail.html', {'form': form, 'product': product})

    def get(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        form = ReviewForm()
        return render(request, 'products/product_detail.html', {'form': form, 'product': product})
    

class EditReviewView(LoginRequiredMixin, UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'products/edit_review.html'
    slug_url_kwarg = 'review_id'
    slug_field = 'id'
    pk_url_kwarg = 'product_id'

    def get_success_url(self):
        product_slug = self.object.product.slug
        return reverse('products:product_detail', kwargs={'product_slug': product_slug})

    def form_valid(self, form):
        return super().form_valid(form)


    
class DeleteReviewView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'products/delete_review.html'

    def get_success_url(self):
        product_slug = self.object.product.slug
        return reverse('products:product_detail', kwargs={'product_slug': product_slug})

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        review = self.get_object()
        product = review.product
        
        # Get all reviews for the product except the one being deleted
        remaining_reviews = Review.objects.filter(product=product).exclude(pk=review.pk)
        
        # Recalculate the average rating
        new_avg_rating = remaining_reviews.aggregate(Avg('stars'))['stars__avg']
        
        # Update the product's average rating
        product.avg_rating = new_avg_rating
        product.save()
        
        messages.success(request, 'Your review has been deleted.')
        return super().delete(request, *args, **kwargs)
    
def review_detail(request, pk):
    review = get_object_or_404(Review, pk=pk)
    return render(request, 'products/review_detail.html', {'review': review})