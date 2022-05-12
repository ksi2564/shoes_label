# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from photo.forms import ShoesPhotoForm, TopCategoryForm, SubCategoryForm
from photo.models import Photo, TopCategory, SubCategory


class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'


class PhotoCreate(CreateView):
    model = Photo
    form_class = ShoesPhotoForm
    template_name = 'photo/photo_create.html'
    success_url = '/'


class PhotoUpdate(UpdateView):
    model = Photo
    form_class = ShoesPhotoForm
    template_name = 'photo/photo_update.html'
    success_url = '/'


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/'


class PhotoDetail(DetailView):
    model = Photo
    form_class = ShoesPhotoForm
    template_name = 'photo/photo_detail.html'
    success_url = '/'


class TopCategoryCreate(CreateView):
    model = TopCategory
    form_class = TopCategoryForm
    template_name = 'category/topcategory_create.html'
    success_url = '/'


class SubCategoryCreate(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'category/subcategory_create.html'
    success_url = '/subcategory/create/'
