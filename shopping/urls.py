from django.conf.urls import url, patterns
from . import views

app_name = 'shopping'
urlpatterns = [
    url(r'^add/(?P<isbn>[0-9]+)$', views.add, name='shopping-cart-add'),
    url(r'^remove/(?P<isbn>[0-9]+)$', views.remove, name='shopping-cart-remove'),
    url(r'^show/$', views.show, name='shopping-cart-show'),
    url(r'^checkout/$', views.checkout, name='shopping-cart-checkout'),
]	

