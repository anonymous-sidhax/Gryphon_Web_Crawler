# Checking broken links

from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import requests
import time

def main():
    url = input("Enter a URL or a website: ")
    start_time = time.time()
    internal_broken_links, external_broken_links = get_broken_links(url)
    print(internal_broken_links)
    print(external_broken_links)
    end_time = time.time()
    print (end_time-start_time)

# Function for validating HTTP status Code
def validate_url(url, broken_links):
        try:
            response = requests.head(url)
            if response.status_code == 404:
                return broken_links.append(url)
            return broken_links
        except Exception as e:
            return broken_links

def get_broken_links(url):

    # Getting root domain for checking internal links
    root_domain = urlparse(url).netloc
    root_domain = ('.'.join(root_domain.split('.')[1:]))

    # Getting webpage text for searching href links
    try:
        webpage = requests.get(url).text
    except:
        return [], []

    # Parsing HTML
    soup = BeautifulSoup(webpage, features='html.parser')

    # Create a list containing all links with the root domain.
    links = [link.get("href") for link in soup.find_all("a")]

    # Initialize list for broken links.
    broken_links, internal_broken_links, external_broken_links = [], [], []

    # Loop through links checking for 404 responses, and append to list.
    # for link in links:
    #     try:
    #         if root_domain in link:
    #             internal_broken_links = validate_url(link, internal_broken_links)
    #         else:
    #             external_broken_links = validate_url(link, external_broken_links)
    #     except:
    #         continue    
    try:
        with ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(validate_url, links)
    except:
        pass

    for link in broken_links:
        try:
            if root_domain in broken_links:
                internal_broken_links = internal_broken_links.append(link)
            else:
                external_broken_links = external_broken_links.append(link)
        except:
            continue     

    return internal_broken_links, external_broken_links

main()