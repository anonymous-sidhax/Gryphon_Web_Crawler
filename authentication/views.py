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

# For SSL
import socket
import ssl
import datetime
from urllib.parse import urlparse

# pip3 install requests
import requests

# pip3 install lxml
from lxml import etree
from lxml.html import iterlinks, resolve_base_href, make_links_absolute

from Compliance_Checks import Accessibility, Errors, Search, Usability


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
SUMMARY, ACCESSIBILITY, ERRORS, SEARCH, STANDARDS, COMPATIBILITY, USABILITY, COOKIES = {}, {}, {}, {}, {}, {}, {}, {}
ERROR_COUNT, ACCESSIBILITY_COUNT, COMPATIBILITY_COUNT, SEARCH_COUNT, STANDARDS_COUNT, USABILITY_COUNT = 1, 1, 1, 1, 1, 1

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

def cookie_checker(page):
    cookies = {}
    for cookie in page.cookies:
        cookies[cookie.name] = [cookie.value, cookie.expires]    
        
    return JsonResponse(
        cookies
    )

def ssl_expiry_datetime(hostname):
    ssl_dateformat = r'%b %d %H:%M:%S %Y %Z'

    context = ssl.create_default_context()
    context.check_hostname = False

    conn = context.wrap_socket(
        socket.socket(socket.AF_INET),
        server_hostname=hostname,
    )
    # 5 second timeout
    conn.settimeout(5.0)

    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    # Python datetime object
    return datetime.datetime.strptime(ssl_info['notAfter'], ssl_dateformat)

# You can't access this endpoint from GET method
def crawler(request):
    if request.method == "POST":
        
        base_url = json.loads(request.body)['url'] # URL from the input field
        start_time = time.time()
        global LINKS, IMAGES, VIDEOS, DOCS, AUDIO, FILES, SCRIPTS, OTHER_TYPES
        global CRAWLED_URLS, NEW_URLS, URLS
        global ACCESSIBILITY, Errors, COMPATIBILITY, STANDARDS, SUMMARY, COOKIES
        global ERROR_COUNT
        Accessibility_count, Error_count, Search_count, Usability_count = 0, 0, 0, 0

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


        # SSL
        now = datetime.datetime.now()
        try:
            expire = ssl_expiry_datetime(urlparse(base_url).netloc)
            if expire > now:
                SUMMARY.update({0 : ["SSL Certificate Proper", base_url, "SSL Expiry: " + expire, ["-"]]})
            else:
                SUMMARY.update(["SSL Certificate Expired", base_url, "SSL Expiry: " + expire, ["-"]])
        except Exception as e:
            print (e)
            SUMMARY.update(["SSL Error", base_url, "No SSL detected", ["-"]])
        
        # Cookies
        COOKIES = cookie_checker(page, base_url)
        print (COOKIES)

        for link in LINKS:
            try:
                page = requests.get(link, headers=HEADERS, allow_redirects=True, timeout=2) # Get Page
            except requests.exceptions.RequestException as e:
                print (e)
                continue
            
            # All Compliance Checks
            # Update it to a list and run a for loop instead of calling each function everytime.
            duplicate_id_check = Accessibility.duplicate_id_check(page.content, link)
            blank_body_check = Errors.blank_body_check(page.content, url)
            meta_description_tag_check = Search.meta_description_tag_check(page.content, link)
            title_tag_check = Search.title_tag_check(page.content, link)
            underlined_text_is_not_a_link_check = Usability.underlined_text_is_not_a_link_check(page.content, link)

            if duplicate_id_check is not None:
                ACCESSIBILITY.update({Accessibility_count : duplicate_id_check})
                Accessibility_count += 1
            if blank_body_check is not None:
                ERRORS.update({Error_count : blank_body_check})
                Error_count += 1
            if Search.meta_description_tag_check:
                SEARCH.update({Search_count : meta_description_tag_check})
                Search_count += 1
            if Search.title_tag_check is not None:
                SEARCH.update({Search_count : title_tag_check})
                Search_count += 1
            if Usability.underlined_text_is_not_a_link_check is not None:
                USABILITY.update({Usability_count : underlined_text_is_not_a_link_check})
                Usability_count += 1

            # SSL
            now = datetime.datetime.now()
            try:
                expire = ssl_expiry_datetime(urlparse(link).netloc)
                if expire > now:
                    pass
                else:
                    SUMMARY.update(["SSL Error", link, "SSL Certificate Expired", ["-"]])
            except Exception as e:
                print (e)
                SUMMARY.update(["SSL Error", link, "No SSL Certificate Detected.", ["-"]])

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
        print (ERRORS)
        print ({"SUMMARY" : SUMMARY,
            "Errors": ERRORS, 
            "Standards": STANDARDS,
            "Compatibility": COMPATIBILITY,
            "Accessibility": ACCESSIBILITY,
            "Search" : SEARCH,
            "Usability" : USABILITY
            })
        return JsonResponse(
            {"Errors": ERRORS, 
            "Standards": STANDARDS,
            "Compatibility": COMPATIBILITY,
            "Accessibility": ACCESSIBILITY,
            "Search" : SEARCH,
            "Usability" : USABILITY
            }
            )
    else:
        return HttpResponseForbidden()
# return JsonResponse(
# {"Errors": {0: ["Error Description", "URL1", "GUILDELINE1", "ERROR TEXT2"], 1: ["Error Description 2", "URL2", "GUILDELINE1", "ERROR TEXT1"]},
# "Compatibility": {0: [], 1: []}, 
# "Standards": {0:[], 1:[]}}
# )