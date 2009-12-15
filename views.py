from django_freshbooks import forms 
from django_freshbooks.settings import *
from django_freshbooks.refreshbooks import api
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.http import Http404

import logging

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


def form_create(request,form_type):
    '''
    form_type must be a simple type with no line items
    Category, Client, Expense, Item, Payment, Project, Staff, Task, Time Entry
    '''
    logging.debug("form_type is"+form_type)
    if form_type not in ('invoice','category','client','expense','item','payment','project','staff','task','timeentry'):
        raise Http404
    
    form_class = form_type.capitalize() + 'Form'
    if request.method == 'POST': # If the form has been submitted...
        form = getattr(forms,form_class)(request.POST) # A form bound to the POST data
        formsets = __instantiate_formsets(form.formset_classes,request.POST)
        #TODO loop over and validate formsets
        #TODO remove remove 'and False' to enable FB API again
        if form.is_valid() and False: # All validation rules pass
            fb = auth_freshbooks()
            fb_kwargs = {str(form_type): form.cleaned_data}
            func_type = getattr(fb, form_type)
            # We could check here if id is set to determine create or updated
            func_type.create(**fb_kwargs)
            return HttpResponseRedirect(reverse('form_added',kwargs={'form_type':form_type})) # Redirect after POST
    else:
        form = getattr(forms,form_class)()# An unbound form
        formsets = __instantiate_formsets(form.formset_classes)
    # We should be able to abstract this a bit for when we bind data
    
    
    return render_to_response('form.html', { 'form': form, 'formsets':formsets})

def __instantiate_formsets(formset_classes,data={}):
    try:
        formsets = list()
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
            fb = auth_freshbooks()
            fb_kwargs = {'category': form.cleaned_data}
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
