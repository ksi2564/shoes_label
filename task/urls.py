# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path

from task.views import plustask, data_label, ShoesDataUploadView, ShoesList

# from task.views import ShoesDataUploadView

app_name = "taskapp"

urlpatterns = [
    path('', plustask, name='plustask'),
    path('mytask/', ShoesList.as_view(), name='task'),
    path('mytask/data_upload/', ShoesDataUploadView.as_view(), name='data_upload'),
    path('mytask/data_label/', data_label, name='data_label'),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
