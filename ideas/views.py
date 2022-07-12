from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Idea
from .forms import CommentForm


class IdeaList(generic.ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by('title')
    template_name = 'ideas/ideas.html'
    paginate_by = 6


class IdeaDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Idea.objects.filter(status=1)
        idea = get_object_or_404(queryset, slug=slug)
        comments = idea.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if idea.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "ideas/ideas_detail.html",
            {
                "idea": idea,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
                
            },
        )
