from django.shortcuts import render
from django.views.generic.list import ListView
from bookstore.models import Book
from suds.client import Client
import json, urllib2



soap_client = Client('http://localhost:8080/bookQntWS/bookWS?wsdl')


class BookListView(ListView):
	model = Book
	template_name = 'soapQntWS/quantList.html'

def quantityDetails(request, isbn):
	data = json.load(urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn))
	book = Book.objects.get(isbn=isbn)
	results = soap_client.service.findByIsbn(isbn)
	print results
	if 'imageLinks' in data['items'][0]['volumeInfo']:
		pic = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
	else:		
		pic='http://www.clker.com/cliparts/q/L/P/Y/t/6/no-image-available-md.png'
	context={'pic':pic, 'book':book, 'results':results}
	return render(request, 'soapQntWS/details.html', context)