from . import views
from django.urls import path

# List of urls that will be used by the app
# this list is taken by the project level urls.py file
urlpatterns = [
	path('', views.PostList.as_view(), name='post_list'),
	path('<slug:slug>/', views.post_view, name='post_view'),
]