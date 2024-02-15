from . import views
from django.urls import path

# List of urls that will be used by the app
# this list is taken by the project level urls.py file
urlpatterns = [
    path('', views.IndexPage.as_view(), name='home'),
    path('blog/', views.PostList.as_view(), name='blog_list'),
    path('blog/post/<slug:slug>/', views.post_view, name='post_view'),
    path(
        'blog/post/<slug:slug>/edit_comment/<int:comment_id>',
        views.comment_edit, name='comment_edit'
    ),
    path(
        'blog/post/<slug:slug>/delete_comment/<int:comment_id>',
        views.comment_delete, name='comment_delete'
    ),
    path('profile/<int:user_id>', views.profile, name='users-profile'),
    path(
        'profile/<str:user_id>/bio_edit/<int:id>',
        views.bio_edit, name='bio_edit'
    ),
]
