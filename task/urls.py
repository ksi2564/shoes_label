from django.urls import path, include

from task.views import task

app_name = "taskapp"

urlpatterns = [
    path('', task, name='task'),
]
