import requests
from bs4 import BeautifulSoup 

def meta_description_tag_check(url):
    '''
    Checking for meta tag description.
        - A well-written meta description attracts more clicks in search results than an irrelevant or missing description.
    Priority 3 - AAA (https://www.bing.com/webmasters/help/webmasters-guidelines-30fba23a)
    @input:
        url: URL which is currently being crawled.
    @output:
        boolean: True (if description is present) else False
    '''
    response = requests.get(url)
    soup = BeautifulSoup(response.text)

    all_metas = soup.find_all('meta')

    for meta in all_metas:
        if 'name' in meta.attrs and meta.attrs['name'] == 'description':
            return True
    
    return False

def title_tag_check(page_text):
    '''
    Checking for title on a web page.
    Priority 1 - A (https://www.w3.org/TR/WCAG21/#page-titled)
    @input:
        page_text: Source code of the current web page.
    @output:
        boolean: True (if title is present) else False
    '''
    soup = BeautifulSoup(page_text)

    title = soup.find_all('title')

    if title:
        return True
    return False
