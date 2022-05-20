from django.contrib import admin

# Register your models here.
from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto

admin.site.register(Photo)
admin.site.register(LabeledPhoto)
admin.site.register(TopCategory)
admin.site.register(SubCategory)
