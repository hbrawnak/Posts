from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post



def home(request):

    posts = Post.objects.all()

    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

#ListView for home page
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts' #Refer to 'posts' in home context.
    ordering = ['-created_at'] #orderBy created_at DESC

class PostDetailView(DetailView):
    model = Post



def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)
