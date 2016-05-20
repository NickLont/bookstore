from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from bookstore.models import Book


def add(request,isbn):
    cart = Cart(request.session)
    product = Book.objects.get(isbn=isbn)
    cart.add(product, price=product.price)
    return render(request, 'shopping/show-cart.html')


def remove(request,isbn):
    cart = Cart(request.session)
    product = Book.objects.get(isbn=isbn)
    cart.remove(product)
    return render(request, 'shopping/show-cart.html')


def show(request):
    return render(request, 'shopping/show-cart.html')
