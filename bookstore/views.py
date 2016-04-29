from django.shortcuts import render
from sortable_listview import SortableListView
from django.views.generic.detail import DetailView
from .models import Book
import json, urllib2

def index(request):
	return render(request, 'bookstore/index.html')

class BookListView(SortableListView):
	default_sort_field = 'title'
	allowed_sort_fields = {default_sort_field: {'default_direction': '-',
                                                'verbose_name': 'Title'},
					        'category':{'default_direction': '',
					        			'verbose_name': 'Categories'},
					        'price':{'default_direction': '',
					        			'verbose_name': 'Price'}}                                       
	paginate_by = 5
	model = Book
	template_name = "bookstore/list.html"    

def details(request, isbn):
	data = json.load(urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn))
	# pic = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
	book = Book.objects.get(isbn=isbn)
	if 'imageLinks' in data['items'][0]['volumeInfo']:
		pic = data['items'][0]['volumeInfo']['imageLinks']['thumbnail']
	else:		
		pic='http://www.clker.com/cliparts/q/L/P/Y/t/6/no-image-available-md.png'
	context={'pic':pic, 'book':book}
	return render(request, 'bookstore/details.html', context)