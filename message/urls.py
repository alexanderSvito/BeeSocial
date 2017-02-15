from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.dialogs, name='dialogs'),
    url(r'^(?P<id>\d+?)$', views.messages, name='messages'),
    url(r'^test$', views.test, name='test'),
]