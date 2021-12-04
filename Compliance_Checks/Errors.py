import requests
from bs4 import BeautifulSoup 


def blank_body_check(page_text, url):
    '''
    Checking if body is empty in a webpage.
    @input:
        page_text: Source code of the current web page.
    @output:
        boolean: True (if body is empty) else False
    '''
    error_text = "Body is empty."
    guideline = "Empty Body."
    guideline_link = "https://www.w3.org/TR/2008/REC-WCAG20-20081211/#ensure-compat-parses"

    soup = BeautifulSoup(page_text, 'html.parser')

    body = soup.body

    if body:
        return None
    else:
        return [error_text, url, guideline, ["-"]]