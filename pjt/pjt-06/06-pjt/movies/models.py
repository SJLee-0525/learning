from django.db import models
from django.conf import settings

# Create your models here.
class Movie(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='write_movies')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='like_movies')
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='media/')

class Comment(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.CharField(max_length=200)