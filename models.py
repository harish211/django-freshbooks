from django.db import models
from freshbooks.django_freshbooks.api import * 
from freshbooks.django_freshbooks.settings import *
from datetime import date

STATUS_CHOICE = (
                 ('sent','sent'),
                 ('viewed','viewed'),
                 ('paid','paid'),
                 ('draft','draft'),
                 )

class Line(FreshbookObject):
    name = models.CharField(max_length=255,blank=True)
    description = models.CharField(max_length=255,blank=True)
    unit_cost = models.DecimalField(max_digits=2,decimal_places=2,blank=True)
    quantity = models.IntegerField(blank=True)
    tax1_name = models.CharField(max_length=255,blank=True)
    tax2_name = models.CharField(max_length=255,blank=True)
    tax1_percent = models.DecimalField(max_digits=2,decimal_places=2,blank=True)
    tax2_percent = models.DecimalField(max_digits=2,decimal_places=2,blank=True)
   
    def clean(self):
        cleaned_data = self.cleaned_data
        api.setup(FRESHBOOKS_URL,FRESHBOOKS_TOKEN);
        line = api.Line()
        
        for key,value in self.cleaned_data.items():
            setattr(line, key, value)
        try:
            response = api.call_api("line.create", {None:client})
        except Exception as msg:
            raise models.ValidationError(msg)
        
        
class Invoice(FreshbookObject):
    client_id = models.IntegerField()
    number = models.CharField(max_length=255,blank=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICE,default='draft')
    date = models.DateField(default=date.today(),blank=True)
    po_number = models.CharField(max_length=255,blank=True)
    discount = models.DecimalField(blank=True,max_digits=2,decimal_places=2)
    notes = models.CharField(max_length=255,blank=True,)
    terms = models.CharField(max_length=255,blank=True)
    return_uri = models.CharField(max_length=255,blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    p_street1 = models.CharField(max_length=255,blank=True)
    p_street2 = models.CharField(max_length=255,blank=True)
    p_city = models.CharField(max_length=255,blank=True)
    p_state = models.CharField(max_length=255,blank=True)
    p_country = models.CharField(max_length=255,blank=True)
    p_code = models.CharField(max_length=255,blank=True)

    def clean(self):
        cleaned_data = self.cleaned_data
        api.setup(FRESHBOOKS_URL,FRESHBOOKS_TOKEN);
        invoice = api.Invoice()
        
        for key,value in self.cleaned_data.items():
            setattr(client, key, value)
        try:
            response = api.call_api("invoice.create", {None:client})
        except Exception as msg:
            raise models.ValidationError(msg)
        
    
        
class Client(FreshbookObject):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    organization = models.CharField(max_length=100)
    email = models.EmailField()
    username = models.CharField(max_length=50, blank=True)
    password = models.CharField(max_length=10, blank=True)
    work_phone = models.CharField(max_length=20,blank=True)
    home_phone = models.CharField(max_length=20,blank=True)
    mobile = models.CharField(max_length=20,blank=True)
    fax = models.CharField(max_length=20,blank=True)
    notes = models.CharField(max_length=255,blank=True,)
    p_street1 = models.CharField(max_length=255,blank=True)
    p_street2 = models.CharField(max_length=255,blank=True)
    p_city = models.CharField(max_length=255,blank=True)
    p_state = models.CharField(max_length=255,blank=True)
    p_country = models.CharField(max_length=255,blank=True)
    p_code = models.CharField(max_length=255,blank=True)
    s_street1 = models.CharField(max_length=255,blank=True)
    s_street2 = models.CharField(max_length=255,blank=True)
    s_city = models.CharField(max_length=255,blank=True)
    s_state = models.CharField(max_length=255,blank=True)
    s_country = models.CharField(max_length=255,blank=True)
    s_code = models.CharField(max_length=255,blank=True)

    def save(self):
        setup(FRESHBOOKS_URL,FRESHBOOKS_TOKEN);
        response = call_api("client.create", {None:self})


class Item(FreshbookObject):
    '''
    The Item object
    '''

    object_name = 'item'
    TYPE_MAPPINGS = {'item_id' : 'int', 'unit_cost' : 'float',
        'quantity' : 'int', 'inventory' : 'int'}

    def __init__(self):
        '''
        The constructor is where we initially create the
        attributes for this class
        '''
        for att in ('item_id', 'name', 'description', 'unit_cost',
        'quantity', 'inventory'):
            setattr(self, att, None)

