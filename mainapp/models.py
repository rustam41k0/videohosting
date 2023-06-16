from django.db import models
from authapp.models import User
from django.urls import reverse
from django.utils.timezone import now


class Video(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=40, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='images/', verbose_name='Превью')
    file = models.FileField(upload_to='video/', verbose_name='Видеофайл')
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="dislikes", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view', kwargs={'pk': self.id})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField(verbose_name='Описание', max_length=100, null=False)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=False)
    create_at = models.DateTimeField(default=now, verbose_name='Дата публикации')

    def __str__(self):
        return self.author.username + self.text
