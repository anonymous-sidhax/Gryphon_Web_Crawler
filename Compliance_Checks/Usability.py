from bs4 import BeautifulSoup 

def underlined_text_is_not_a_link_check(page_text):
    '''
    Check if underlined text is not a link.
        -Avoid underlined text - people will click on it and think it's a broken link.
    Priority 2 - AA (https://www.powermapper.com/products/sortsite/rules/usegov10.4/)
    @input:
        page_text: Source code of the current web page..
    @output:
        boolean: True (if underlined text is not a link) else False
    '''
    soup = BeautifulSoup(page_text.text, 'html.parser')

    u_tags = soup.find_all('u')

    for underlined in u_tags:
        if '<a' not in underlined.get_text():
            return True
    
    return False

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

