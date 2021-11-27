from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "home.html")

def load_url_queue(request):
    if request.method == "POST":
        print(request.POST.get("website-url", ""))
        return JsonResponse({})