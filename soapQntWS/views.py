from django.shortcuts import render
from django.views.generic.list import ListView
from bookstore.models import Book
from suds.client import Client
import json, urllib2
from .forms import quantityChange



soap_client = Client('http://localhost:8080/bookQntWS/bookWS?wsdl')


class BookListView(ListView):
	model = Book
	template_name = 'soapQntWS/quantList.html'

def quantityDetails(request, isbn):
	data = json.load(urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn))
	book = Book.objects.get(isbn=isbn)
	if 'imageLinks' in data['items'][0]['volumeInfo']:
		pic = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
	else:		
		pic='http://www.clker.com/cliparts/q/L/P/Y/t/6/no-image-available-md.png'
	if request.method == 'POST':
		form = quantityChange(request.POST)
		if form.is_valid():
			change = soap_client.service.updateQuantity(isbn, form.cleaned_data['quantity_input'])
			results = soap_client.service.findByIsbn(isbn)
			context={'pic':pic, 'book':book, 'results':results, 'form':form, 'change':change}
	else:
		results = soap_client.service.findByIsbn(isbn)
		form = quantityChange()		
		context={'pic':pic, 'book':book, 'results':results, 'form':form}
	return render(request, 'soapQntWS/details.html', context)