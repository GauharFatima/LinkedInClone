from django.contrib import admin
from PostsApp.models import Post, Comments, Like


# Register your models here.
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Like)
