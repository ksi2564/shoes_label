from django.urls import path, include

from task.views import task, plustask, login

app_name = "taskapp"

urlpatterns = [
    path('', task, name='task'),
    path('plustask/', plustask, name='plustask'),
    path('login/', login, name='login'),
]
