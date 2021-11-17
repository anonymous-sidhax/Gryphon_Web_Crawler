from bs4 import BeautifulSoup 
import collections

def duplicate_id_check(page_text):
    '''
    Checking if same ID is used on more than one element.
    Priority 1 - A (https://www.w3.org/TR/2008/REC-WCAG20-20081211/#ensure-compat-parses)
    @input:
        page_text: Source code of the current web page.
    @output:
        list: List of duplicate ids.
    '''
    soup = BeautifulSoup(page_text)

    ids = [a.attrs['id'] for a in soup.find_all(attrs={'id': True})]
    ids = collections.Counter(ids)

    duplicate_ids = [key for key, value in ids.items() if value > 1]

    return duplicate_ids