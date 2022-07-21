from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import CreateView, DetailView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Idea
from .forms import IdeaForm, CommentForm


class IdeaList(ListView):
    """ A view to return a list of ideas"""
    model = Idea
    queryset = Idea.objects.order_by('activity_name')
    template_name = 'ideas/ideas.html'
    paginate_by = 6


class IdeaDetail(DetailView):
    """ A view to see the idea in detail """
    def get(self, request, pk, *args, **kwargs):
        queryset = Idea.objects
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
        queryset = Idea.objects
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
    """ A view to like an idea """

    def post(self, request, pk):
        idea = get_object_or_404(Idea, pk=pk)

        if idea.likes.filter(id=request.user.id).exists():
            idea.likes.remove(request.user)
        else:
            idea.likes.add(request.user)

        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))


class IdeaCreate(CreateView):
    """ A view to create an idea """

    form_class = IdeaForm
    template_name = 'ideas/create_idea.html'
    success_url = "/ideas/ideas/"
    model = Idea

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Idea created successfully')
        return super(IdeaCreate, self).form_valid(form)


class IdeaDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ A view to delete an idea """
    model = Idea
    success_url = "/ideas/ideas/"
    template_name = "ideas/idea_delete_conf.html"

    def test_func(self):
        return self.request.user == self.get_object().author



