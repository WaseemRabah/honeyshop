# Generated by Django 4.2.7 on 2023-12-02 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_order_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_amount',
        ),
    ]
