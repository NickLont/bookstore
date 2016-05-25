from django.conf.urls import url, patterns
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'shopping'
urlpatterns = [
    url(r'^add/(?P<isbn>[0-9]+)$', login_required(views.add), name='shopping-cart-add'),
    url(r'^remove/(?P<isbn>[0-9]+)$', login_required(views.remove), name='shopping-cart-remove'),
    url(r'^show/$', login_required(views.show), name='shopping-cart-show'),
    # url(r'^checkout/$', views.checkout, name='shopping-cart-checkout'),
]	

