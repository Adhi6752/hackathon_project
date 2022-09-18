from turtle import title
from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=260)
    slug=models.SlugField()
    intro =models.TextField()
    body=models.TextField()
    image=models.ImageField(upload_to='uploads/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('-created_at',)
