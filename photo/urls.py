from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from photo.views import PhotoList, PhotoDetail, PhotoUpdate, PhotoDelete, PhotoCreate, TopCategoryCreate, \
    SubCategoryCreate

app_name = "photo"

urlpatterns = [
    path('', PhotoList.as_view(), name='index'),
    path('create/', PhotoCreate.as_view(), name='create'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='detail'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),

    path('topcategory/create/', TopCategoryCreate.as_view(), name='top-category_create'),
    path('subcategory/create/', SubCategoryCreate.as_view(), name='top-category_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
