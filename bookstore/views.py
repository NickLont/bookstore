from django.shortcuts import render
from sortable_listview import SortableListView
from django.views.generic.detail import DetailView
from .models import Book
import json, urllib2
from suds.client import Client
from registration.backends.simple.views import RegistrationView


soap_client = Client('http://localhost:8080/bookQntWS/bookWS?wsdl')

def index(request):
	book1 = Book.objects.get(isbn=9780345339706)
	book2 = Book.objects.get(isbn=9780307277671)
	book3 = Book.objects.get(isbn=9780446310789)
	book4 = Book.objects.get(isbn=9780141380322)
	context = {'book1':book1, 'book2':book2, 'book3':book3, 'book4':book4}

	return render(request, 'bookstore/index.html', context)

class BookListView(SortableListView):
	default_sort_field = 'title'
	allowed_sort_fields = {default_sort_field: {'default_direction': '-',
                                                'verbose_name': 'Title'},
					        'category':{'default_direction': '',
					        			'verbose_name': 'Category'},
					        'price':{'default_direction': '',
					        			'verbose_name': 'Price'}}                                       
	paginate_by = 10
	model = Book
	template_name = "bookstore/list.html"    

def details(request, isbn):
	data = json.load(urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn))
	book = Book.objects.get(isbn=isbn)
	results = soap_client.service.findByIsbn(isbn)
	if 'imageLinks' in data['items'][0]['volumeInfo']:
		pic = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
	else:		
		pic='http://www.clker.com/cliparts/q/L/P/Y/t/6/no-image-available-md.png'
	context={'pic':pic, 'book':book, 'results':results}
	return render(request, 'bookstore/details.html', context)

def about(request):
	return render(request, 'bookstore/about.html')

