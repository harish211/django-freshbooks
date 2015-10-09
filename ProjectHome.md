This is combination of Django Forms and the Freshbooks API refreshbooks from Owen Jacobson here http://pypi.python.org/pypi/refreshbooks/.

INSTALLATION:

# Download dependacies
<pre>
easy_install oauth<br>
easy_install functional<br>
easy_install lxml<br>
easy_install httplib2<br>
</pre>


# Checkout the code into a dir named django\_freshbooks

<pre>
cd /Library/Python/2.6/site-packages/ # or /var/lib/python2.6/site-packages<br>
svn co http://django-freshbooks.googlecode.com/svn/trunk/ django_freshbooks<br>
</pre>


# Add 2 settings to your settings.py
<pre>
cd /var/my/django/project/<br>
echo 'FRESHBOOKS_TOKEN = "MYSECRETKEYFROMFRESHBOOKS"<br>
FRESHBOOKS_URL = "myurl.freshbooks.com"' >> settings.py<br>
</pre>

# Add to urls.py
<pre>
(r'^freshbooks/', include('django_freshbooks.urls')),<br>
</pre>