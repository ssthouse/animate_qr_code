from django.shortcuts import render
from django.http import HttpResponse
import datetime
from main.models import Dreamreal

# Create your views here.


def hello(request, number=1):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "main/template/hello.html", {'today': today, 'days_of_week': daysOfWeek})


def article(request, number):
    text = 'Displaying article number: %s' % number
    return HttpResponse(text)


def crudops(request):
    # create an entry
    dreamreal = Dreamreal(website="https://github.com",
                          mail="ssthouse@163.com", name="sorex", phonenumber="18771037960")
    dreamreal.save()

    # read all entries
    objects = Dreamreal.objects.all()
    res = 'Printing all Dreamreal entries in the DB : <br>'
    for elt in objects:
        res += elt.name + '<br>'

    # read a specific entry
    sorex = Dreamreal.objects.get(name='sorex')
    res += "Pringint one result:<br>"
    res += sorex.name + '<br>'

    # delete one entry
    res += 'Deleting one entry:<br><br>'
    sorex.delete()

    # update one entry

    dreamreal = Dreamreal(website="https://github.com",
                          mail="ssthouse@163.com", name="sorex", phonenumber="18771037960")
    dreamreal.save()
    res += "Updating one entry:<br><br>"
    dreamreal = Dreamreal.objects.get(name='sorex')
    dreamreal.name = 'ssthouse'
    dreamreal.save()
    return HttpResponse(res)
