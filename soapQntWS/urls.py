from django.conf.urls import url
from . import views
from .views import BookListView

app_name = 'soap'
urlpatterns = [
    url(r'^$', BookListView.as_view(), name='book-list' ),
    url(r'^(?P<isbn>[0-9]+)/$', views.quantityDetails , name='soapDetailed' ),
]