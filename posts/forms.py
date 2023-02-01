from django import forms
from posts.models import Comment, Post


class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "text")

class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")