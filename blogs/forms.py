from django import forms
from django.contrib.auth.forms import UserCreationForm


from .models import BlogPost, Comment

class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields =['title', 'text']
        labels = {'title':'新帖名称', 'text':'内容'}
        widgets = {'text':forms.Textarea(attrs={'cols':60})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        labels = {'text':''}
        widgets = {'text': forms.Textarea(attrs={'cols':60})}

