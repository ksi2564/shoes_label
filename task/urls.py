from django.urls import path, include

from task.views import plustask, login

app_name = "taskapp"

urlpatterns = [
    path('', login, name='task'),
    path('plustask/', plustask, name='plustask'),
]
