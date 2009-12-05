from django import forms
from freshbooks.django_freshbooks import api 
from freshbooks.django_freshbooks.settings import *

class ClientForm(forms.Form):
    def clean(self):
        cleaned_data = self.cleaned_data
        api.setup(FRESHBOOKS_URL,FRESHBOOKS_TOKEN);
        client = api.Client()
        
        for key,value in self.cleaned_data.items():
            setattr(client, key, value)
        """
        client.first_name = cleaned_data['first_name']
        client.last_name = cleaned_data['last_name']
        client.organization = cleaned_data['organization']
        client.email = cleaned_data['email']
        client.username = cleaned_data['username']
        client.password = cleaned_data['password']
        client.work_phone = cleaned_data['work_phone']
        client.home_phone = cleaned_data['home_phone']
        client.mobile = cleaned_data['mobile']
        client.fax = cleaned_data['fax']
        client.notes = cleaned_data['notes']
        client.p_street1 = cleaned_data['p_street1']
        client.p_street2 = cleaned_data['p_street2']
        client.p_city = cleaned_data['p_city']
        client.p_state = cleaned_data['p_state']
        client.p_country = cleaned_data['p_country']
        client.p_code = cleaned_data['p_code']
        client.s_street1 = cleaned_data['s_street1']
        client.s_street2 = cleaned_data['s_street2']
        client.s_city = cleaned_data['s_city']
        client.s_state = cleaned_data['s_state']
        client.s_country = cleaned_data['s_country']
        client.s_code = cleaned_data['s_code']
        """
        
        try:
            response = api.call_api("client.create", {None:client})
        except Exception as msg:
            raise forms.ValidationError(msg)
        
        
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    organization = forms.CharField(max_length=100)
    email = forms.EmailField()
    username = forms.CharField(max_length=50, required=False)
    password = forms.CharField(max_length=10,min_length=6,widget=forms.PasswordInput(render_value=False), required=False)
    work_phone = forms.CharField(min_length=10,max_length=20,required=False)
    home_phone = forms.CharField(min_length=10,max_length=20,required=False)
    mobile = forms.CharField(min_length=10,max_length=20,required=False)
    fax = forms.CharField(min_length=10,max_length=20,required=False)
    notes = forms.CharField(required=False,widget=forms.Textarea)
    p_street1 = forms.CharField(required=False)
    p_street2 = forms.CharField(required=False)
    p_city = forms.CharField(required=False)
    p_state = forms.CharField(required=False)
    p_country = forms.CharField(required=False)
    p_code = forms.CharField(required=False)
    s_street1 = forms.CharField(required=False)
    s_street2 = forms.CharField(required=False)
    s_city = forms.CharField(required=False)
    s_state = forms.CharField(required=False)
    s_country = forms.CharField(required=False)
    s_code = forms.CharField(required=False)

