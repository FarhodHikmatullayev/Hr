from django.db import models
from ckeditor.fields import RichTextField
from apps.blog.models import Base, Category
from django.db.models.signals import pre_save
from django.utils.text import slugify


class Company(models.Model):
    title = models.CharField(max_length=221)
    image = models.ImageField(upload_to='companies/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class JobCategory(models.Model):
    title = models.CharField(max_length=221)
    body = models.TextField()
    image = models.ImageField(upload_to='jobs/Category/', null=True, blank=True)

    def __str__(self):
        return self.title


class Location(models.Model):
    title = models.CharField(max_length=221)

    def __str__(self):
        return self.title


class Job(Base):
    NATURE = (
        (1, "Full-time"),
        (2, "Part-time"),
        (3, "Remote"),
    )
    GENDER = (
        (1, "Man"),
        (2, "Woman"),
    )
    title = models.CharField(max_length=221)
    slug = models.SlugField(null=True, blank=True, unique_for_date='created_date')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = RichTextField()
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    vacancy = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    salary = models.CharField(max_length=221)
    nature = models.IntegerField(choices=NATURE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    experience = models.IntegerField()
    gender = models.IntegerField(choices=GENDER)

    def __str__(self):
        return self.title


def job_pre_save(instance, sender, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
    return instance


pre_save.connect(job_pre_save, sender=Job)


class SubContent(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=221)
    body = RichTextField()

    def __str__(self):
        return f"{self.job.title}'s SubContent({self.id})"
