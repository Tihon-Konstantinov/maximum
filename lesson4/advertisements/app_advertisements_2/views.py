from django.shortcuts import render
from django.http import HttpResponse

def index2(request):
    return HttpResponse('<h1>Домашка по 4 занятию')
