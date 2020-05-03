from django.shortcuts import render

def storePage(request):
    return render(request, 'store/store.html')

def cartPage(request):
    return render(request, 'store/cart.html')

def checkoutPage(request):
    return render(request, 'store/checkout.html')