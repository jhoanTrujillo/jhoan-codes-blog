from django import forms
from django.forms import ModelForm
from .models import Comment, Profile
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


# This handles the change of the bio
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        image = CloudinaryFileField(
            options={"folder": "profile/"}
        )
        fields = ('image', 'bio')
