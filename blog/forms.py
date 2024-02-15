from .models import Comment, Profile
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# This handles the change of the bio
class BioForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio',)
