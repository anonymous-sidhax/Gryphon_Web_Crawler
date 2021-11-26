from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "home.html")

def crawler(request):
    base_url = request.Get.get('base_url')
    print ()

def load_url_queue(request):
    base_url = ["https://wikipedia.com"]
    print (base_url)
    #return base_url
    