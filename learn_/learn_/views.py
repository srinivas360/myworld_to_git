from django.http import HttpResponse
from django.shortcuts import render

def aboutpage(req):
    return HttpResponse('in about page')

def homepage(req):
    print('--i got in home page')
    # return HttpResponse('in home page')
    return render(req, 'homepage.html')