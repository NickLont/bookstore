from __future__ import unicode_literals
from django.db import models
# from django.contrib.auth import User

class Category(models.Model):
	SATIRE = 'sat'
	DRAMA = 'dra'
	ACTION = 'act'
	MYSTERY = 'mys'
	CHILDRENS = 'chi'
	TRAVEL = 'tra'
	BIOGRAPHY = 'bio'
	CATEGORY_CHOICES = ((SATIRE, 'Satire'),(DRAMA, 'Drama'), (ACTION, 'Action'), (MYSTERY, 'Mystery'), 
						(CHILDRENS, 'Childrens'), (TRAVEL, 'Travel'), (BIOGRAPHY, 'Biography'))

	name = models.CharField(max_length=3, choices = CATEGORY_CHOICES, default=ACTION)
	info = models.CharField(max_length=50, blank=True) 

	class Meta:
		verbose_name = "Category"
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.get_name_display()
	def __unicode__(self):
		return self.get_name_display()


class Book(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	title = models.CharField(max_length=50)
	isbn = models.CharField(max_length=50, unique=True)
	price = models.DecimalField(max_digits=5, decimal_places=1, default=0)

	class Meta:
		verbose_name = "Book"
		verbose_name_plural = "Books"

	def __str__(self):
		return self.title

# class CartBook(models.Model):
# 	cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
# 	book = models.ForeignKey(Book)

# class Cart(models.Model):
# 	user = models.ForeignKey(User)
# 	name = models.CharField(max_length=50)



	