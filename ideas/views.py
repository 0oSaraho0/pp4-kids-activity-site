from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
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
        comments = idea.comments.order_by("-created_on")
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

    def post(self, request, slug, *args, **kwargs):
        queryset = Idea.objects.filter(status=1)
        idea = get_object_or_404(queryset, slug=slug)
        comments = idea.comments.order_by("-created_on")
        liked = False
        if idea.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.idea = idea
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "ideas/ideas_detail.html",
            {
                "idea": idea,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
                
            },
        )


class IdeaLike(View):

    def post(self, request, slug):
        idea = get_object_or_404(Idea, slug=slug)

        if idea.likes.filter(id=request.user.id).exists():
            idea.likes.remove(request.user)
        else:
            idea.likes.add(request.user)

        return HttpResponseRedirect(reverse('idea_detail', args=[slug]))

