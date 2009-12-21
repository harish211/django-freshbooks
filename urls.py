from django.conf.urls.defaults import *
from django_freshbooks.views import *

urlpatterns = patterns('',
    url(r'^(?P<form_type>\w+)/$', form_justin, name='form_create'),
    url(r'^(?P<form_type>\w+)/(?P<object_id>\d+)/$', form_justin, name='form_edit'),
    url(r'^(?P<type>\w+)/list/$', list, name='list'),
    url(r'^added/(?P<form_type>\w+)/$', form_added, name='form_added'),
)
