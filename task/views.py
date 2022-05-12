from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from task.models import Photo


def task(request):
    return render(request, 'taskapp/task.html')


def data_upload(request):
    if request.method =="POST":

        tempfile = request.POST.get('hello_world_input')

        new_task = Photo()
        new_task.image = tempfile
        new_task.save()


        return HttpResponseRedirect(reverse('data_upload'))
    else:
        task = task.objects.all()
        return render(request, 'taskapp/data_upload.html', context={'hello_world_list': hello_world_list})

    try:
        post.image = request.FILES['image']
    except:
        post.image = None


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
