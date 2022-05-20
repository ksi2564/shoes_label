from django.forms import ModelForm

from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto


class ShoesPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image']


class TopCategoryForm(ModelForm):
    class Meta:
        model = TopCategory
        fields = ['top_category']


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = ['top_category', 'sub_category']


class LabeledPhotoForm(ModelForm):
    class Meta:
        model = LabeledPhoto
        fields = ['top_category', 'sub_category']
