from django.db import models
import datetime

# Create your models here.

class Product(models.Model):
    name  = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.name

class Order(models.Model):
    customer         = models.CharField(max_length=200)
    phone            = models.CharField(max_length=20, null=True)
    shipping_address = models.CharField(max_length=200)
    date_ordered     = models.DateTimeField(auto_now_add=True)
    completed        = models.BooleanField(default=False)

    # def __init__(self, customer, phone, shipping_address):
    #     self.customer = customer
    #     self.phone    = phone
    #     self.shipping_address = shipping_address
    #     self.completed = False
    #     self.date_ordered = datetime.datetime.now()

    @property
    def get_card_total(self):
        orderitems = orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    def __str__(self):
        return str(self.id) + " - " +str(self.customer) + " - " + str(self.phone)

class OrderItem(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order    = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

    def __str__(self):
        return self.product.name

