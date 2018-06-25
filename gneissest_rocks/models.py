from django.db import models

class Rocks(models.Model):
    image_url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=50)
