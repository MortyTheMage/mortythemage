from django.core.urlresolvers import reverse
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils import timezone
from django.views import generic
from .models import Comic, Content

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'comic/index.html'
    content_object_name = 'latest_comic_list'
    def get_queryset(self):
        """ Return the most recent comic """
        return Comic.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Comic
    template_name = 'comic/index.html'
    def get_queryset(self):
        """Excludes any posts that aren't published yet."""
        return Comic.objects.filter(pub_date__lte=timezone.now())
