from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from task.forms import ShoesDataCreationForm
from task.models import ShoesData


def task(request):
    return render(request, 'taskapp/task.html')


# def data_upload(request):
#     return render(request, 'taskapp/data_upload.html')


def first_page(request):
    return render(request, 'taskapp/first_page.html')


def free_trial(request):
    return render(request, 'taskapp/free_trial.html')


def plustask(request):
    return render(request, 'taskapp/plustask.html')


def login(request):
    return render(request, 'taskapp/login.html')


def data_label(request):
    return render(request, 'taskapp/data_label.html')


class ShoesDataUploadView(CreateView):
    model = ShoesData
    context_object_name = 'task_data'
    form_class = ShoesDataCreationForm
    success_url = reverse_lazy('taskapp:task')
    template_name = 'taskapp/data_upload.html'
