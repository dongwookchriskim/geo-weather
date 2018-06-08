from django.shortcuts import render
from django.http import HttpResponse

def alert(request):
    context = {}
    return render(request, 'weather/alert.html', context)

def index(request):
    context = {}
    return render(request, 'weather/index.html', context)