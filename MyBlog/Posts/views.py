from django.shortcuts import render, redirect

from .forms import PostForm
from .models import Post


# Create your views here.
def newpost(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base')
        else:
            form = PostForm()
        return render(request, 'newpost.html', {'form': form})

def error_page(request):
    return render(request, 'error.html')

def base(request):
    posts = Post.objects.all()
    return render(request, 'posts_list.html', {'posts': posts})

