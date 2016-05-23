from django.conf.urls import url
from . import views
from .views import BookListView
from django.contrib.auth.decorators import login_required

app_name = 'soap'
urlpatterns = [
    url(r'^$', login_required(BookListView.as_view()), name='book-list' ),
    url(r'^(?P<isbn>[0-9]+)/$', views.quantityDetails , name='soapDetailed' ),
]