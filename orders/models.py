from django.db import migrations, models
from django.contrib.auth.models import User
from products.models import Product
from django.utils import timezone

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order_number = models.CharField(max_length=20, default=timezone.now)

    def save(self, *args, **kwargs):
        # Generate a unique order number before saving the order
        if not self.order_number:
            self.order_number = self.generate_order_number()
        super().save(*args, **kwargs)

    def generate_order_number(self):
        # Generate a unique order number based on the current timestamp
        timestamp_str = self.created_at.strftime('%Y%m%d%H%M%S')
        user_id_str = str(self.user.id).zfill(5) 
        return f'{timestamp_str}-{user_id_str}'
    

def generate_default_order_number(apps, schema_editor):
    Order = apps.get_model('orders', 'Order')
    for order in Order.objects.all():
        order.order_number = order.generate_order_number()
        order.save()

class Migration(migrations.Migration):

    dependencies = [
        
    ]

    operations = [
        migrations.RunPython(generate_default_order_number),
        migrations.AddField(
            model_name='order',
            name='order_number',
            field=models.CharField(max_length=20, unique=True, default=''),
        ),
    ]

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
