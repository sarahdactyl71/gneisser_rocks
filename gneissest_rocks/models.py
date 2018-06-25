from django.db import models

class Rocks(models.Model):
    image_url = models.TextField()
    name = models.CharField(max_length=50)
    description = TextField()
    location = CharField(max_length=50)
