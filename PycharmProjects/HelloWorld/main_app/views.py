from django.http import HttpResponse
from django.shortcuts import render


def homeView(request):
    return HttpResponse("Hello World")

