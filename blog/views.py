from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def blog_list(request):
    blogs = Blog.objects.filter(isPublished=True).order_by('-created_at')
    return render(request, 'blog/list.html', {'blogs': blogs})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk, isPublished=True)
    return render(request, 'blog/detail.html', {'blog': blog})
