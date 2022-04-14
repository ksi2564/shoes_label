from django.urls import path, include

from task.views import task, data_upload, first_page, free_trial, plustask, login, data_label

app_name = "taskapp"

urlpatterns = [
    path('', task, name='task'),
    path('plustask/', plustask, name='plustask'),
    path('login/', login, name='login'),
    path('data_upload/', data_upload, name='data_upload'),
    path('first_page/', first_page, name='first_page'),
    path('free_trial/', free_trial, name='free_trial'),
    path('data_label/', data_label, name='data_label'),
]
