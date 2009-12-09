INSTALLATION:

cd /Library/Python/2.6/site-packages/ # or /var/lib/python2.6/site-packages
svn co http://django-freshbooks.googlecode.com/svn/trunk/ django_freshbooks

# Add 2 settings to your settings.py
cd /var/my/django/project/
echo 'FRESHBOOKS_TOKEN = "MYSECRETKEYFROMFRESHBOOKS"
FRESHBOOKS_URL = "myurl.freshbooks.com"' >> settings.py

# Add to urls.py
(r'^freshbooks/', include('django_freshbooks.urls')),
