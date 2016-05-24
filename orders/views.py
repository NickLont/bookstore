from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from carton.cart import Cart
from django.contrib.sessions.models import Session
from django.conf import settings
from django.shortcuts import get_object_or_404



def order_create(request):
	cart = Cart(request.session)
	if request.method == 'POST':
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save(commit=False)
			order.placed_by_user = request.user
			order.save()
			for item in cart.items:
				OrderItem.objects.create(order=order,
											product=item.product,
											price=item.price,
											quantity=item.quantity)
			cart.clear()
			context={'order': order}	
			return render(request, 'orders/created.html', context)
	else:
		form = OrderCreateForm()
		return render(request, 'orders/create.html', {'cart': cart, 'form': form})	

def order_show(request, order_id):
	order = get_object_or_404(Order, id=order_id)
	context={'order': order}		
	return render(request, 'orders/invoice.html', context)