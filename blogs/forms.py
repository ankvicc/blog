from django import forms
from .models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {
            'title': 'Заголовок',
            'text': 'Текст записи',
        }
