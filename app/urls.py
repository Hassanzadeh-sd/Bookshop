from django.conf.urls import url
from . import views

app_name= "app"

urlpatterns = [
    # ex : /book/
    url(r'^$', views.Index, name="Index"),
    # ex : /book/list
    url(r'^list/$', views.Book_list, name="book-list"),
    # ex : /book/1/
    url(r'^(?P<pk>[0-9]+)/$', views.Book_detail, name="book-detail"),
    # ex : /author/
    url(r'^author/$', views.Author, name="author"),
    # ex : /author/1/
    url(r'^author/(?P<pk>[0-9]+)/$', views.Author_detail, name="author-detail"),
]