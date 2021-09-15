from django.db import models

# Create your models here.

class blog_post(models.Model):
    heading=models.CharField(max_length=100)
    paragraph=models.TextField(max_length=10000)
