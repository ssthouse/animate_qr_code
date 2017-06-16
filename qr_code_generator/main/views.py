from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
import datetime
from main.models import Dreamreal, GifModel
from main.forms import LoginForm, GifForm, DownloadForm
from main.tools.GifGenerator import GifGenerator


# Create your views here.


def index(request):
    return render(request, 'main/template/index.html')


def readFile(filename, chunk_size=512):
    with open(filename, 'rb') as f:
        while True:
            c = f.read(chunk_size)
            if c:
                yield c
            else:
                break


def download_gif(request):
    downloadForm = DownloadForm(request.POST)
    if request.method != "POST" or not downloadForm.is_valid():
        return render(request, 'main/template/error.html', {})
    file_path = downloadForm.cleaned_data['download_path']
    open(file_path, "rb")
    response = StreamingHttpResponse(readFile(file_path))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(file_path)
    return response


def submit_img(request):
    # TODO: 处理图片数据
    saved = False
    gifForm = GifForm(request.POST, request.FILES)
    # 异常判断
    if request.method != "POST" or not gifForm.is_valid():
        return render(request, 'main/template/error.html', {})

    gifModel = GifModel()
    gifModel.url = gifForm.cleaned_data['url']
    gifModel.colorful = gifForm.cleaned_data['colorful']
    gifModel.picture = gifForm.cleaned_data['picture']
    gifModel.save()
    # 去掉static的图片路径 ==> 用于template
    abs_path = str(gifModel.picture)
    pic_path = abs_path[abs_path.find('/') + 1:]
    filename = pic_path[pic_path.find('/') + 1:]
    print("pic_path:  " + pic_path)

    # TODO: 初始化动图生成器 尝试调用动图生成器
    gifGenerator = GifGenerator(gifForm.cleaned_data['url'], abs_path, False)
    gifGenerator.generate_gif_with_gif()
    result_path = gifGenerator.get_result_path()
    gifModel.result = result_path
    gifModel.save()
    gif_path = result_path[result_path.find('/') + 1:]

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
