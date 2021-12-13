import requests
from django.http import JsonResponse
from datetime import datetime

def cookie_checker(page_text, url):

    try:
        page = requests.get(url, allow_redirects=True, timeout=2) # Get Page
    except requests.exceptions.RequestException as e:
        print (e)


    cookies = {}
    for cookie in page.cookies:
        cookies[cookie.name] = [cookie.value, cookie.expires]     
        
    print (cookies)

    return JsonResponse(
        cookies
    )

cookie_checker("asdsa", "https://www.youtube.com")