# models.py

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum, F, DecimalField
from django.conf import settings


class Order(models.Model):
    order_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')
    
    # Customer Information
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    
    # Shipping Address
    street_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    county = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    # Delivery Cost
    delivery_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def generate_order_number(self):
        return str(uuid.uuid4()).split('-')[0]
    
    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        total_price_sum = self.orderlineitem_set.annotate(
            total_price=Sum(F('quantity') * F('price'), output_field=DecimalField())
        ).aggregate(Sum('total_price'))['total_price__sum'] or 0

        self.order_total = total_price_sum
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.order_number)



class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def total_price(self):
        if self.price is not None and self.quantity is not None:
            return self.quantity * self.price
        return 0

    def __str__(self):
        return f"{self.quantity} x {self.product_name} in Order {self.order.order_number}"
