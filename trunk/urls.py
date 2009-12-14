from django.conf.urls.defaults import *
from django_freshbooks.views import *
urlpatterns = patterns('',
    url(r'^create/(?P<form_type>\w+)/$', form_create, name='form_create'),
    url(r'^create_inline/(?P<form_type>\w+)/$', inline_form_create, name='inline_form_create'),
    url(r'^added/(?P<form_type>\w+)/$', form_added, name='form_added'),
)
