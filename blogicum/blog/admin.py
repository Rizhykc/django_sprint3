from django.contrib import admin
from blog.models import Categories, Post, Location


admin.site.register(Categories)
admin.site.register(Post)
admin.site.register(Location)