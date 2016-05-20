from django.conf.urls import url, patterns

app_name = 'shopping'
urlpatterns = patterns('shopping.views',
    url(r'^add/(?P<isbn>[0-9]+)$', 'add', name='shopping-cart-add'),
    url(r'^remove/(?P<isbn>[0-9]+)$', 'remove', name='shopping-cart-remove'),
    url(r'^show/$', 'show', name='shopping-cart-show'),
)

