import unittest
from mock import *
from django.http import HttpResponseRedirect
from django_freshbooks.forms import *
from django_freshbooks.views import *
from django_freshbooks import views
from django_freshbooks.refreshbooks import api

#For info on the mock library: http://www.voidspace.org.uk/python/mock/

mock_api = Mock()
mock_api.client = Mock(spec=["create","invalid"])
def mock_auth(x=""):
    print "CALLED mock AUTH"
    return mock_api

views.auth_freshbooks = mock_auth

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
    request = Mock()
        
#    def test_get_form_create(self):
#        self.request.method = "GET"
#        response = form_create(self.request,"client")
#        assert response.content.find("<form") >=0, "Should have found a valid form"
#        
#    def test_post_form_create(self):
#        self.request.method = "POST"
#        self.request.POST = MINIMAL_CLIENT_DATA
#        response = form_create(self.request,"client")
#        assert isinstance(response,HttpResponseRedirect),"Should be redirecting to *added"
#        assert mock_api.client.create.called # asserts this method was called
            
        