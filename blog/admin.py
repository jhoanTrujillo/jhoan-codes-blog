from django.contrib import admin
from .models import Post

# Registering the model into the admin
# this give us CRUD capabilities with the post
admin.site.register(Post)