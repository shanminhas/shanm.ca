from . import views
from django.urls import path
from users import views as user_views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', views.home, name='homepage-home'),
    path('about/', views.about, name='homepage-about'),
    path('projects/', views.projects, name='homepage-projects'),  # posts
    path('post/<slug:slug>/',
         PostDetailView.as_view(), name='project-detail')
]
