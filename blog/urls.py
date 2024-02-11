from . import views
from django.urls import path

# List of urls that will be used by the app
# this list is taken by the project level urls.py file
urlpatterns = [
	path('', views.IndexPage.as_view(), name='home'),
	path('blog/post_list', views.PostList.as_view(), name='blog_list'),
	path('blog/post_list/<slug:slug>/', views.post_view, name='post_view'),
]