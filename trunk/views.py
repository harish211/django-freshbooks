from django_freshbooks import forms 
from django_freshbooks.settings import *
from django_freshbooks.refreshbooks import api
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.http import Http404
from lxml import objectify

import logging
logging.basicConfig(level=logging.DEBUG)

def auth_freshbooks(type='token'):
    if type == 'oauth':
        c = api.OAuthClient(
                            FRESHBOOKS_URL,
                            '',
                            'My Consumer Secret',
                            'An existing token',
                            'An existing token secret'
                            )
    else:
        c = api.TokenClient(
                            FRESHBOOKS_URL,
                            FRESHBOOKS_TOKEN
                            )
    return c
def form(request,form_type,object_id=None):
    if form_type in ('category','client','expense','item','payment','project','staff','task','time_entry'):
        pass
        #LineFormSet = list
    elif form_type in ('estimate','invoice','recurring'):
        LineFormSet = formset_factory(forms.LineForm, extra=2)
    else:
        raise Http404
    form_class = form_type.capitalize() + 'Form'
    if request.method == 'POST': # If the form has been submitted...
        form = getattr(forms,form_class)(request.POST) # A form bound to the POST data
        formsets = __instantiate_formsets(form.formset_classes, request.POST)
        # filter will return formsets that fail validation, only continue if the returned list is empty
        if form.is_valid() and not filter(lambda fset: not fset.is_valid(),formsets):
            import logging
            logging.debug("VALID")
            fb = auth_freshbooks()
            fb_kwargs = {str(form_type): form.cleaned_data}
            func_type = getattr(fb, form_type)
            # We could check here if id is set to determine create or updated
            if object_id:
                func_type.update(**fb_kwargs)
            else:
                func_type.create(**fb_kwargs)
            return HttpResponseRedirect(reverse('form_added',kwargs={'form_type':form_type})) # Redirect after POST
    else:
        if object_id:
            fb = auth_freshbooks()
            E = objectify.E
            fb_type = E.root(E.id(object_id),)
            func_type = getattr(fb, form_type)
            fb_kwargs = {str(form_type)+'_id': fb_type.id}
            fb_type_response = func_type.get(**fb_kwargs)
            form = getattr(forms,form_class)(getattr(fb_type_response,form_type).__dict__)# a bound form
            #formsets = LineFormSet()
        else:
            form = getattr(forms,form_class)() # an unbound form
            #formsets = LineFormSet()
        formsets = __instantiate_formsets(form.formset_classes, request.POST)
    
    return render_to_response('form.html', { 'form': form, 'formsets':formsets})

def list(request,type):
    fb_map = {
              'category':
              {'plural':'categories',
               'description':'name',
               },
              'item':
              {'plural':'items',
               'description':'name',
               },
              'client':
              {'plural':'clients',
               'description':'organization',
               },
              'estimate':
              {'plural':'estimates',
               'description':'organization',
               },
              'expense':
              {'plural':'expenses',
               'description':'amount',
               },
              'invoice':
              {'plural':'invoices',
               'description':'organization',
               },
              'payment':
              {'plural':'payments',
               'description':'amount',
               },
              'project':
              {'plural':'projects',
               'description':'name',
               },
              'recurring':
              {'plural':'recurrings',
               'description':'organization',
               },
              'staff':
              {'plural':'staff_members',
               'description':'first_name',
               },
              'task':
              {'plural':'tasks',
               'description':'name',
               },
              'time_entry':
              {'plural':'time_entries',
               'description':'hours',
               },
              }
    fb = auth_freshbooks()
    result = []
    type_list = getattr(fb,type).list()
    if type == 'staff':
        xml_type = 'member'
    else:
        xml_type = type
    for element in getattr(getattr(type_list,fb_map[type]['plural']),xml_type):
        result.append({'id':getattr(element,type+'_id'),'description':getattr(element,fb_map[type]['description'])})
    return render_to_response('list.html', {'list':result, 'type':type})


def __instantiate_formsets(formset_classes,data={}):
    try:
        formsets = []
        for attr_name,formset_class in formset_classes.items():
            if len(data) > 0:
                formset = formset_class(data)
            else:
                formset = formset_class()
            formset.name = attr_name
            formsets.append(formset)
    except AttributeError:
        pass
    return formsets

def inline_form_create(request,form_type):
    '''
    form_type must be a simple type with no relationships
    Category, Client, Item, Staff, Task
    '''
    if form_type not in ('estimate','invoice','recurring'):
        raise Http404
    form_class = form_type.capitalize() + 'Form'
    LineFormSet = formset_factory(forms.LineForm, extra=2)
    if request.method == 'POST': # If the form has been submitted...
        form = getattr(forms,form_class)(request.POST) # A form bound to the POST data
        formset = LineFormSet(request.POST)
        if form.is_valid(): # All validation rules pass
            form.cleaned_data['lines']=list()
            for f in formset.forms:
                if f.is_valid():
                    form.cleaned_data['lines'].append(('line',f.cleaned_data))
            fb = auth_freshbooks()
            fb_kwargs = {str(form_type): form.cleaned_data}
            func_type = getattr(fb, form_type)
            func_type.create(**fb_kwargs)
            return HttpResponseRedirect(reverse('form_added',kwargs={'form_type':form_type})) # Redirect after POST
    
    form = getattr(forms,form_class)()# An unbound form
    formset = LineFormSet()

    return render_to_response('form.html', { 'form': form, 'formset':formset})

def form_added(request,form_type):
    return render_to_response('added.html', {'type':form_type})

def client_added(request):
    return render_to_response('added.html', {'type':'client'})

