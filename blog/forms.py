from django import forms
from django.forms import ModelForm
from .models import Comment, Profile

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# This handles the change of the bio
class BioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
