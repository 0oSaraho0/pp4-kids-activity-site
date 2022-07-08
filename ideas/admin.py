from django.contrib import admin
from .models import Idea
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Idea)
class IdeaAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')



# Register your models here.
