from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# This is the original Home view. Replaced by PostListView class view
# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


# This is the blog home view, created by adding variables
# the corresponding url path also had to be updated
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # Convention: <app name>/<model name>_<viewtype>.html
    context_object_name = 'posts'
    # Puts the list of blogs in order. Adding the - sign, displays newest to oldest (as opposed to the default which is the opposite)
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Title'})
