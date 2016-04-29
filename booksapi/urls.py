from django.conf.urls import url
from . import views

app_name = 'booksapi'
urlpatterns = [
    url(r'^$', views.searchIndex, name='searchIndex' ),
    url(r'^(?P<isbn>[0-9]+)/$', views.search, name='apiSearch'),
]