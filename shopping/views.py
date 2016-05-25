from django.http import HttpResponse
from django.shortcuts import render
from carton.cart import Cart
from bookstore.models import Book
from django.contrib.sessions.models import Session

def show(request):
	cart = Cart(request.session)	
	if request.method == 'POST':
		print 'mpike mesa sto post'
		isbn = request.POST.get("book_isbn",'')
		quant = request.POST.get("book_new_quant",'')
		product = Book.objects.get(isbn=isbn)
		cart.set_quantity(product, quantity=quant)
		return render(request, 'shopping/show-cart.html')
	else:
		return render(request, 'shopping/show-cart.html')

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



