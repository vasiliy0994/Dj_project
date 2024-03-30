from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='medin/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
