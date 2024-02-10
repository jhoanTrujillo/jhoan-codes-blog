from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

# Decorator needed to register a class instead of a plain model
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
	list_display = ('title', 'slug', 'status')
	search_fields = ['title']
	list_filter = ('status',)
	prepopulated_fields = {'slug': ('title',)}
	summernote_fields = ('content',)

# Models should be register below
admin.site.register(Comment)