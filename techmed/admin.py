from django.contrib import admin

# Register your models here.
from .models import Post, Problem

admin.site.register(Post)
admin.site.register(Problem)
