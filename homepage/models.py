from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='homepage_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    appname = models.CharField(max_length=200, default="")
    # figure out how to link to a specific app regardless of the homepage name (either 127.0.0.1:8000/ or shantanuminhas.com/ )
    #url = models.URLField(max_length=200, default='')

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs)
