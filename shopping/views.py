from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from bookstore.models import Book
# from bookstore.models import Cart as MyCart
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
	cart = Cart(request.session)
	for item in cart.items:
		print "product: ",item.product
		print "price: ", item.price
		print "quantity: ", item.quantity
	return render(request, 'shopping/show-cart.html')

# def checkout(request ):
#     #cmd: take user from request.session
#     #cmd: take cart from request.session
#     #cmd: take products from cart
#     #cmd: create MyCart me ton user kai to cart
#     #cmd: for loop gia na kaneis create ola ta CartBook me ta products kai to cart
#     print request.session
#     return render(request, 'shopping/show-cart.html')
