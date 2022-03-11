from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.


class product(models.Model):
    name = models.CharField(max_length=32)
    price = models.IntegerField(default=100)
    buy = models.IntegerField(default=100)
    number = models.IntegerField(default=1)
    def __str__(self):
        return f'{self.name}({self.price})'

class customer(models.Model):
    author = models.CharField(max_length=32)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=32)
    basket = models.ManyToManyField(product)
    def __str__(self):
        return f'{self.author}({self.phone})'
