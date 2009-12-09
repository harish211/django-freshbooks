from django.contrib import admin
from django_freshbooks.models import *

class ClientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client,ClientAdmin)