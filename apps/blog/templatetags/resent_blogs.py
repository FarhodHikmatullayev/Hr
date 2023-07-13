from django import template
from apps.blog.models import Tag, Category, Blog

register = template.Library()


@register.simple_tag()
def tags():
    tag = Tag.objects.all()
    return tag


@register.simple_tag()
def categories():
    category = Category.objects.all()
    return category


@register.simple_tag()
def resent_blog():
    r_b = Blog.objects.order_by('-id')[:3]
    return r_b
