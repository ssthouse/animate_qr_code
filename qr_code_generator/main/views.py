from django.shortcuts import render
from django.http import HttpResponse
import datetime
from main.models import Dreamreal, GifModel
from main.forms import LoginForm, GifForm


# Create your views here.


def index(request):
    return render(request, 'main/template/index.html')


# TODO: 处理图片数据
def submit_img(request):
    saved = False
    if request.method == "POST":
        gifForm = GifForm(request.POST, request.FILES)
        if gifForm.is_valid():
            gifModel = GifModel()
            gifModel.url = gifForm.cleaned_data['url']
            gifModel.colorful = gifForm.cleaned_data['colorful']
            gifModel.picture = gifForm.cleaned_data['picture']
            gifModel.save()
            saved = True
            # generate file path
            abs_path = str(gifModel.picture)
            pic_path = abs_path[abs_path.find('/') + 1:]
            print("pic_path:  " + pic_path)
        else:
            print("the form is invalid!!!!!!!!!!!!!!!!")
    else:
        gifForm = GifForm()
        print("the form is not POST!!!!!!!!!!!!!!!!")

    return render(request, 'main/template/success.html', locals())


def hello(request, number=1):
    today = datetime.datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "main/template/hello.html", {'today': today, 'days_of_week': daysOfWeek})


def article(request, number):
    text = 'Displaying article number: %s' % number
    return HttpResponse(text)


def connect(request):
    return render(request, 'main/template/login.html')


def login(request):
    username = "not logged in"
    if request.method == "POST":
        MyLoginForm = LoginForm(request.POST)
        if (MyLoginForm.is_valid()):
            username = MyLoginForm.cleaned_data['username']
    else:
        MyLoginForm = LoginForm()
    return render(request, 'main/template/loggedin.html', {'username': username})


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
