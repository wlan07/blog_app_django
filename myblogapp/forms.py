from django import forms
from .models import Category, Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category',
                  'body', 'snippet', 'header_image')
        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'author_field_id',
                'type': 'hidden'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'snippet': forms.Textarea(attrs={
                'class': 'form-control'
            }),

        }


class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
            })

        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'category', 'body', 'snippet')
        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'category': forms.Select(attrs={
                'class': 'form-control'
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control'
            }),
            'snippet': forms.Textarea(attrs={
                'class': 'form-control'
            }),

        }
