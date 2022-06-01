# Generated by Django 4.0.3 on 2022-06-01 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0017_remove_photo_labeled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='labeledphoto',
            options={'ordering': ['created']},
        ),
        migrations.AlterModelOptions(
            name='photo',
            options={'ordering': ['created']},
        ),
        migrations.CreateModel(
            name='ExamPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspector', models.CharField(max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('exam_image', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='exam_image', to='photo.labeledphoto')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
