from django.urls import path, include

from task.views import task, data_upload, first_page, free_trial

app_name = "taskapp"

urlpatterns = [
    path('', task, name='task'),
    path('data_upload/', data_upload, name='data_upload'),
    path('first_page/', first_page, name='first_page'),
    path('free_trial/', free_trial, name='free_trial'),

]
