from .models import Comment, Idea
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class IdeaForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = (
            'activity_name',
            'picture',
            'activity_location',
            'age_range',
            'cost',
            'activity_website',
            'review',
        )