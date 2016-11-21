from __future__ import unicode_literals
from django.contrib import admin
from .models import Project, Detail, File

class FileInline(admin.StackedInline):
    model = File
    extra = 0

class DetailInline(admin.StackedInline):
	model = Detail
	extra = 0

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['project_title']}),
        ('Date Information',    {'fields': ['pub_date']}),
    ]
    inlines = [DetailInline, FileInline]
    search_fields = ['project_title']
    list_filter = ['pub_date']
    list_display = ['project_title']
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# Register your models here.
admin.site.register(Project, ProjectAdmin)