from . import views
from django.urls import path

urlpatterns = [
    path('ideas/', views.IdeaList.as_view(), name='ideas'),
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
]
