from __future__ import unicode_literals
from django.contrib import admin
from .models import Comic, Content

class ContentInline(admin.StackedInline):
    model = Content
    extra = 1

class ComicAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['comic_title']}),
        ('Date Information',    {'fields': ['pub_date']}),
    ]
    inlines = [ContentInline]
    list_display = ['comic_title']

# Register your models here.
admin.site.register(Comic, ComicAdmin)