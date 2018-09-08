from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Habib',
        'title': 'It\'s a title',
        'content': 'This is first content',
        'created_at': 'September 4'
    },
    {
        'author': 'Jui',
        'title': 'It\'s a title 2',
        'content': 'This is second content',
        'created_at': 'September 5'
    }
]


def home(request):
    context = {
        'title': 'Home',
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    context = {'title': 'About'}
    return render(request, 'blog/about.html', context)
