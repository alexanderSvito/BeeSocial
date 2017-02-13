from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^messages/$', views.dialogs, name='dialogs'),
    url(r'^messages/(?P<id>\d+?)$', views.messages, name='messages'),
    url(r'^test/$', views.test, name='test'),
]