# Generated by Django 4.0.3 on 2022-06-02 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0018_alter_labeledphoto_options_alter_photo_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examphoto',
            name='inspector',
            field=models.CharField(default='tester', max_length=32),
        ),
    ]
