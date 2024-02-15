from django.contrib import admin
from .models import Post, Comment, Profile
from django_summernote.admin import SummernoteModelAdmin

# Decorator needed to register a class based on a model.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
	# Adds search and filtering functionality to post list
	list_display = ('title', 'slug', 'status', 'created_on', 'author')
	search_fields = ['title', 'content']
	list_filter = ('status', 'created_on')
	# Prepopulates slug with the title of the post
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = ('content',)

# Models should be register below
admin.site.register(Comment)
admin.site.register(Profile)