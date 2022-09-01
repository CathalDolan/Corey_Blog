from django.shortcuts import render
from django.http import HttpResponse

# Dummy list of dictionaries
posts = [
    {
        'author': 'CFD',
        'title': 'Blog Post 1',
        'content': 'Content for blog post 1',
        'date_posted': 'September 1st 2022',
    },
    {
        'author': 'John Doe',
        'title': 'Blog Post 2',
        'content': 'Content for blog post 2',
        'date_posted': 'September 2nd 2022',
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Title'})
