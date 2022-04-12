from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def task(request):
    return render(request, 'taskapp/task.html')

def plustask(request):
    return render(request, 'taskapp/plustask.html')


def login(request):
    return render(request, 'taskapp/login.html')


def uplaod_data(request):
    return render(request, 'taskapp/data_upload.html')