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
