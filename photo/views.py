# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from photo.forms import ShoesPhotoForm, TopCategoryForm, SubCategoryForm
from photo.models import Photo, TopCategory, SubCategory, Category
from django.shortcuts import redirect,render
from django.views.generic import View


class PhotoList(ListView):
    model = Photo
    template_name = 'photo/photo_list.html'


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

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PhotoDetail, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


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

def addPhoto(request):
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.getlist('image')

        for image in image:
            photo = Photo.objects.create(
                image=image,
            )

        return redirect('/')

    return render(request, 'photo/photo_create.html')


class CategoryView(View):
    template_name = 'category/category.html'
    def get(self, request):
        context = {'categories': Category.objects.all()}

        return render(request, self.template_name, context)