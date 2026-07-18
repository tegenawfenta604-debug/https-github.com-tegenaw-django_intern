from django.db.models import F
from django.shortcuts import render, get_object_or_404
from .models import Blog


def blog_list(request):
    """Display all published blog posts, newest first."""
    blogs = Blog.objects.filter(is_published=True)
    return render(request, "blog/list.html", {"blogs": blogs})


def blog_detail(request, slug):
    """Display a single published post (by slug) and increment its view counter."""
    blog = get_object_or_404(Blog, slug=slug, is_published=True)
    Blog.objects.filter(pk=blog.pk).update(number_of_views=F("number_of_views") + 1)
    return render(request, "blog/detail.html", {"blog": blog})


def blog_detail_pk(request, pk):
    """Backward-compatible detail view keyed by primary key."""
    blog = get_object_or_404(Blog, pk=pk, is_published=True)
    Blog.objects.filter(pk=blog.pk).update(number_of_views=F("number_of_views") + 1)
    return render(request, "blog/detail.html", {"blog": blog})
