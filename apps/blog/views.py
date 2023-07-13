from django.shortcuts import render
from .models import Blog, Category, Tag


def blog(request):
    blogs_list = Blog.objects.order_by('-id')
    # categories = Category.objects.all()
    # tags = Tag.objects.all()
    ctx = {
        'blogs': blogs_list,
        # 'categories': categories,
        # 'tags': tags
    }
    return render(request, 'blog/blog.html', ctx)


def blog_detail(request, slug):
    ctx = {

    }
    return render(request, 'blog/blog_details.html', ctx)
