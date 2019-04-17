from django.conf.urls import patterns, url

from thing import views

from rest_framework import routers, serializers, viewsets



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /thing/5/
    url(r'^(?P<thing_id>\d+)/$', views.detail, name='detail'),
    # ex: /thing/5/results/
    url(r'^(?P<thing_id>\d+)/results/$', views.results, name='results'),
    # ex: /thing/5/vote/
    url(r'^(?P<thing_id>\d+)/vote/$', views.vote, name='vote'),
)
