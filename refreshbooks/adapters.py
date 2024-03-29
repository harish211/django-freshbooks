from lxml import etree, objectify
import logging

from django_freshbooks.refreshbooks import elements, client

def encode_as_simple_from_element(name, value):
    """Creates an etree element following the simple field convention. To 
    ease reuse of returned data in future calls, we smash anything that looks 
    like an ObjectifiedDataElement to unicode:
    
        >>> value = objectify.DataElement(5)
        >>> element = encode_as_simple('foo', value)
        >>> element.tag == 'foo'
        True
        >>> element.text == '5'
        True
    """
    return encode_as_simple(name, value.text)

def encode_as_simple(name, value):
    """Creates an etree element following the simple field convention. Values
    are assumed to be strs or unicodes already:
    
        >>> element = encode_as_simple('foo', '5')
        >>> element.tag == 'foo'
        True
        >>> element.text == '5'
        True
    """
    val_type = type(value).__name__
    if val_type != 'dict' and val_type !='list' and val_type != 'unicode':
        value = str(value)
    if isinstance(value, objectify.ObjectifiedDataElement):
        return encode_as_simple(name, unicode(value))
    return elements.field(name, value)

def encode_as_dict(_name, **kwargs):
    # To make collisions between the first positional parameter and the 
    # keyword parameters unlikely, that's why.
    return elements.type(_name, [
        encode_parameter(name, value) for (name, value) in kwargs.iteritems()
    ])

def encode_as_list_of_dicts(name, *args):
    return elements.type(name, [
        encode_parameter(name, value) for (name, value) in args
    ])

def encode_parameter(name, value):
    # This type-checking order is delicate. Don't touch it until you 
    # understand the interactions between:
    #
    # - foo(*a_dict) causes foo to receive the keys of a_dict as positional
    #   parameters.
    # - foo(*a_string) causes foo to receive each character of a_string as a
    #   positional parameter.
    # - encode_as_simple will barf with a TypeError if the value is not
    #   representable as XML.
    # - encode_as_simple_from_element will barf with an AttributeError if the 
    #   value is not an Element-shaped thing.
    #
    # We do this so that we don't need to maintain a list of mappings for
    # every Freshbooks API document type. You're welcome.
    try:
        return encode_as_simple_from_element(name, value)
    except AttributeError:
        try:
            return encode_as_dict(name, **value)
        except TypeError, msg:
            try:
                return encode_as_simple(name, value)
            except TypeError, msg:
                return encode_as_list_of_dicts(name, *value)

def xml_request(method, **params):
    request_document = elements.request(
        method,
        [
            encode_parameter(name, value)
            for (name, value) in params.iteritems()
        ]
    )
    
    return etree.tostring(request_document)

def fail_to_exception_response(response):
    if response.attrib['status'] == 'fail':
        raise client.FailedRequest(response.error)
    
    return response