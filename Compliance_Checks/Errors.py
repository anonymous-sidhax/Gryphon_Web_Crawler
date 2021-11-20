import requests
from bs4 import BeautifulSoup 


def blank_body_check(page_text):
    '''
    Checking if body is empty in a webpage.
    @input:
        page_text: Source code of the current web page.
    @output:
        boolean: True (if body is empty) else False
    '''
    soup = BeautifulSoup(page_text, 'html.parser')

    body = soup.body

    if body:
        return False
    return True