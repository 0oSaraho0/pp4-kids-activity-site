from .models import Comment, Idea
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """ A form to make a comment """
    class Meta:
        model = Comment
        fields = ('body',)


class IdeaForm(forms.ModelForm):
    """ A form to create an idea """
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
        widgets = {
            'review': SummernoteWidget()
        }
