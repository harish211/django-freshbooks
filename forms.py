from django import forms
from freshbooks.django_freshbooks.models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client