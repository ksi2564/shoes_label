from django.urls import path, include

from task.views import task, uplaod_data, data_label, img_btn

app_name = "taskapp"

urlpatterns = [
    path('', task, name='task'),
    path('data_upload/', uplaod_data, name='upload_data'),
    path('data_label/', data_label, name='data_label'),
    path('img_btn/', img_btn, name='img_btn'),
]
