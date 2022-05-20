from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from photo.views import PhotoList, PhotoDetail, PhotoUpdate, PhotoDelete, TopCategoryCreate, \
    SubCategoryCreate, addPhoto, labelPhoto, LabeledPhotoList, LabeledPhotoDetail, LabeledPhotoUpdate, \
    LabeledPhotoDelete, CategoryView

app_name = "photo"

urlpatterns = [
    path('', PhotoList.as_view(), name='index'),
    path('create/', addPhoto, name='create'),
    path('update/<int:pk>/', PhotoUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', PhotoDelete.as_view(), name='delete'),
    path('detail/<int:pk>/', labelPhoto, name='detail'),

    path('labeled/list', LabeledPhotoList.as_view(), name='labeled_list'),
    path('labeled/detail/<int:pk>', LabeledPhotoDetail.as_view(), name='labeled_detail'),
    path('labeled/update/<int:pk>', LabeledPhotoUpdate.as_view(), name='labeled_update'),
    path('labeled/delete/<int:pk>', LabeledPhotoDelete.as_view(), name='labeled_delete'),

    path('topcategory/create/', TopCategoryCreate.as_view(), name='top-category_create'),
    path('subcategory/create/', SubCategoryCreate.as_view(), name='top-category_create'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
