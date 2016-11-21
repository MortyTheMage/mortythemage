from __future__ import unicode_literals
import datetime
import os
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import escape
from django.utils.safestring import mark_safe

# Create your models here.
class Project(models.Model):
    project_title = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.project_title

class Details(models.Model):
	details = models.ForeignKey(Project, on_delete=models.CASCADE)
	details_text = models.TextField()
	def __str__(self):
		return mark_safe(self.details_text)

class File(models.Model):
    file = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_field = models.FileField(upload_to='')
    def file_name(self):
        return self.file_field.name.replace("./","")
    def read_file(self):
        output = []
        f = open(os.path.join(settings.MEDIA_ROOT, self.file_name()), 'r')
        for line in f:
            output.append(line)
        f.close()
        return output
    def __str__(self):
        return self.file_field.name