# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from photo.forms import ShoesPhotoForm, TopCategoryForm, SubCategoryForm, LabeledPhotoForm
from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto
from django.shortcuts import redirect, render


def first_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        request.session['labeler'] = name
    return render(request, 'first_page.html')


class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'


class PhotoUpdate(UpdateView):
    model = Photo
    form_class = ShoesPhotoForm
    template_name = 'photo/photo_update.html'
    success_url = '/list/'


class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/list/'


class PhotoDetail(DetailView):
    model = Photo
    template_name = 'photo/photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PhotoDetail, self).get_context_data(**kwargs)
        context['topcategories'] = TopCategory.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context

    @staticmethod
    def post(request, *args, **kwargs):
        new_labeled = LabeledPhoto()
        new_labeled.labeled_image = Photo.objects.get(id=request.POST.get('labeled_image'))
        new_labeled.labeler = request.session['labeler']
        new_labeled.topcategory = request.POST.get('top')
        new_labeled.subcategory = request.POST.get('sub')
        new_labeled.save()

        return redirect('/list/')


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
    success_url = reverse_lazy('photo:labeled_detail')

    def get_success_url(self):
        return reverse('photo:labeled_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super(LabeledPhotoUpdate, self).get_context_data(**kwargs)
        context['topcategories'] = TopCategory.objects.all()
        context['subcategories'] = SubCategory.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        request.POST = request.POST.copy()
        request.POST['labeler'] = request.session['labeler']
        request.POST['topcategory'] = request.POST.get('top')
        request.POST['subcategory'] = request.POST.get('sub')
        return super(LabeledPhotoUpdate, self).post(request, **kwargs)


class LabeledPhotoDelete(DeleteView):
    model = LabeledPhoto
    template_name = 'label/labeled_photo_delete.html'
    success_url = reverse_lazy('photo:labeled_list')
