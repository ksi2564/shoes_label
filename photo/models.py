from django.db import models

# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='shoes_data/%Y/%m/%d', name='image')
    created = models.DateTimeField(auto_now_add=True)

    @property
    def labeled(self):
        try:
            return self.labeled_image is not None
        except LabeledPhoto.DoesNotExist:
            return False

    def __str__(self):
        return "image : " + str(self.image)

    class Meta:
        ordering = ['created']


class TopCategory(models.Model):
    topcategory = models.CharField(max_length=64)

    def __str__(self):
        return self.topcategory


class SubCategory(models.Model):
    topcategory = models.ForeignKey(TopCategory, on_delete=models.CASCADE)
    subcategory = models.CharField(max_length=64)

    def __str__(self):
        return self.subcategory

    class Meta:
        ordering = ['topcategory']


class LabeledPhoto(models.Model):
    labeled_image = models.OneToOneField(Photo, on_delete=models.PROTECT, related_name='labeled_image')
    topcategory = models.CharField(max_length=64)
    subcategory = models.CharField(max_length=64)
    labeler = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '작업자: ' + self.labeler + ' / ' + str(self.labeled_image)

    class Meta:
        ordering = ['created']


class ExamPhoto(models.Model):
    exam_image = models.OneToOneField(LabeledPhoto, on_delete=models.PROTECT, related_name='exam_image')
    inspector = models.CharField(max_length=32)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '검수자: ' + self.inspector + ' / ' + str(self.exam_image)

    class Meta:
        ordering = ['created']
