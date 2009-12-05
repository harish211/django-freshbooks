from django.conf.urls.defaults import *
urlpatterns = patterns('',
    (r'^client/create/', 'freshbooks.django_freshbooks.views.client_create'),
    (r'^client/added/', 'freshbooks.django_freshbooks.views.client_added'),
)
