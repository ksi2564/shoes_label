# Generated by Django 4.0.3 on 2022-05-20 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0006_photo_labeled_alter_labeledphoto_labeled_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='labeled',
        ),
    ]
