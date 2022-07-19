from . import views
from django.urls import path

urlpatterns = [
    path('ideas/', views.IdeaList.as_view(), name='ideas'),
    path('post/<slug:pk>/<str:title>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:pk>', views.IdeaLike.as_view(), name='idea_like'),
    path('create/', views.IdeaCreate.as_view(), name='create'),
]
