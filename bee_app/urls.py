from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^messages/$', views.messages, name='messages'),
    url(r'^test/$', views.test, name='test'),
]