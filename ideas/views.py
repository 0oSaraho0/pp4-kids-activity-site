from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import CreateView, DetailView, ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Idea
from .forms import IdeaForm, CommentForm


class IdeaList(ListView):
    model = Idea
    queryset = Idea.objects.filter(status=1).order_by('title')
    template_name = 'ideas/ideas.html'
    paginate_by = 6


class IdeaDetail(DetailView):
    def get(self, request, pk, *args, **kwargs):
        queryset = Idea.objects.filter(status=1)
        idea = get_object_or_404(queryset, pk=pk)
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

    def post(self, request, pk, *args, **kwargs):
        queryset = Idea.objects.filter(status=1)
        idea = get_object_or_404(queryset, pk=pk)
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


class IdeaLike(CreateView):

    def post(self, request, pk):
        idea = get_object_or_404(Idea, pk=pk)

        if idea.likes.filter(id=request.user.id).exists():
            idea.likes.remove(request.user)
        else:
            idea.likes.add(request.user)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class IdeaCreate(CreateView):

    form_class = IdeaForm
    template_name = 'ideas/create_idea.html'
    success_url = "/ideas/ideas/"
    model = Idea

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Idea created successfully')
        return super(IdeaCreate, self).form_valid(form)


