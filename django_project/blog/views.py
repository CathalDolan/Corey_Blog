from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# This isn't used as the home landing page is the Blog page
def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
