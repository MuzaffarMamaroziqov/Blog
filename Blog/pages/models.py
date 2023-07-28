from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=50)
    body=models.TextField(null=True)
    author=models.ForeignKey(
        'auth.User' ,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_list', args=[str(self.pk)])