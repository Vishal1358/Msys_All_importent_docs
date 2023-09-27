# i Have created this file
from django.http import HttpResponse


#  this code for understanding of urls.py and views.py
# def index(request):
#     return HttpResponse("<h1>Hello</h1> <a href='https://chat.openai.com/?model=text-davinci-002-render-sha'> Django ChatGpt</a> ")
#
# def about(request):
#     return HttpResponse("Hello About")



def index(request):
    return HttpResponse("Hello..!")

def removepunc(request):
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newlineremove")

def spaceremove(request):
    return HttpResponse("spaceremove")

def charcount(request):
    return HttpResponse("charcount")

