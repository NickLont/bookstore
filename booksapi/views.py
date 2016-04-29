from django.shortcuts import render, redirect
from django.http import HttpResponse
import json, urllib2

def searchIndex(request):
	return render(request, 'booksapi/searchIndex.html')

def search(request, isbn):	
	data = json.load(urllib2.urlopen('https://www.googleapis.com/books/v1/volumes?q=isbn:'+isbn))
	url = data['items'][0]['accessInfo']['webReaderLink']
	return redirect(url)
