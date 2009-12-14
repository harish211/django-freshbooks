from django_freshbooks import forms 
from django_freshbooks.settings import *
from django_freshbooks.refreshbooks import api
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.forms.formsets import formset_factory
from django.http import Http404

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
    if form_type not in ('category','client','expense','item','payment','project','staff','task','timeentry'):
        raise Http404
    
    form_class = form_type.capitalize() + 'Form'
    if request.method == 'POST': # If the form has been submitted...
        form = getattr(forms,form_class)(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            fb = auth_freshbooks()
            fb_kwargs = {'category': form.cleaned_data}
            func_type = getattr(fb, form_type)
            func_type.create(**fb_kwargs)
            return HttpResponseRedirect(reverse('form_added',kwargs={'form_type':form_type})) # Redirect after POST
    
    form = getattr(forms,form_class)()# An unbound form

    return render_to_response('form.html', { 'form': form, })

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

def generic_freshbooks_create(request,form_class,next_view):
    if request.method == 'POST': # If the form has been submitted...
        form = form_class(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            print "IS VALID"
            fb = auth_freshbooks()
            #fb.category.create(category=form.cleaned_data)
            return HttpResponseRedirect(reverse(form_added)) # Redirect after POST
    
    form = form_class() # An unbound form
    return render_to_response('form.html', { 'form': form, })
