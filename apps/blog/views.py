from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Blog, Category, Tag, Comment
from .forms import CommentForm


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


def blog_detail(request, **kwargs):
    obj = get_object_or_404(Blog, created_date__day=kwargs['day'], created_date__month=kwargs['month'],
                            created_date__year=kwargs['year'], slug=kwargs['slug'])
    comments_blog = Comment.objects.filter(blog__in=obj.id, parent_comment__isnull=True)
    parent = request.GET.get('parent')
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            if parent:
                obj.parent_comment_id = int(parent)
            obj.save()
            messages.success(request, 'your comment was successfully accepted')
            return redirect('.')
        messages.info(request, 'Fields must not bee empty')

    ctx = {
        'blog': obj,
        'comments': comments_blog,
        'form': form,
    }
    return render(request, 'blog/blog_details.html', ctx)
