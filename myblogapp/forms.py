from django import forms
from .models import Category, Post


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'author': forms.Select(attrs={
                'class': 'form-control'
            }),
            'body': forms.Textarea(attrs={
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
        fields = ('title', 'category', 'body')
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


        }
