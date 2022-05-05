from django.urls import path

from task.views import task, plustask, data_label
from task.views import ShoesDataUploadView

app_name = "taskapp"

urlpatterns = [
    path('', plustask, name='plustask'),
    path('mytask/', task, name='task'),
    path('mytask/data_upload/', ShoesDataUploadView.as_view(), name='data_upload'),
    path('mytask/data_label/', data_label, name='data_label'),
]
