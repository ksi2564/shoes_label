# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from photo.forms import ShoesPhotoForm, TopCategoryForm, SubCategoryForm, LabeledPhotoForm
from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto
from django.shortcuts import redirect, render


def first_page(request):
    return render(request, 'first_page.html')


class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'
    queryset = Photo.objects.filter(labeled=False)


class PhotoUpdate(UpdateView):
    model = Photo
    form_class = ShoesPhotoForm
    template_name = 'photo/photo_update.html'
    success_url = '/list/'


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/list/'


def labelPhoto(request, pk):
    if request.method == 'GET':
        labeled = Photo.objects.get(id=pk)
        subcategories = SubCategory.objects.all()
        topcategories = TopCategory.objects.all()
        return render(request, 'photo/photo_detail.html',
                      {'labeled': labeled, 'subcategories': subcategories, 'topcategories': topcategories})

    elif request.method == 'POST':
        new_labeled = LabeledPhoto()
        new_labeled.labeled_image = Photo.objects.get(id=pk)
        new_labeled.top_category = request.POST.get('top')
        new_labeled.sub_category = request.POST.get('sub')
        new_labeled.save()

        labeled = Photo.objects.get(id=pk)
        labeled.labeled = True
        labeled.save()

        return redirect('/list/')
    return render(request, 'photo/photo_detail.html')


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'


class TopCategoryCreate(CreateView):
    model = TopCategory
    form_class = TopCategoryForm
    template_name = 'category/topcategory_create.html'
    success_url = '/topcategory/create/'


class SubCategoryCreate(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'category/subcategory_create.html'
    success_url = '/subcategory/create/'


def addPhoto(request):
    if request.method == 'POST':
        image = request.FILES.getlist('image')

        for image in image:
            Photo.objects.create(image=image)

        return redirect('/list/')

    return render(request, 'photo/photo_create.html')


class LabeledPhotoList(ListView):
    model = LabeledPhoto
    template_name = 'label/labeled_photo_list.html'


class LabeledPhotoDetail(DetailView):
    model = LabeledPhoto
    template_name = 'label/labeled_photo_detail.html'


class LabeledPhotoUpdate(UpdateView):
    model = LabeledPhoto
    form_class = LabeledPhotoForm
    template_name = 'label/labeled_photo_update.html'
    success_url = '/labeled/list'


class LabeledPhotoDelete(DeleteView):
    model = LabeledPhoto
    template_name = 'label/labeled_photo_delete.html'
    success_url = '/labeled/list'
