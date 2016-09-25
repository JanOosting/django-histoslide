from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^slide/(?P<slide_id>\d+)/$', views.slide),
    url(r'^(?P<slug>\d+).dzi$', views.dzi),
    url(r'^(?P<slug>\d+).dzi.json$', views.properties),
    url(r'^(?P<slug>\d+)_files/(?P<level>\d+)/(?P<col>\d+)_(?P<row>\d+)\.(?P<slideformat>jpeg|png)$', views.dztile),
    url(r'^(?P<slug>\d+)_map/(?P<level>\d+)/(?P<col>\d+)_(?P<row>\d+)\.(?P<slideformat>jpeg|png)$', views.gmtile),
]
