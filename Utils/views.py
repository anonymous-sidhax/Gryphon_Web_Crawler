import time
from urllib.parse import urlparse

def get_time():
    '''
    Returns the time in format: HH:MM:SS
    '''
    return time.strftime('%H:%M:%S')

def get_full_time():
    '''
    Returns the time in format: HH:MM:SS Weekday Month Year
    '''    
    return time.strftime('%H:%M:%S, %A %b %Y')

def is_valid(url):
    '''
    Checks whether the URL is valid or not.
    '''
    # We can also use USE django.core.validators.URLValidator() TO CHECK IF A STRING IS A URL.
    '''
    validate = URLValidator()

    try:
        validate("http://www.avalidurl.com/")
        print("String is a valid URL")
    except ValidationError as exception:
        print("String is not valid URL")

    OR

    # pip install validators
    >>> import validators
    >>> validators.url("http://google.com")
    True
    >>> validators.url("http://google")
    ValidationFailure(func=url, args={'value': 'http://google', 'require_tld': True})
    >>> if not validators.url("http://google"):
    ...     print "not valid"
    ... 
    not valid
    >>>
    '''
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)
