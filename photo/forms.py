from django.forms import ModelForm

from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto


class ShoesPhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ['image']


class TopCategoryForm(ModelForm):
    class Meta:
        model = TopCategory
        fields = ['topcategory']


class SubCategoryForm(ModelForm):
    class Meta:
        model = SubCategory
        fields = ['topcategory', 'subcategory']


class LabeledPhotoForm(ModelForm):
    class Meta:
        model = LabeledPhoto
        fields = ['labeler', 'topcategory', 'subcategory']
