import json
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.http import JsonResponse
import Utils.views as a


def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "home.html")

# You can't access this endpoint from GET method
def crawler(request):
    if request.method == "POST":
        url = json.loads(request.body)['url'] # URL from the input field
        return JsonResponse(
            {"Errors": {0: ["Duplicate id - the same ID is used on more than one element.", "https://www.google.com/", "WCAG 2.0 A 4.1.1", "https://www.w3.org/TR/2008/REC-WCAG20-20081211/#ensure-compat-parses", ['abc', 'def']]}, 
            "Standards" : {0 : ["same format as errors"]}, 
            "Compatibility": {0 : [""]}})
    else:
        return HttpResponseForbidden()

def load_url_queue(request):
    base_url = ["https://wikipedia.com"]
    print (base_url)
    #return base_url

def test(request):
    print("Hello WOrld")
    return HttpResponse("<html><script>window.location.replace('/');</script></html>")
