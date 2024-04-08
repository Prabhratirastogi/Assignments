from django.db import models
from django.core.validators import EmailValidator
import re
from django.core.exceptions import ValidationError


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length =255)
    email = models.EmailField()
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username
    

class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name