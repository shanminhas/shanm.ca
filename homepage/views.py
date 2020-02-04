from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
# , CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Post
from django.contrib.auth.decorators import permission_required
#from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'homepage/home.html', {'title': 'Home'})


def about(request):
    return render(request, 'homepage/about.html', {'title': 'About'})


def projects(request):
    context = {
        'projects': Post.objects.all()
    }
    # figure out how to put {'title': 'Projects'} in homepage.views
    return render(request, 'homepage/projects.html', context)

    # return render(request, 'techmed/home.html', context)
# //////////////
# //////////////
# //////////////


class PostListView(ListView):
    model = Post
    template_name = 'homepage/projects.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    paginate_by = 1


class PostDetailView(DetailView):
    model = Post
    template_name = 'homepage/project_detail.html'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
