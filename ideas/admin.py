from django.contrib import admin
from .models import Idea, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Idea)
class IdeaAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'updated_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'updated_on')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'idea', 'created_on')
    list_filter = ('created_on',)
    search_fields = ('name', 'email', 'body')




# Register your models here.
