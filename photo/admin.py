from django.contrib import admin

# Register your models here.
from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto, ExamPhoto

admin.site.register(Photo)
admin.site.register(LabeledPhoto)
admin.site.register(TopCategory)
admin.site.register(SubCategory)
admin.site.register(ExamPhoto)
