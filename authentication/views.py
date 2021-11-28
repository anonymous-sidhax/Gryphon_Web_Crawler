from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

import Utils.views as a

# Create your views here.
def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "home.html")

def test(request):
    print("Hello WOrld")
    return HttpResponse("<html><script>window.location.replace('/');</script></html>")

def crawler(request):    
    print(a.get_time())
    print ({0: ["Duplicate id - the same ID is used on more than one element.", "https://www.google.com", "WCAG 2.0 A 4.1.1", "https://www.w3.org/TR/2008/REC-WCAG20-20081211/#ensure-compat-parses", ['abc', 'def']]})
    return HttpResponse("<html><script>window.location.replace('/');</script></html>")

def load_url_queue(request):
    base_url = ["https://wikipedia.com"]
    print (base_url)
    #return base_url
    
