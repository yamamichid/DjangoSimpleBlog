from django import forms
from markdownx.fields import MarkdownxFormField


from .models import Comment


class CommentForm(forms.ModelForm):
    text = MarkdownxFormField()

    class Meta:
        model = Comment
        fields = ["author", "text"]
