"""
Gryphon Web Crawler
Built with ❤
"""

from django.shortcuts import render
import time
import queue

from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup

# pip3 install requests
import requests

# pip3 install lxml
from lxml import etree
from lxml.html import iterlinks, resolve_base_href, make_links_absolute

import Utils.views as util
from Compliance_Checks.Search import meta_description_tag_check,title_tag_check
def index(request):
    return render(request, "homepage.html")
    
def analyze(base_url):

    urls = crawl(base_url)
    for url in urls:
        urls = urls.append(get_all_website_links())

    if not meta_description_tag_check:
        # add row in database
        pass
    if not title_tag_check:
        # add row in database
        pass



def initialize():
    '''
    Sets all of the variables for crawling,
    and as a result can be used for effectively resetting the crawler.
    '''
    # Declare global variables
    global VERSION, START_TIME, START_TIME_LONG
    global TODO_FILE, DONE_FILE, ERR_LOG_FILE
    global RESPECT_ROBOTS
    global TODO, DONE, THREAD_COUNT
    global connection
    global TOTAL_DOMAIN_COUNT
    global ERROR_DOMAIN_COUNT
    global VALID_ENTRY_COUNT
    global TOTAL_TIME_TAKEN
    global AVERAGE_TIME_TAKEN
    global HEADERS
    
    # Getting Arguments
    VERSION = '0.0.1'

    # Initializing variables
    url_queue = []
    RESPECT_ROBOTS = False
    TODO_FILE, DONE_FILE = '', ''
    TODO, DONE = queue.Queue(), queue.Queue()
    TOTAL_DOMAIN_COUNT = 0
    ERROR_DOMAIN_COUNT = 0
    VALID_ENTRY_COUNT = 0
    TOTAL_TIME_TAKEN  = 0
    AVERAGE_TIME_TAKEN = 0
    connection = None

    HEADERS = {
    'gryphon': {
        'User-Agent': 'Gryphon Web Crawler (Windows NT 10.0; bot; +https://github.com/anonymous-sidhax/Gryphon_Web_Crawler)',
        'Accept-Language': 'en_US, en-US, en',
        'Accept-Encoding': 'gzip',
        'Connection': 'keep-alive'
        }
    }

def load_url_queue():
    base_url = ["https://wikipedia.com"]
    return base_url

def storing_data_to_database():
    pass

def crawl(base_url):
    global HEADERS, ERROR_DOMAIN_COUNT
    try:
        # Attempt to get size of document in bytes
        size_of_doc = int(requests.head(base_url, headers=HEADERS).headers['Content-length'])
    except KeyError:  # Sometimes Content-Length header is not returned...
        size_of_doc = 1
    except requests.exceptions.RequestException as e:
        # log warnings in db and also count of errors - error_domain_count
        ERROR_DOMAIN_COUNT += 1

    try:
        page = requests.get(base_url, headers=HEADERS, allow_redirects=True, timeout=2) # Get Page
    except requests.exceptions.RequestException as e:
        pass

    # Getting all URLs from <a> tags - href
    try:
        # Pull out all links after resolving them using any <base> tags found in the document.
        urls = [url for element, attribute, url, pos in iterlinks(resolve_base_href(make_links_absolute(page.content, base_url)))]
    except etree.ParseError:
        # If the document is not HTML content this will return an empty list.
        urls = []

    # To remove duplicate links
    urls = list(set(urls))
    
    return urls

def get_all_website_links(url):
    '''
    Returns all URLs from <a> tags - href 
    '''
    urls = set()
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    for a_tag in soup.findAll("a"):
        href = a_tag.attrs.get("href")
        if href == "" or href is None:
            # href empty tag
            continue

        # join the URL if it's relative (not absolute link)
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        # remove URL GET parameters, URL fragments, etc.
        href = parsed_href.scheme + "://" + parsed_href.netloc + parsed_href.path
        print (parsed_href.scheme)
        print (parsed_href.netloc)
        print (parsed_href.path)

        if not util.is_valid(href):
            # not a valid URL
            continue

        # if href in internal_urls:
        #     # already in the set
        #     continue
        # if domain_name not in href:
        #     # external link
        #     if href not in external_urls:
        #         external_urls.add(href)
        #     continue

        urls.add(href)
        #internal_urls.add(href)

    print (len(href))
    return urls

###########
# CLASSES #
###########

class SizeError(Exception):
    """
    Raised when a file is too large to download in an acceptable time.
    """
    pass