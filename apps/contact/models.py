from django.db import models
from apps.blog.models import Base


class Contact(Base):
    name = models.CharField(max_length=221)
    email = models.EmailField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}'s message"

