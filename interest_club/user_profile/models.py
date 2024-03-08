from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    telegram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    vk_url = models.URLField(blank=True, null=True)
    profile_picture = models.ImageField("Изображения", default="profile_pictures/default_profile_picture.jpg",
                                        null=True,
                                        blank=True, upload_to='media/profile_pictures')
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    post_image = models.ImageField(upload_to='photos/', blank=True, null=True)
    post_content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.post_author.username} - {self.created_at}'
