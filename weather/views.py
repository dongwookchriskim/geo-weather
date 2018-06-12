from django.shortcuts import render
from django.http import HttpResponse

def alert(request):
    return render(request, 'weather/alert.html')

def index(request):
    return render(request, 'weather/index.html')