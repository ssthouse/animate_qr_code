from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def hello(request, number=1):
    today = datetime.datetime.now().date()
    return render(request, "main/template/hello.html", {'today': today})


def article(request, number):
    text = 'Displaying article number: %s' % number
    return HttpResponse(text)
