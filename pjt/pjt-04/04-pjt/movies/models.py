from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class ImageUpload(models.Model):
    image = models.ImageField(upload_to='media/')