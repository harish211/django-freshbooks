from django_freshbooks.forms import *
from django_freshbooks.settings import *
from django_freshbooks.refreshbooks import api
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

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


def category_create(request):
    if request.method == 'POST': # If the form has been submitted...
        form = CategoryForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            fb = auth_freshbooks()
            fb.category.create(category=form.cleaned_data)
            return HttpResponseRedirect(reverse(category_added)) # Redirect after POST
    
    form = CategoryForm() # An unbound form

    return render_to_response('form.html', { 'form': form, })

def category_added(request):
    return render_to_response('added.html', {'type':'category'})

def client_create(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ClientForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            fb = auth_freshbooks()
            fb.client.create(form.cleaned_data)
            return HttpResponseRedirect(reverse(client_added)) # Redirect after POST
    
    form = ClientForm() # An unbound form

    return render_to_response('form.html', { 'form': form, })

def client_added(request):
    return render_to_response('added.html', {'type':'client'})

