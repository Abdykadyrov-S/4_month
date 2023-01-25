from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.

# def hello(request):
#     my_list = [1,2,3,4]
#     return HttpResponse(my_list)

# def hello(request):
#     body = """
#     <h1>Привет</h1>
#     <p>Параграф</p>
#     """   
#     return HttpResponse(body)



def hello(request):
    return HttpResponse("GeekTech", status=200, headers={"name": "Simon"})


def time(request):
    tim = datetime.datetime.now()
    return HttpResponse(tim)

def goodbye(request):
    return HttpResponse("Goodbye!")

def index(request):
    context = {
        "title": "Главная страница",
        "my_list": [1,2,3,4,5],
    }
    return render(request, "index.html", context)

def about(request):
    context = {
        "title": "О нас"
    }
    return render(request, "about.html", context )

def contacts(request):
    context = {
        "title": "Контакты"
    }
    return render(request, "contacts.html", context )