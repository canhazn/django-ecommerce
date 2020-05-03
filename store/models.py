from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    user  = models.OneToOneField(User, on_delete=models.SET_NULL)
    name  = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name  = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer     = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed    = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=200)

    # def __str__(self):
    #     return str(self.id)

class OrderItem(models.Model):
    product    = models.ForeignKey(Product, on_delete=models.SET_NULL)
    order      = models.ForeignKey(Order, on_delete=models.SET_NULL)
    quantity   = models.IntegerField(default=0)    

class ShippingAddress(models.Model):
    customer   = models.ForeignKey(Customer, on_delete=models.SET_NULL)
    order      = models.ForeignKey(Order, on_delete=models.SET_NULL)
    address    = models.CharField(max_length=200)    

    def __str__(self):
        return self.address

