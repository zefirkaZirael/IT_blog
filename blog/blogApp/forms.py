from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post            # Model to connect form
        fields = ['title', 'context'] # What info to show in form


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['context']

