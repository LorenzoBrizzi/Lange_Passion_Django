from django.views.generic import ListView, DetailView
from django.shortcuts import render
from .models import Post


def home(request):
    return render(request, 'home/home.html')

def contacts(request):
    return render(request, 'home/contacts.html', {'title': 'Contacts'})

def watches(request):
    return render(request, 'home/watches.html', {'title': 'Watches'})

def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/blog.html', context, {'title': 'Blog'})


class PostListView(ListView):
    model = Post
    template_name = 'home/blog.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
