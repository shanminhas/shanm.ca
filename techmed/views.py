from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.
from .models import Post, Problem
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
#from django.utils.decorators import method_decorator


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'techmed/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'techmed/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 3


class UserListView(ListView):
    model = Post
    template_name = 'techmed/user_posts.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)


class PostDetailView(DetailView):
    model = Post
    #slug_field = 'slug'
    #slug_url_kwarg = 'slug'


class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = ('techmed.can_add_post')
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # just setting the form author to the currently logged in user
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/techmed'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'techmed/about.html', {'title': 'About'})


def index(request):
    return render(request, 'techmed/index.html', {'title': 'Index'})

# //////////////////////////
# //////////////////////////
# /////////////////////////


def problems(request):
    context = {
        'problems': Problem.objects.all()
    }
    return render(request, 'techmed/problems.html', context)


class ProblemListView(ListView):
    model = Problem
    template_name = 'techmed/problems.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'problems'
    paginate_by = 1


class ProblemDetailView(DetailView):
    model = Problem
    #slug_field = 'slug'
    #slug_url_kwarg = 'slug'


class ProblemCreateView(LoginRequiredMixin, CreateView):
    model = Problem
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ProblemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Problem
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class ProblemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Problem
    success_url = '/techmed'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
