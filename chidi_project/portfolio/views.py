from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    posts = Blog.objects.order_by('-id')[:4]
    context = {
        'posts':posts,
    }
    return render(request, 'index.html', context)

def gallery(request):
    return render(request, 'gallery.html')

def blog(request):
    posts = Blog.objects.order_by('-id')
    context = {
        'posts':posts,
    }
    return render(request, 'blog.html', context)

def blogpage(request, slug):
    blogpost = get_object_or_404(Blog, slug=slug)
    
    context = {
        'blogpost': blogpost
    }
    return render(request, 'blog-details.html', context )