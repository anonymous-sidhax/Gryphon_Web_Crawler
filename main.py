from django.http import HttpResponse

def test():
    return HttpResponse("Hello, world. #Homepage")

test()