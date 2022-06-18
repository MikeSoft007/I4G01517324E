from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model

class Post(models.Model):
    class Meta:
        verbose_name = "post"
        verbose_name_plural = "post"

    title = models.CharField(max_length=200)
    text  = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    created_date = models.DateTimeField()
    published_date = models.DateTimeField()