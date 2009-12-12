from django import forms
from datetime import date
from django.utils.functional import lazy

STATUS_CHOICES = (
                 ('sent','sent'),
                 ('viewed','viewed'),
                 ('paid','paid'),
                 ('draft','draft'),
                 )
INVOICE_CHOICES = (
                 ('sent','sent'),
                 ('viewed','viewed'),
                 ('paid','paid'),
                 ('draft','draft'),
                 )
EXP_CHOICES = (
                 (0,'not assigned'),
                 (1,'unbilled'),
                 (2,'invoiced'),
                 )
EST_STATUS_CHOICES = (
                 ('sent','sent'),
                 ('viewed','viewed'),
                 ('disputed','disputed'),
                 ('replied','replied'),
                 ('accepted','accepted'),
                 ('draft','draft'),
                 )
FREQ_CHOICES = (
                 ('weekly','weekly'),
                 ('2 weeks','2 weeks'),
                 ('4 weeks','4 weeks'),
                 ('monthly','monthly'),
                 ('3 months','3 months'),
                 ('6 months','6 months'),
                 ('yearly','yearly'),
                 ('2 years','2 years'),
                 )
def get_client_list():
    return ((1, 'one'),)
def get_project_list():
    return ((1, 'one'),)
def get_task_list():
    return ((1, 'one'),)
def get_staff_list():
    return ((1, 'one'),)
def get_invoice_list():
    return ((1, 'one'),)
def get_category_list():
    return ((1, 'one'),)
class CategoryForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/categories/ '''
    category_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    name = forms.CharField()
        
class ClientForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/clients/ '''
    client_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    organization = forms.CharField()
    email = forms.EmailField()
    username = forms.CharField(required=False)
    password = forms.CharField(widget=forms.PasswordInput,required=False)
    work_phone = forms.CharField(required=False, help_text="(XXX) XXX-XXXX")
    home_phone = forms.CharField(required=False, help_text="(XXX) XXX-XXXX")
    mobile = forms.CharField(required=False, help_text="(XXX) XXX-XXXX")
    fax = forms.CharField(required=False, help_text="(XXX) XXX-XXXX")
    notes = forms.CharField(widget=forms.Textarea,required=False)
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
    
class EstimateForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/estimates/ '''
    estimate_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    client_id = forms.TypedChoiceField(choices=lazy(get_client_list,tuple)(),coerce=int)
    status = forms.ChoiceField(choices=EST_STATUS_CHOICES,initial='draft')
    date = forms.DateField(initial=date.today(),required=False)
    po_number = forms.CharField(required=False)
    discount = forms.DecimalField(required=False,max_value=100,decimal_places=2)
    notes = forms.CharField(widget=forms.Textarea,required=False,)
    terms = forms.CharField(required=False)
    return_uri = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    organization = forms.CharField(required=False)
    p_street1 = forms.CharField(required=False)
    p_street2 = forms.CharField(required=False)
    p_city = forms.CharField(required=False)
    p_state = forms.CharField(required=False)
    p_country = forms.CharField(required=False)
    p_code = forms.CharField(required=False)
    # line will be a seperate formset

class ExpenseForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/expenses/ '''
    expense_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    staff_id = forms.TypedChoiceField(choices=lazy(get_staff_list,tuple)(),coerce=int)
    category_id = forms.TypedChoiceField(choices=lazy(get_category_list,tuple)(),coerce=int)
    project_id = forms.TypedChoiceField(choices=lazy(get_project_list,tuple)(),required=False, coerce=int)
    client_id = forms.TypedChoiceField(choices=lazy(get_client_list,tuple)(),required=False,coerce=int)
    amount = forms.DecimalField(max_digits=10,decimal_places=2,required=False)
    vendor = forms.CharField(required=False)
    date = forms.DateField(required=False)
    notes = forms.CharField(widget=forms.Textarea,required=False)
    status = forms.TypedChoiceField(choices=EXP_CHOICES,coerce=int)
    tax1_name = forms.CharField(required=False)
    tax1_percent = forms.DecimalField(max_digits=10,decimal_places=2,required=False)
    tax1_amount = forms.DecimalField(max_digits=10,decimal_places=2,required=False)
    tax2_name = forms.CharField(required=False)
    tax2_percent = forms.DecimalField(max_digits=10,decimal_places=2,required=False)
    tax2_amount = forms.DecimalField(max_digits=10,decimal_places=2,required=False)

class InvoiceForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/invoices/ '''
    invoice_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    client_id = forms.TypedChoiceField(choices=lazy(get_client_list,tuple)(),coerce=int)
    number = forms.CharField(required=False)
    status = forms.ChoiceField(choices=STATUS_CHOICES,initial='draft')
    date = forms.DateField(initial=date.today(),required=False)
    po_number = forms.CharField(required=False)
    discount = forms.DecimalField(required=False,max_value=100,decimal_places=2)
    notes = forms.CharField(widget=forms.Textarea,required=False)
    terms = forms.CharField(required=False)
    return_uri = forms.URLField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    organization = forms.CharField(required=False)
    p_street1 = forms.CharField(required=False)
    p_street2 = forms.CharField(required=False)
    p_city = forms.CharField(required=False)
    p_state = forms.CharField(required=False)
    p_country = forms.CharField(required=False)
    p_code = forms.CharField(required=False)
    # line will be a seperate formset

class ItemForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/items/ '''
    item_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    name = forms.CharField()
    description = forms.CharField(required=False)
    unit_cost = forms.DecimalField(decimal_places=2,required=False)
    quantity = forms.IntegerField(required=False)
    inventory = forms.IntegerField(required=False)
            
class PaymentForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/items/ '''
    payment_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    client_id = forms.TypedChoiceField(choices=lazy(get_client_list,tuple)(),coerce=int)
    invoice_id = forms.TypedChoiceField(choices=get_invoice_list(),required=False, coerce=int)
    date = forms.DateField(required=False)
    amount = forms.DecimalField(decimal_places=2,required=False)
    type = forms.CharField(required=False)
    notes = forms.CharField(widget=forms.Textarea,required=False)
         
class ProjectForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/projects/ '''
    project_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    name = forms.CharField()
    bill_method = forms.CharField()
    client_id = forms.TypedChoiceField(choices=lazy(get_client_list,tuple)(), required=False, coerce=int)
    rate = forms.DecimalField(max_digits=10,decimal_places=2, required=False)
    description = forms.CharField(required=False)

class RecurringForm(forms.Form):
    ''' http://developers.freshbooks.com/api/view/recurring/ '''
    recurring_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    client_id = forms.TypedChoiceField(choices=lazy(get_client_list,tuple)(), coerce=int)
    date = forms.DateField(initial=date.today(),required=False)
    po_number = forms.CharField(required=False)
    discount = forms.DecimalField(required=False,max_value=100,decimal_places=2)
    occurrences = forms.IntegerField(help_text='0 = infinite',initial=0)
    frequency = forms.ChoiceField(choices=FREQ_CHOICES)
    send_email = forms.BooleanField(required=False)
    send_snail_mail = forms.BooleanField(required=False)
    notes = forms.CharField(widget=forms.Textarea,required=False)
    terms = forms.CharField(required=False)
    return_uri = forms.CharField(required=False)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    organization = forms.CharField(required=False)
    p_street1 = forms.CharField(required=False)
    p_street2 = forms.CharField(required=False)
    p_city = forms.CharField(required=False)
    p_state = forms.CharField(required=False)
    p_country = forms.CharField(required=False)
    p_code = forms.CharField(required=False)
    ''' Line will be a seperate formset '''

class StaffForm(forms.Form):
    '''
    Staff only has a get and list methods
    Can not create staff via api
    http://developers.freshbooks.com/api/view/staff/
    '''
    staff_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    username = forms.CharField(required=False)
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    business_phone = forms.CharField(required=False, help_text="(XXX) XXX-XXXX")
    mobile_phone = forms.CharField(required=False, help_text="(XXX) XXX-XXXX")
    rate = forms.DecimalField(max_digits=10,decimal_places=2)
    notes = forms.CharField(widget=forms.Textarea,required=False,)
    street1 = forms.CharField(required=False)
    street2 = forms.CharField(required=False)
    city = forms.CharField(required=False)
    state = forms.CharField(required=False)
    country = forms.CharField(required=False)
    code = forms.CharField(required=False)
           
class TaskForm(forms.Form):
    task_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    name = forms.CharField()
    billable = forms.BooleanField(required=False)
    rate = forms.DecimalField(decimal_places=2, required=False)
    description = forms.CharField(required=False)
    
class TimeEntryForm(forms.Form):
    task_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    project_id = forms.TypedChoiceField(choices=lazy(get_project_list,tuple)(), coerce=int)
    task_id = forms.TypedChoiceField(choices=lazy(get_task_list,tuple)(), coerce=int)
    hours = forms.DecimalField(decimal_places=2,required=False)
    date = forms.DateField(required=False)
    notes = forms.CharField(widget=forms.Textarea,required=False)

class LineForm(forms.Form):
    name = forms.CharField(required=False)
    description = forms.CharField(required=False)
    unit_cost = forms.DecimalField(decimal_places=2)
    quantity = forms.IntegerField(required=False)
    tax1_name = forms.CharField(required=False)
    tax2_name = forms.CharField(required=False)
    tax1_percent = forms.DecimalField(decimal_places=2,required=False)
    tax2_percent = forms.DecimalField(decimal_places=2,required=False)
