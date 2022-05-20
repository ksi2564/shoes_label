from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin    # 관리자페이지에서 카테고리를 트리형식으로
from photo.models import Photo, TopCategory, SubCategory, LabeledPhoto, Category

admin.site.register(Photo)
admin.site.register(LabeledPhoto)
admin.site.register(TopCategory)
admin.site.register(SubCategory)
admin.site.register(Category, DraggableMPTTAdmin)
