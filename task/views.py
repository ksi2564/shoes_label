from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


def task(request):
    return render(request, 'taskapp/task.html')


def data_label(request):
    return render(request, 'taskapp/data_label.html')


def img_btn(request):
    return render(request, 'teskapp/img_btn.html')


def uplaod_data(request):
    return render(request, 'taskapp/data_upload.html')


class Article:
    pass


class ArticleListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'taskapp/list.html'
    paginate_by = 6