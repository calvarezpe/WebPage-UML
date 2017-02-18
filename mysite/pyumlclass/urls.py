from django.conf.urls import url

from . import views

app_name = 'pyumlclass'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archive/$', views.archive, name='archives'),
    url(r'^results/$', views.results, name='results')
]
