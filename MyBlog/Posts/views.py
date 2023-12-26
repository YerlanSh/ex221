from django.shortcuts import render

from .models import Post


# Create your views here.

def base(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})

