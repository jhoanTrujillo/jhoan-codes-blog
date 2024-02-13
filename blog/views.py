from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
# Imports generic class from django
from django.views import generic
from .forms import CommentForm


# Class based view 
class IndexPage(generic.ListView):
	"""
	Handles the index page data.
	queryset: returns a list of published post
	pagination: Total of 6, to keep the list small on index.
	template_name: refers to the index template in blog templates
	"""
	queryset = Post.objects.filter(status=1).order_by("-created_on")
	template_name = 'blog/index.html'
	paginate_by = 6
      
class PostList(generic.ListView):
	# Import model to access data via generic view
	# Filtering results by published post only
	queryset = Post.objects.filter(status=1).order_by("-created_on")
	template_name = 'blog/post_list.html'
	paginate_by = 9

def post_view(request, slug):
    """
    Display an individual :model:`blog.Post`.
    **Context**
    ``post``
        An instance of :model:`blog.Post`.
    **Template:**
    :template:`blog/post_detail.html`
    """
    # Access post model data. Only query published post
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    # Access the comment model data 
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approval=True).count()

	# Inherits value from comment_form in form.py
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
	
    comment_form = CommentForm()
	
    return render(
        request,
        "blog/post_view.html",
        {
			"post": post,
			"author": "Jhoan Trujillo",
			"comments" : comments,
			"comment_count" : comment_count,
			"comment_form": comment_form,
		},
    )

