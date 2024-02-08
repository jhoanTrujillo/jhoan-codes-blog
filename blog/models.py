from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
	title = models.CharField(max_length=200, unique=True)
	# Django default max_length for slugs is 50
	# a slightly higher value was given for flexibility purposes
	slug = models.SlugField(max_length=70, unique=True)
	author = models.ForeignKey(
		User, on_delete=models.CASCADE, related_name="blog_posts"
	)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)