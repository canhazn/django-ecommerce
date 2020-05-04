from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
