from __future__ import unicode_literals
import datetime
from django.utils import timezone
from django.utils.html import escape
from django.utils.safestring import mark_safe
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Comic(models.Model):
    comic_title = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.comic_title

class Content(models.Model):
    comic = models.ForeignKey(Comic, on_delete=models.CASCADE)
    comic_img = models.ImageField(upload_to='images/')
    comic_alt = models.CharField(max_length=256)
    def __str__(self):
        return mark_safe(self.comic_alt)