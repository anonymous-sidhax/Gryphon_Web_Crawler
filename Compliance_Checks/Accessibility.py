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

def alt_in_img_elements_check(page_text):
    '''
    Checking if alt attribute is present on all img tags.
    (https://www.w3.org/TR/2008/WD-WCAG20-TECHS-20081103/H37)
    @input:
        page_text: Source code of the current web page.
    @output:
        list: List of image src without alt.
    '''
    soup = BeautifulSoup(page_text.text, "html.parser")
        
    img_tags = soup.find_all('img')
    empty_alt = []
    for img_tag in img_tags:
        if not img_tag.find('alt') or img_tag.find('alt') == "":
            empty_alt.append(img_tag['src'])   
    
    return empty_alt
