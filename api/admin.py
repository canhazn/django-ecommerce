from django.contrib import admin
from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Product, ProductAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'completed', 'phone', 'shipping_address', 'date_ordered')

admin.site.register(Order, OrderAdmin)


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'order','getOrderCompleted' ,'quantity')

    def getOrderCompleted(self, obj):
        return bool(obj.order.completed)
    
    getOrderCompleted.short_description = "completed"

admin.site.register(OrderItem, OrderItemAdmin)