from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone
from django.views import generic
from .models import Project, Detail, File

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'projects/index.html'
    content_object_name = 'latest_project_list'
    def get_queryset(self):
        """ Return the most recent comic """
        return Project.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
	model = Project
	template_name = 'projects/details.html'