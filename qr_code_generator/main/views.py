from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def hello(request, number=1):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "main/template/hello.html", {'today': today, 'days_of_week': daysOfWeek})


def article(request, number):
    text = 'Displaying article number: %s' % number
    return HttpResponse(text)
