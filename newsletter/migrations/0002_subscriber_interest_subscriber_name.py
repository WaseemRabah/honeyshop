# Generated by Django 4.2.7 on 2023-12-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriber',
            name='interest',
            field=models.CharField(default='General Interest', max_length=255),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='name',
            field=models.CharField(default='Anonymous User', max_length=255),
        ),
    ]
