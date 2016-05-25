from django.http import HttpResponse
from django.shortcuts import render

from carton.cart import Cart
from bookstore.models import Book
from django.contrib.sessions.models import Session



def add(request):
    cart = Cart(request.session)
    isbn = request.POST.get("book_isbn", "")
    product = Book.objects.get(isbn=isbn)
    cart.add(product, price=product.price)
    return render(request, 'shopping/show-cart.html')


def remove(request):
    cart = Cart(request.session)
    isbn = request.POST.get("book_isbn",'')
    product = Book.objects.get(isbn=isbn)
    cart.remove(product)
    return render(request, 'shopping/show-cart.html')


def show(request):
	cart = Cart(request.session)
	# for item in cart.items:
	# 	print "product: ",item.product
	# 	print "price: ", item.price
	# 	print "quantity: ", item.quantity
	if request.method == 'POST':
		isbn = request.POST.get("book_isbn",'')
		quant = request.POST.get("book_new_quant",'')
		product = Book.objects.get(isbn=isbn)
		cart.set_quantity(product, quantity=quant)

	return render(request, 'shopping/show-cart.html')
