from django.urls import path
from .views import (PostListView, PostDetailView, CreateView)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog-detail'),
    path('post/create', CreateView.as_view(), name='blog-create'),
    path('about/', views.about, name='blog-about')
]