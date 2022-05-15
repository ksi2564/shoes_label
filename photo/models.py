from django.db import models

# Create your models here.


class Photo(models.Model):
    image = models.ImageField(upload_to='shoes_data/%Y/%m/%d', name='image')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "image : "+str(self.image)

    class Meta:
        ordering = ['-created']


class TopCategory(models.Model):
    top_category = models.CharField(max_length=64)

    def __str__(self):
        return self.top_category

    class Meta:
        ordering = ['top_category']


class SubCategory(models.Model):
    top_category = models.ForeignKey(TopCategory, on_delete=models.CASCADE, related_name='top')
    sub_category = models.CharField(max_length=64)

    def __str__(self):
        return self.sub_category

    class Meta:
        ordering = ['top_category']


class LabeledPhoto(models.Model):
    labeled_image = models.ForeignKey(Photo, on_delete=models.PROTECT, related_name='labeled_image')
    top_category = models.CharField(max_length=64)
    sub_category = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.labeled_image

    class Meta:
        ordering = ['-created']


