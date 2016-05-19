from django.conf.urls import url
from . import views
from .views import BookListView

app_name = 'bookstore'
urlpatterns = [
    url(r'^$', views.index, name='index' ),
    url(r'^list/$', BookListView.as_view(), name='list' ),
    url(r'^(?P<isbn>[0-9]+)/$', views.details, name='detailedView'),
    url(r'^about/$', views.about, name='about' ),
]