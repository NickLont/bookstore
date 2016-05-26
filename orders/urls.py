from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'orders'
urlpatterns = [
    url(r'^create/$', views.order_create , name='order_create' ),
    url(r'^order/(?P<order_id>\d+)$', login_required(views.order_show), name='order_detailed' ),
    url(r'^orderPDF/(?P<order_id>\d+)$', login_required(views.order_show_as_pdf), name='order_pdf' ),
    url(r'^history/$', login_required(views.show_history) , name='show_history' ),
]