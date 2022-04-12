from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def task(request):
    return render(request, 'taskapp/task.html')


def data_upload(request):
    return render(request, 'taskapp/data_upload.html')


def first_page(request):
    return render(request, 'taskapp/first_page.html')


def free_trial(request):
    return render(request, 'taskapp/free_trial.html')