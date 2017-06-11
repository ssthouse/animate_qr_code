from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return render(request, "main/template/hello.html", {})


# def hello(request, number):
#     text = "<h1>welcome to my app number %s!</h1>" % number
#     return HttpResponse(text)
