from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app_string1(request):
    return HttpResponse('<h1>hii this is my first string</h1>')
