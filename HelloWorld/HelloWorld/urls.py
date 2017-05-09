from django.conf.urls import url
from . import view,testdb

urlpatterns = [
    url(r'^hello$',view.hello),
    url(r'^testdb$',testdb.testdb),
]