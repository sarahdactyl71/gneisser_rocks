from django.db import models

#this is kind of like formulating a schema that generates the kind of migration
#file that we are looking for

class Rock(models.Model):

    def __str__(self):
        return self.name

    image_url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=50)
