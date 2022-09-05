from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
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
    # Puts the list of blogs in order. Adding the - sign, displays newest
    # to oldest (as opposed to the default which is the opposite)
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # This method overrides default form valid method so that we
    # can add the author before the form is submitted.
    def form_valid(self, form):
        # Before the form is submitted get the name of the User
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About Title'})
