import json
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.http import JsonResponse
import Utils.views as a

import time, mimetypes, json
from threading import Lock
import threading
import requests, json, mimetypes, time
from concurrent.futures import ThreadPoolExecutor

# pip3 install requests
import requests

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
ACCESSIBILITY = []
ERROR_COUNT = 1

def remove_duplicates(duplicate_list):
    '''
    Removing duplicate values from a list.
    '''
    if duplicate_list is not None:
        unique_list = list(set(duplicate_list))
        return unique_list
    return duplicate_list

def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "home.html")

# You can't access this endpoint from GET method
def crawler(request):
    if request.method == "POST":
        base_url = json.loads(request.body)['url'] # URL from the input field
        start_time = time.time()
        global LINKS, IMAGES, VIDEOS, DOCS, AUDIO, FILES, SCRIPTS, OTHER_TYPES
        global CRAWLED_URLS, NEW_URLS, URLS
        global ACCESSIBILITY
        global ERROR_COUNT

        #base_url = request.Get.get('base_url')
        # base_url = "https://www.wikipedia.com"

        try:
            page = requests.get(base_url, headers=HEADERS, allow_redirects=True, timeout=2) # Get Page
        except requests.exceptions.RequestException as e:
            print (e)
        
        # Getting all URLs from <a> tags - href
        try:
            # Pull out all links after resolving them using any <base> tags found in the document.
            URLS = [url for element, attribute, url, pos in iterlinks(resolve_base_href(make_links_absolute(page.content, base_url)))]
        except etree.ParseError:
            # If the document is not HTML content this will return an empty list.
            print("error")

        # To remove duplicate links
        URLS = remove_duplicates(URLS)

        for url in URLS:
            
            # try:
            #     Lock = threading.Lock()
            #     with ThreadPoolExecutor(max_workers=None) as executor:
            #         Lock.acquire()
            #         URLS.extend(executor.map(get_all_website_links))
            #         Lock.release()
            # except Exception as e:
            #     print (e)
            #     print (url)
            #NEW_URLS.extend(get_all_website_links(url))

            # Getting seperate mimetypes in variables so that we can crawl only links and not images/videos etc. 
            mimetype = mimetypes.guess_type(url)[0]
            if mimetype != None:
                mimestart = mimetype.split('/')[0]
                if mimestart == 'audio':
                    VIDEOS.extend([url])
                elif mimestart == 'video':
                    VIDEOS.extend([url])
                elif mimestart == 'image':
                    IMAGES.extend([url])
                elif mimestart == 'text':
                    FILES.extend([url])
                elif 'script' in mimetype:
                    SCRIPTS.extend([url])    
                else:
                    OTHER_TYPES.extend([url])
            else:
                LINKS.extend([url])

        for link in LINKS:
            try:
                page = requests.get(link, headers=HEADERS, allow_redirects=True, timeout=2) # Get Page
            except requests.exceptions.RequestException as e:
                print (e)
                continue
            
            duplicate_id_check = Accessibility.duplicate_id_check(page.content, link)
            if duplicate_id_check is not None:
                ACCESSIBILITY.extend(duplicate_id_check)
                #print (ACCESSIBILITY) 
            
            CRAWLED_URLS.extend(link)
            
        print(len(LINKS))
        print(len(IMAGES))
        print(len(VIDEOS))
        print(len(FILES))
        print(len(OTHER_TYPES))
        print(len(SCRIPTS))
        end_time = time.time()
        print (end_time-start_time)
        print (ACCESSIBILITY)
        return JsonResponse(
            {"Errors": {0: ACCESSIBILITY}, 
            "Standards" : {0 : ["same format as errors"]}, 
            "Compatibility": {0 : [""]}})
    else:
        return HttpResponseForbidden()