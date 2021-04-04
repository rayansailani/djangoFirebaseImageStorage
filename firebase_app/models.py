from django.db import models

# Create your models here.


class URLS(models.Model):
    imageURL = models.URLField(max_length=2033, default=None)
