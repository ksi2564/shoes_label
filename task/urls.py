from django.urls import path, include

from task.views import task, uplaod_data

app_name = "taskapp"

urlpatterns = [
    path('', task, name='task'),
    path('data_upload/', uplaod_data, name='upload_data'),
]
