from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Interest_Group(models.Model):
    group_name = models.CharField("Название Группы", max_length=20)
    group_picture = models.ImageField('Изображения группы', upload_to='media/group_picture')
    group_author = models.ForeignKey(User, on_delete=models.CASCADE)
    group_info = models.CharField('Описание группы', max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.group_name


class GroupPost(models.Model):
    group = models.ForeignKey("Interest_Group", on_delete=models.CASCADE, related_name='posts')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Расскажите что сегодня было интересного', blank=True, null=True)
    image = models.ImageField(upload_to='media/group_post_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
