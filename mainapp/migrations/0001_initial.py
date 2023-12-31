# Generated by Django 4.1.7 on 2023-06-16 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mainapp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('preview', models.ImageField(upload_to='images/', validators=[mainapp.validators.valid_image, mainapp.validators.valid_size], verbose_name='Превью')),
                ('file', models.FileField(upload_to='video/', validators=[mainapp.validators.valid_video, mainapp.validators.valid_size], verbose_name='Видеофайл')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('dislikes', models.ManyToManyField(blank=True, related_name='dislikes', to=settings.AUTH_USER_MODEL)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=100, verbose_name='Описание')),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.video')),
            ],
        ),
    ]
