from django.contrib import admin
from .models import Order, OrderItem
from django.core.urlresolvers import reverse

class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

# def order_detail(obj):
# 	return '<a href="{}">View</a>'.format(reverse('orders:order_detailed', args[obj.id]))
# order_detail.allow_tags = True	


class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'placed_by_user','last_name', 'email','address', 'postal_code', 'city', 'paid',
					'created', 'updated']
	list_filter = ['paid', 'created', 'updated']
	inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)