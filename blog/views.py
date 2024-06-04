# Imports generic class from django
from django.views import generic
from django.shortcuts import render, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from cloudinary.forms import cl_init_js_callbacks
from .models import Post, Comment, Profile
from .forms import CommentForm, ProfileForm


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
    # Filtering results by published post only
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
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_view.html",
        {
            "post": post,
            "author": "Jhoan Trujillo",
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')

            return HttpResponseRedirect(reverse('post_view', args=[slug]))

        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('post_view', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_view', args=[slug]))


@login_required
def profile(request, user_id):
    # Query all profiles
    queryset = Profile.objects.all()
    # Get the data from the user asking the request
    profile = get_object_or_404(queryset, user=user_id)

    # Inherits value from comment_form in form.py
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES)
        if profile_form.is_valid():
            bio = profile_form.save(commit=True)
            bio.save()

    profile_form = ProfileForm()

    # Renders page and pass profile data
    return render(
            request,
            'blog/profile.html',
            {
                "profile": profile,
                "profile_form": profile_form,
            },
    )


def bio_edit(request, user_id, id):
    """
    View to edit user's bio
    """
    # Fetch the Profile instance associated with the current user
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == "POST":
        profile_form = ProfileForm(
            data=request.POST, files=request.FILES, instance=profile
            )
        if profile_form.is_valid() and profile.user == request.user:
            profile_form.save()
            messages.success(request, 'Bio Updated!')
            # Redirect to the profile page
            return HttpResponseRedirect(reverse(
                'users-profile', args=[request.user.id]
            ))
        else:
            messages.error(request, 'Error updating profile!')

    return HttpResponseRedirect(reverse(
        'users-profile', args=[request.user.id]
    ))
