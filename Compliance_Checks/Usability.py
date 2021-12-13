from os import error
from bs4 import BeautifulSoup 

def underlined_text_is_not_a_link_check(page_text, url):
    '''
    Check if underlined text is not a link.
        -Avoid underlined text - people will click on it and think it's a broken link.
    Priority 2 - AA (https://www.powermapper.com/products/sortsite/rules/usegov10.4/)
    @input:
        page_text: Source code of the current web page..
    @output:
        boolean: True (if underlined text is not a link) else False
    '''
    error_text = "Underlined text is not a link"
    guideline = "WCAG 2.0 F73 1.4.1"
    guideline_link = "https://www.w3.org/TR/WCAG20-TECHS/F73.html"

    soup = BeautifulSoup(page_text, 'html.parser')

    u_tags = soup.find_all('u')
    underlined_ids = []

    for underlined in u_tags:
        if '<a' not in underlined.get_text():
            underlined_ids.extend([underlined.get_text()])
    
    if not underlined_ids:
        return None
    return [error_text, url, guideline, underlined_ids]

def src_length_check(page_text):
    '''
    Check if link length is not longer than 80 characters.
        -Keep URLs shorter than 78 characters so they don't wrap when emailed.
    Priority 2 - AA (https://www.w3.org/TR/2003/NOTE-chips-20030128/#gl1)
    @input:
        page_text: Source code of the current web page..
    @output:
        list: list of links > 80
    '''
    soup = BeautifulSoup(page_text.text, 'html.parser')

    a_tags = soup.find_all('a')
    longer_a_tags = []
    for a_tag in a_tags:
        if len(a_tag.find('src')) > 80:
            longer_a_tags.appen(a_tag['src'])
    
    return longer_a_tags

def null_tabindex_check(page_text):
    '''
    Checking if null tabindex attribute is present on any forms or links.
    (https://www.maxability.co.in/2016/06/13/tabindex-for-accessibility-good-bad-and-ugly/)
    @input:
        page_text: Source code of the current web page.
    @output:
        list: List of ids or class with null tabindex.
    '''
    soup = BeautifulSoup(page_text.text, "html.parser")
        
    form_tags = soup.find_all('form')
    a_tags = soup.find_all('a')
    error_ids = []
    for form_tag in form_tags:
        if form_tag.find('tabindex')  == "-1":
            error_ids.append(form_tag['id']) or error_ids.append(form_tag['class'])   
    for a_tag in form_tags:
        if a_tag.find('tabindex')  == "-1":
            error_ids.append(a_tag['id']) or error_ids.append(a_tag['class'])

    return error_ids