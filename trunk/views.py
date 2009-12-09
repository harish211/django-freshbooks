from django_freshbooks.forms import *
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def client_create(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ClientForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            obj = form.save()
            return HttpResponseRedirect(reverse(client_added)) # Redirect after POST
    
    form = ClientForm() # An unbound form

    return render_to_response('form.html', { 'form': form, })

def client_added(request):
    return render_to_response('added.html', )
