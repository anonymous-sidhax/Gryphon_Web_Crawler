from threading import Lock
import threading
import requests, json, mimetypes, time
from concurrent.futures import ThreadPoolExecutor


# pip3 install lxml
from lxml import etree
from lxml.html import iterlinks, resolve_base_href, make_links_absolute

from Compliance_Checks import Accessibility

'''
Sets all of the variables for crawling,
and as a result can be used for effectively resetting the crawler.
'''

# Getting Arguments
VERSION = '0.0.1'

# Initializing global variables
HEADERS = {
'gryphon': json.dumps({
    'User-Agent': 'Gryphon Web Crawler (Windows NT 10.0; bot; +https://github.com/anonymous-sidhax/Gryphon_Web_Crawler)',
    'Accept-Language': 'en_US, en-US, en',
    'Accept-Encoding': 'gzip',
    'Connection': 'keep-alive'
    })
}
LINKS, IMAGES, VIDEOS, DOCS, AUDIO, FILES, SCRIPTS, OTHER_TYPES = [], [], [], [], [], [], [], []
CRAWLED_URLS, NEW_URLS, URLS = [], [], []
ACCESSIBILITY = {}
ERROR_COUNT = 1

def get_all_website_links(url):
    global NEW_URLS, CRAWLED_URLS, URLS

    if url not in CRAWLED_URLS:
        if mimetypes.guess_type(url)[0] == None:
            try:
                page = requests.get(url, headers=HEADERS, allow_redirects=True, timeout=2) # Get Page
            except requests.exceptions.RequestException as e:
                return NEW_URLS
            
            # Getting all URLs from <a> tags - href
            try:
                # Pull out all links after resolving them using any <base> tags found in the document.
                NEW_URLS.extend([url for element, attribute, url, pos in iterlinks(resolve_base_href(make_links_absolute(page.content, url)))])
            except etree.ParseError:
                pass
                
            # To remove duplicate links
            NEW_URLS = remove_duplicates(NEW_URLS)

            return NEW_URLS
        else:
            return NEW_URLS
    else:
        return NEW_URLS


def remove_duplicates(duplicate_list):
    '''
    Removing duplicate values from a list.
    '''
    if duplicate_list is not None:
        unique_list = list(set(duplicate_list))
        return unique_list
    return duplicate_list


def crawler():
    print ("test")
    # start_time = time.time()
    # global LINKS, IMAGES, VIDEOS, DOCS, AUDIO, FILES, SCRIPTS, OTHER_TYPES
    # global CRAWLED_URLS, NEW_URLS, URLS
    # global ACCESSIBILITY
    # global ERROR_COUNT

    # #base_url = request.Get.get('base_url')
    # base_url = "https://www.wikipedia.com"

    # try:
    #     page = requests.get(base_url, headers=HEADERS, allow_redirects=True, timeout=2) # Get Page
    # except requests.exceptions.RequestException as e:
    #     print (e)
    
    # # Getting all URLs from <a> tags - href
    # try:
    #     # Pull out all links after resolving them using any <base> tags found in the document.
    #     urls = [url for element, attribute, url, pos in iterlinks(resolve_base_href(make_links_absolute(page.content, base_url)))]
    # except etree.ParseError:
    #     # If the document is not HTML content this will return an empty list.
    #     print("error")
    
    # # To remove duplicate links
    # NEW_URLS.extend(urls)
    # NEW_URLS = remove_duplicates(NEW_URLS)
    
    # for url in NEW_URLS:
    #     try:
    #         Lock = threading.Lock()
    #         with ThreadPoolExecutor(max_workers=None) as executor:
    #             Lock.acquire()
    #             URLS.extend(executor.map(get_all_website_links))
    #             Lock.release()
    #     except Exception as e:
    #         print (e)
    #         print (url)
    #     #NEW_URLS.extend(get_all_website_links(url))

    #     # Getting seperate mimetypes in variables so that we can crawl only links and not images/videos etc. 
    #     mimetype = mimetypes.guess_type(url)[0]
    #     if mimetype != None:
    #         mimestart = mimetype.split('/')[0]
    #         if mimestart == 'audio':
    #             VIDEOS.extend(url)
    #         elif mimestart == 'video':
    #             VIDEOS.extend(url)
    #         elif mimestart == 'image':
    #             IMAGES.extend(url)
    #         elif mimestart == 'text':
    #             FILES.extend(url)
    #         elif 'script' in mimetype:
    #             SCRIPTS.extend(url)    
    #         else:
    #             OTHER_TYPES.extend(url)
    #     else:
    #         LINKS.extend(url)
    #     CRAWLED_URLS.extend(url)
    #     NEW_URLS.extend(URLS)
    #     URLS = []

    # print(len(LINKS))
    # print(len(IMAGES))
    # print(len(VIDEOS))
    # print(len(FILES))
    # print(len(OTHER_TYPES))
    # print(len(SCRIPTS))
    # end_time = time.time()
    # print (end_time-start_time)
    
    # for link in LINKS:
    #     try:
    #         page = requests.get(link, headers=HEADERS, allow_redirects=True, timeout=2) # Get Page
    #     except requests.exceptions.RequestException as e:
    #         print (e)

    #     check = Accessibility.duplicate_id_check(page.content, link)
        
    #     if check is not None:
    #         ACCESSIBILITY[ERROR_COUNT] = check
    #         ERROR_COUNT+=1

    # #print (ACCESSIBILITY)
    return {0: ["Duplicate id - the same ID is used on more than one element.", "https://www.google.com", "WCAG 2.0 A 4.1.1", "https://www.w3.org/TR/2008/REC-WCAG20-20081211/#ensure-compat-parses", ['abc', 'def']]}

crawler()

# Debugging
print(mimetypes.guess_type("https://www.wikipedia.com/portal/wikipedia.org/assets/js/gt-ie9-ce3fe8e88d.js"))