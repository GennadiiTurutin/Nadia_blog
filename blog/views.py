from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView, 
    DeleteView
    )
from .models import Post


def art_design(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'blog/art_design.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/art_design.html'   # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'subtitle', 'content']

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
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html')


def inspiration(request):
    return render(request, 'blog/inspiration.html')

def lifestyle(request):
    context = {
    'posts': Post.objects.all()
    }
    return render(request, 'blog/lifestyle.html', context)

def search(request):
    query = request.GET.get('q')
    results = Post.objects.filter(Q(title__icontains=query) | 
        Q(subtitle__icontains=query) | 
        Q(content__icontains=query))

    context = {
    'posts': results
    }
    return render(request, 'blog/art_design.html', context)

