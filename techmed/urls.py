from django.urls import path, include
from . import views
from users import views as user_views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import ProblemListView, ProblemDetailView, ProblemCreateView, ProblemUpdateView, ProblemDeleteView, UserListView

urlpatterns = [
    # views.home and make PostListView another url
    path('posts', PostListView.as_view(), name='techmed-home'),  # posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('problem/', ProblemListView.as_view(),
         name='techmed-problems'),  # problems
    path('problem/<int:pk>/', ProblemDetailView.as_view(), name='problem-detail'),
    path('problem/new/', ProblemCreateView.as_view(), name='problem-create'),
    path('problem/<int:pk>/update/',
         ProblemUpdateView.as_view(), name='problem-update'),
    path('problem/<int:pk>/delete/',
         ProblemDeleteView.as_view(), name='problem-delete'),
    path('about/', views.about, name='techmed-about'),  # about
    path('index/', views.index, name='techmed-index'),
    path('register/', user_views.register, name='register'),
    path('user/<str:username>', UserListView.as_view(), name='user-posts'),

]
""" path('login/', user_views.login, name='login'), """
