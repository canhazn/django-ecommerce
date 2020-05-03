from django.urls import path
from . import views


urlpatterns = [
    path('', views.storePage, name='store-page'),
    path('cart-page/', views.cartPage, name='cart-page'),
    path('checkout-page/', views.checkoutPage, name='checkout-page')
]
