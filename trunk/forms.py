from django import forms
from django_freshbooks.models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client