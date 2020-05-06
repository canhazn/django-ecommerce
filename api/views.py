from django.shortcuts import render
from .models import *
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .forms import *

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    return Response({"mess": "hello"})

@api_view(['GET'])
def ProductList(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print(serializer.data)
    return Response(serializer.data)

@api_view(['POST'])
def OrderCreate(request):
    # order = request.data
    order = {
        "customer" : "Anh nguyen",
        "phone" : "0963697819",
        "shipping_address" : "dai dinh, tam dao",
        "order_items" : [
            {
                "product_id" : 1,
                "quantity": 1
            },
            {
                "product_id" : 2,
                "quantity": 1
            }
        ]
    }

    # -------- save order 
    # order = {
    #     "customer" : "Tuan nguyen",
    #     "phone" : "0963697819",
    #     "shipping_address" : "dai dinh, tam dao",
    # }

    # new_order = OrderForm(data=order)
    # print(new_order.is_valid())
    # new_order.save()

    # -------- end save order 

    # -------- save order items


    for item in order["order_items"]:        
        currentProduct = Product.objects.get(id=item["product_id"])
        currentOrder  = Order.objects.get(id=3)
        newOrderItem = OrderItemForm(data={
            "product": currentProduct,
            "order": currentOrder,
            "quantity": item["quantity"]
        })
        newOrderItem.save()
        print(newOrderItem)


    return Response({})