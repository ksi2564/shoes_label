from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from photo.views import PhotoList, PhotoUpdate, PhotoDelete, TopCategoryCreate, \
    SubCategoryCreate, addPhoto, LabeledPhotoList, LabeledPhotoDetail, LabeledPhotoUpdate, \
    LabeledPhotoDelete, first_page, PhotoDetail

app_name = "photo"

urlpatterns = [
    path('', first_page, name='index'),
    path('list/', PhotoList.as_view(), name='list'),
    path('create/', addPhoto, name='create'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', PhotoDetail.as_view(), name='detail'),

    path('labeled/list', LabeledPhotoList.as_view(), name='labeled_list'),
    path('labeled/detail/<int:pk>', LabeledPhotoDetail.as_view(), name='labeled_detail'),
    path('labeled/update/<int:pk>', LabeledPhotoUpdate.as_view(), name='labeled_update'),
    path('labeled/delete/<int:pk>', LabeledPhotoDelete.as_view(), name='labeled_delete'),

    path('topcategory/create/', TopCategoryCreate.as_view(), name='top-category_create'),
    path('subcategory/create/', SubCategoryCreate.as_view(), name='sub-category_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
