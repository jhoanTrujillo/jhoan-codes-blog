from django.shortcuts import render
from .models import Post
# Imports generic class from django
from django.views import generic


# Class based view 
class PostList(generic.ListView):
	# Import model to access data via generic view
	# Filtering results by published post only
	queryset = Post.objects.filter(status=0).order_by("created_on")
	template_name = 'blog/index.html'
	paginate_by = 6
