import unittest
import mock
from django.http import HttpResponseRedirect
from django_freshbooks.forms import *
from django_freshbooks.views import *

MINIMAL_CLIENT_DATA = {
                        "client_id":"",
                        "first_name":"Johan",
                        "last_name":"Doe",
                        "organization":"Acme Co",
                        "email":"jon@acme.com"
                       }

class FormsTestCase(unittest.TestCase):
    def test_posted_client(self):
        form = ClientForm(MINIMAL_CLIENT_DATA)
        assert form.is_valid(),"only required fields are checked"
            
            
class ViewsTestCase(unittest.TestCase):
    request = mock.Mock()

    def setUp(self):
        self.request = mock.Mock()
        
    def test_get_generic_create_view(self):
        self.request.method = "GET"
        response = client_create(self.request,ClientForm,client_added)
        assert response.content.find("<form") >=0, "Should have found a valid form"
        
    def test_post_generic_create_view(self):
        self.request.method = "POST"
        self.request.POST = MINIMAL_CLIENT_DATA
        response = generic_freshbooks_create(self.request,ClientForm,client_added)
        
        assert isinstance(response,HttpResponseRedirect),"Should be redirecting to *added"