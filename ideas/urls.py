from . import views
from django.urls import path

urlpatterns = [
    path('ideas/', views.IdeaList.as_view(), name='ideas'),
    path('post/<slug:pk>/<str:activity_name>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('delete/<slug:pk>', views.IdeaDelete.as_view(), name='idea_delete'),
    path('like/<slug:pk>', views.IdeaLike.as_view(), name='idea_like'),
    path('create/', views.IdeaCreate.as_view(), name='create'),
    path('edit/<slug:pk>', views.IdeaEdit.as_view(), name='idea_edit')
]
