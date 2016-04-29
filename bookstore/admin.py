from django.contrib import admin
from . models import Book

class BookAdmin(admin.ModelAdmin):
	model = Book
	list_display = ['title', 'isbn', 'category']
	search_fields = ['title', 'isbn']
	list_filter = ['category']
	ordering = ['title']

admin.site.register(Book, BookAdmin)