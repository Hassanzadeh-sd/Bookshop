from django.conf.urls import url
from . import views

app_name= "app"

urlpatterns = [
    # ex : /book/
    url(r'^$', views.listview, name="book_listview"),
    # ex: /book/5/
    url(r'^(?P<pk>[0-9]+)/$', views.detail, name="book_detail"),
]