from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    job_title = models.CharField(max_length=25)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.name

    