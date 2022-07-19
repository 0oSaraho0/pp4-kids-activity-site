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
            'title',
            'featured_image',
            'activity_location',
            'web_address',
            'content',
        )

        lables = {
            'title': 'Activity Name',
            'featured_image': 'Picture',
            'activity_location': 'Location',
            'web_address': 'Web Link',
            'content': 'Review',
        }
