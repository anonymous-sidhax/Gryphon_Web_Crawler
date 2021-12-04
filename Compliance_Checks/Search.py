import requests
from bs4 import BeautifulSoup 

def meta_description_tag_check(page_text, url):
    '''
    Checking for meta tag description.
        - A well-written meta description attracts more clicks in search results than an irrelevant or missing description.
    Priority 3 - AAA (https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a)
    @input:
        url: URL which is currently being crawled.
    @output:
        boolean: True (if description is present) else False
    '''
    error_text = "Meta Description is not present."
    guideline = "BING Webmaster Guidelines"
    guideline_link = "https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a"

    soup = BeautifulSoup(page_text, 'html.parser')

    all_metas = soup.find_all('meta')

    for meta in all_metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'description':
            return None
    
    return [error_text, url, guideline, ["-"]]

def title_tag_check(page_text, url):
    '''
    Checking for title on a web page.
    Priority 1 - A (https://www.w3.org/TR/WCAG21/#page-titled)
    @input:
        page_text: Source code of the current web page.
    @output:
        boolean: True (if title is present) else False
    '''
    error_text = "Page title is not present."
    guideline = "WCAG 2.0 A 2.4.2"
    guideline_link = "https://www.w3.org/TR/WCAG21/#page-titled"

    soup = BeautifulSoup(page_text, 'html.parser')

    title = soup.find_all('title')

    if title:
        return None
    else:
        return [error_text, url, guideline, ["-"]]

def doctype_check(page_text):
    '''
    Checking if DOCTYPE is defined on a page.
    https://html.spec.whatwg.org/multipage/syntax.html#the-doctype
    @input:
        page_text: Source code of the current web page.
    @output:
        string: returns the doctype if available else None
    '''
    soup = BeautifulSoup(page_text.text, 'html.parser')

    items = [item for item in soup.contents if isinstance(item, BeautifulSoup.Doctype)]
    return items[0] if items else None