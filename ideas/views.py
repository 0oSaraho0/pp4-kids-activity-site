from django.shortcuts import render
from django.views import generic
from .models import Idea


class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by('title')
    template_name = 'ideas/ideas.html'
    paginate_by = 6


# Create your views here.
