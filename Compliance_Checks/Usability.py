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
    soup = BeautifulSoup(page_text)

    u_tags = soup.find_all('u')

    for underlined in u_tags:
        if '<a' not in underlined.get_text():
            return True
    
    return False