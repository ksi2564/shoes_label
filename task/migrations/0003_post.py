# Generated by Django 4.0.3 on 2022-05-03 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_photo_delete_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]