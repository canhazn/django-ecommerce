from django.urls import path
from . import views

urlpatterns = [
   path('', views.ApiOverview, name="api-overview"),
   path('product-list/', views.ProductList, name="product-list")
]
