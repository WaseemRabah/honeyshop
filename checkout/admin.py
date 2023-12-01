from django.contrib import admin
from .models import Order, OrderLineItem

class OrderLineItemInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('product_name', 'quantity', 'price', 'total_price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'full_name', 'email', 'created_at', 'updated_at', 'is_completed']
    list_filter = ['is_completed']
    inlines = [OrderLineItemInline]
    search_fields = ['order_number', 'full_name', 'email']

    def order_number(self, obj):
        return obj.order_number
    order_number.short_description = 'Order Number'

    def full_name(self, obj):
        return obj.full_name
    full_name.short_description = 'Full Name'

    def email(self, obj):
        return obj.email
    email.short_description = 'Email'

admin.site.register(Order, OrderAdmin)
