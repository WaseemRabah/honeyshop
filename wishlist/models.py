from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product,blank=True,related_name='wishlist')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username}'s Wishlist"


    def add_to_wishlist(self, product):
        """
        Add a product to the wishlist.

        Parameters:
        - product: The product instance to be added to the wishlist.
        """
        self.products.add(product)


    def remove_from_wishlist(self, product):
        """
        Remove a product from the wishlist.

        Parameters:
        - product: The product instance to be removed from the wishlist.
        """
        self.products.remove(product)


    def get_all_products(self):
        """
        Get all products in the wishlist.

        Returns:
        - QuerySet: A queryset containing all products in the wishlist.
        """
        return self.products.all()