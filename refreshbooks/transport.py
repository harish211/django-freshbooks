import base64
import httplib
import httplib2
import oauth.oauth as oauth

class OAuthAuthorization(object):
    """Generates headers for an OAuth Core 1.0 Revision A (say that three 
    times fast) request, given an oauth.Consumer and an oauth.Token.
    
        >>> import oauth.oauth as oauth
        >>> consumer = oauth.OAuthConsumer("EXAMPLE", "CONSUMER")
        >>> token = oauth.OAuthToken("EXAMPLE", "TOKEN")
        >>> auth = OAuthAuthorization(consumer, token)
        >>> auth() # doctest:+ELLIPSIS
        {'Authorization': 'OAuth realm="", oauth_nonce="...", oauth_timestamp="...", oauth_consumer_key="EXAMPLE", oauth_signature_method="PLAINTEXT", oauth_version="1.0", oauth_token="EXAMPLE", oauth_signature="CONSUMER%26TOKEN"'}
    
    """
    def __init__(self, consumer, token, sig_method=oauth.OAuthSignatureMethod_PLAINTEXT()):
        self.consumer = consumer
        self.token = token
        self.sig_method = sig_method

    def __call__(self):
        oauth_request = oauth.OAuthRequest.from_consumer_and_token(
            self.consumer,
            token=self.token
        )
        oauth_request.sign_request(self.sig_method, self.consumer, self.token)
        return oauth_request.to_header()

class TokenAuthorization(object):
    """Generates HTTP BASIC authentication headers obeying FreshBooks'
    token-based auth scheme (token as username, password irrelevant).
    
        >>> auth = TokenAuthorization("monkey")
        >>> auth()
        {'Authorization': 'Basic bW9ua2V5Og=='}
    
    Prefer OAuthAuthorization, above, for new development.
    """
    def __init__(self, token):
        # See RFC 2617.
        base64_user_pass = base64.b64encode("%s:" % (token, ))
        
        self.headers = {
            'Authorization': 'Basic %s' % (base64_user_pass, )
        }
    
    def __call__(self):
        return self.headers

class TransportException(Exception):
    def __init__(self, reason):
        self.reason = reason
    
    def __str__(self):
        return repr(self.reason)

class HttpTransport(object):
    def __init__(self, url, headers_factory):
        self.url = url
        self.headers_factory = headers_factory
    
    def __call__(self, entity):
        client = httplib2.Http()
        import logging
        logging.debug("Trying to connect to "+self.url)
        resp, content = client.request(
            self.url,
            'POST',
            headers=self.headers_factory(),
            body=entity
        )
        if resp.status >= 400:
            raise TransportException(resp.status)
        
        return content
