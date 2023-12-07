from django.db import models

class Subscriber(models.Model):
    name = models.CharField(max_length=255, default='')
    email = models.EmailField(unique=True)
    interest = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.email