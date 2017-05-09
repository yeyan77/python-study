from django.conf.urls import url
from django.contrib import admin

from . import view,testdb,search,array

urlpatterns = [
    url(r'^hello$',view.hello),
    url(r'^testdb$',testdb.testdb),
    url(r'^search-form$',search.search_form),
    url(r'^search$',search.search),
    url(r'^admin/',admin.site.urls),

    url(r'^array$',array.array),
    url(r'^array-form$',array.array_form),

]