from django.shortcuts import render


posts = [
    {
        'author': 'Lorenzo Brizzi',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Sara Pedrotti',
        'title': 'New Post',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]


def home(request):
    return render(request, 'home/home.html')

def contacts(request):
    return render(request, 'home/contacts.html', {'title': 'Contacts'})

def watches(request):
    return render(request, 'home/watches.html', {'title': 'Watches'})

def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/blog.html', context, {'title': 'Blog'})

