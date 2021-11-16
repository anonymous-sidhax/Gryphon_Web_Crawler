import requests
from bs4 import BeautifulSoup 

def meta_description_tag_check(url):
    '''
    Checking for meta tag description.
        - A well-written meta description attracts more clicks in search results than an irrelevant or missing description.
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