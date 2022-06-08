# Create your views here.
import csv
import datetime

import xlwt
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from photo.decorators import is_login
from photo.forms import ShoesPhotoForm, TopCategoryForm, SubCategoryForm, LabeledPhotoForm
from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto, ExamPhoto
from django.shortcuts import redirect, render


def first_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        request.session['labeler'] = name
    return render(request, 'first_page.html')


class PhotoList(ListView):
    model = Photo
    paginate_by = 25
    queryset = Photo.objects.filter(labeled_image__isnull=True)
    template_name = 'photo/photo_list.html'


@method_decorator(is_login, name="dispatch")
class PhotoUpdate(UpdateView):
    model = Photo
    form_class = ShoesPhotoForm
    template_name = 'photo/photo_update.html'
    success_url = '/list'


@method_decorator(is_login, name="dispatch")
class PhotoDelete(DeleteView):
    model = Photo
    template_name = 'photo/photo_delete.html'
    success_url = '/list'


@method_decorator(is_login, name="dispatch")
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

        try:
            return redirect('photo:detail', Photo.objects.filter(labeled_image__isnull=True,
                                                                 pk__gt=request.POST.get('labeled_image')).first().pk)
        except:
            return redirect('photo:list')


@method_decorator(is_login, name="dispatch")
class TopCategoryCreate(CreateView):
    model = TopCategory
    form_class = TopCategoryForm
    template_name = 'category/topcategory_create.html'
    success_url = '/topcategory/create'


@method_decorator(is_login, name="dispatch")
class SubCategoryCreate(CreateView):
    model = SubCategory
    form_class = SubCategoryForm
    template_name = 'category/subcategory_create.html'
    success_url = '/subcategory/create'


@is_login
def addPhoto(request):
    if request.method == 'POST':
        image = request.FILES.getlist('image')

        for image in image:
            Photo.objects.create(image=image)

        return redirect('/list')

    return render(request, 'photo/photo_create.html')


@method_decorator(is_login, name="dispatch")
class LabeledPhotoList(ListView):
    model = LabeledPhoto
    paginate_by = 25
    queryset = LabeledPhoto.objects.filter(exam_image__isnull=True)
    template_name = 'label/labeled_photo_list.html'


@method_decorator(is_login, name="dispatch")
class LabeledPhotoDetail(DetailView):
    model = LabeledPhoto
    template_name = 'label/labeled_photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LabeledPhotoDetail, self).get_context_data(**kwargs)

        if LabeledPhoto.objects.count() - ExamPhoto.objects.count() != 1:
            try:
                context['the_prev'] = LabeledPhoto.objects.filter(exam_image__isnull=True,
                                                                  pk__lt=self.object.pk).order_by('-pk').first().pk
            except:
                context['the_prev'] = LabeledPhoto.objects.filter(exam_image__isnull=True,
                                                                  pk__gt=self.object.pk).order_by('-pk').first().pk
            try:
                context['the_next'] = LabeledPhoto.objects.filter(exam_image__isnull=True,
                                                                  pk__gt=self.object.pk).order_by('pk').first().pk
            except:
                context['the_next'] = LabeledPhoto.objects.filter(exam_image__isnull=True,
                                                                  pk__lt=self.object.pk).order_by('pk').first().pk

        return context

    @staticmethod
    def post(request, *args, **kwargs):
        new_examed = ExamPhoto()
        new_examed.exam_image = LabeledPhoto.objects.get(id=request.POST.get('examed_image'))
        new_examed.inspector = request.session['labeler']
        new_examed.save()

        try:
            return redirect('photo:labeled_detail', LabeledPhoto.objects.filter(exam_image__isnull=True,
                                                                                pk__gt=request.POST.get(
                                                                                    'examed_image')).first().pk)
        except:
            return redirect('photo:labeled_list')


@method_decorator(is_login, name="dispatch")
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


@method_decorator(is_login, name="dispatch")
class LabeledPhotoDelete(DeleteView):
    model = LabeledPhoto
    template_name = 'label/labeled_photo_delete.html'
    success_url = reverse_lazy('photo:labeled_list')


@method_decorator(is_login, name="dispatch")
class ExamPhotoList(ListView):
    model = ExamPhoto
    paginate_by = 25
    queryset = ExamPhoto.objects.all()

    def get_template_names(self):
        if self.request.path == reverse('photo:exam_list_detail'):
            return ['exam/exam_photo_list_detail.html']
        return ['exam/exam_photo_list.html']

    def get_context_data(self, **kwargs):
        context = super(ExamPhotoList, self).get_context_data(**kwargs)
        context['image'] = Photo.objects.all()
        context['labeled_image'] = LabeledPhoto.objects.all()
        try:
            context['labeled_per'] = int(context['labeled_image'].count()/context['image'].count()*100)
        except:
            context['labeled_per'] = 0
        try:
            context['examed_per'] = int(self.object_list.count()/context['labeled_image'].count()*100)
        except:
            context['examed_per'] = 0
        context['preview'] = ExamPhoto.objects.all()[:5]

        return context


@method_decorator(is_login, name="dispatch")
class ExamPhotoDetail(DetailView):
    model = ExamPhoto
    template_name = 'exam/exam_photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ExamPhotoDetail, self).get_context_data(**kwargs)

        if ExamPhoto.objects.count() != 1:
            try:
                context['the_prev'] = ExamPhoto.objects.filter(pk__lt=self.object.pk).order_by('-pk').first().pk
            except:
                context['the_prev'] = ExamPhoto.objects.filter(pk__gt=self.object.pk).order_by('-pk').first().pk
            try:
                context['the_next'] = ExamPhoto.objects.filter(pk__gt=self.object.pk).order_by('pk').first().pk
            except:
                context['the_next'] = ExamPhoto.objects.filter(pk__lt=self.object.pk).order_by('pk').first().pk

        return context


@method_decorator(is_login, name="dispatch")
class ExamPhotoDelete(DeleteView):
    model = ExamPhoto
    template_name = 'exam/exam_photo_delete.html'
    success_url = reverse_lazy('photo:exam_list_detail')


def csv_export(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + str(datetime.date.today()) + '.csv'

    writer = csv.writer(response)
    writer.writerow(['파일명', '상위 카테고리', '하위 카테고리', '최종 검수자'])

    csv_datas = ExamPhoto.objects.all().values_list('exam_image__labeled_image__image', 'exam_image__topcategory',
                                                    'exam_image__subcategory', 'inspector')
    for csv_data in csv_datas:
        writer.writerow(csv_data)

    return response


def excel_export(request):
    response = HttpResponse(content_type="application/vnd.ms-excel")
    # 다운로드 받을 때 생성될 파일명 설정
    response["Content-Disposition"] = 'attachment; filename=' \
                                      + str(datetime.date.today()) + '.xls'

    # 인코딩 설정
    wb = xlwt.Workbook(encoding='utf-8')
    # 생성될 시트명 설정
    ws = wb.add_sheet('Shoes Labeling Information')

    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['파일명', '상위 카테고리', '하위 카테고리', '최종 검수자']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = ExamPhoto.objects.all().values_list('exam_image__labeled_image__image', 'exam_image__topcategory',
                                               'exam_image__subcategory', 'inspector')

    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
