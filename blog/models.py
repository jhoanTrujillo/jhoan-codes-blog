from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Allows access to cloudinary on app
from cloudinary.models import CloudinaryField


# Options to show text draft or published
# in the blog creation area of the admin
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    # Django default max_length for slugs is 50
    # a slightly higher value was given for flexibility purposes
    slug = models.SlugField(max_length=70, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    # max_length set to 320 to limit the number of lines
    # that can be display, allowing for 80 chars per line
    # blank allows for empty value submittion
    excerpt = models.TextField(max_length=500, blank=True)
    content = models.TextField()
    # auto_now_add will add the creation date of the post to the database
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)

    # Changes the name format in the admin
    def __str__(self):
        return f"{self.title} | Author: {self.author}"

    # Orders the post by date of creation
    class meta:
        ordering = ["-created_on"]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approval = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    # Changes the name format in the admin
    def __str__(self):
        return f"{self.body}"

    class meta:
        ordering = ["created_on"]


# Profile model edited from https://dev.to/earthcomfy/django-user-profile-3hik
# The code was slightly edited for my personal needs and the user of cloudinary
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image', default='placeholder')
    bio = models.TextField(default="bio")

    # Signals code coming from https://dev.to/earthcomfy/django-user-profile-3hik
    # When user is created, then a profile is created as well.
    def __str__(self):
        return f'{self.user.username} Profile'
