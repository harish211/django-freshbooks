from django.conf import settings

# Create your freshbooks token from My Account -> API
FRESHBOOKS_TOKEN = getattr(settings,"FRESHBOOKS_TOKEN","")

# The URL you use to access your freshbooks site
FRESHBOOKS_URL = getattr(settings,"FRESHBOOKS_URL","")