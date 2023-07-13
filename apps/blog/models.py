from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Base(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True


class Category(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Blog(Base):
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True, unique_for_date='created_date')
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ImageField(upload_to='blogs/')
    description = RichTextField()

    def __str__(self):
        return self.title


def blog_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    return instance


pre_save.connect(blog_pre_save, sender=Blog)


class Comment(Base):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    name = models.CharField(max_length=221)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(upload_to='blogs/comment/', null=True, blank=True)
    message = models.TextField()
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    top_level_comment_id = models.IntegerField(null=True, blank=True)

    @property
    def children(self):
        return Comment.objects.filter(top_level_comment_id=self.top_level_comment_id).exclude(
            id=self.top_level_comment_id)

    def __str__(self):
        return f"{self.blog}'s comment ({self.id})"


def top_id(instance, sender, created, *args, **kwargs):
    if created:
        parent = instance
        while parent.parent_comment:
            parent = parent.parent_comment
        instance.top_level_comment_id = parent.id
        instance.save()
    return instance


post_save.connect(top_id, sender=Comment)
