from django.urls import path

from task.views import task, data_upload, plustask, data_label

app_name = "taskapp"

urlpatterns = [
    path('', plustask, name='plustask'),
    path('mytask/', task, name='task'),
    path('mytask/data_upload/', data_upload, name='data_upload'),
    path('mytask/data_label/', data_label, name='data_label'),
]
