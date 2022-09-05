from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    # path('', views.home, name='blog-home'), replaced by PostListView below.
    # .as_view converts it into a view
    path('', PostListView.as_view(), name='blog-home'),
    # into before pk indicates that the data must be an integer
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]
