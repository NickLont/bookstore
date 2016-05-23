from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from bookstore.models import Book, CartBook
from bookstore.models import Cart as MyCart
from django.contrib.sessions.models import Session



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
	# print request.session['cart']
	# s= Cart(request.session)
	# print s.count
	return render(request, 'shopping/show-cart.html')

def checkout(request ):
    #cmd: take user from request.session
    #cmd: take cart from request.session
    #cmd: take products from cart
    #cmd: create MyCart me ton user kai to cart
    #cmd: for loop gia na kaneis create ola ta CartBook me ta products kai to cart
    print request.session
    return render(request, 'shopping/show-cart.html')
