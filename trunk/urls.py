from django.conf.urls.defaults import *
from django_freshbooks.views import *
urlpatterns = patterns('',
    (r'^client/create/', client_create),
    (r'^client/added/', client_added),
    (r'^category/create/', category_create),
    (r'^category/added/', category_added),
)
