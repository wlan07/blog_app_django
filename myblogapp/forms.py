from django import forms
from .models import Catergory, Post


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
        model = Catergory
        fields = '__all__'
        widgets = {

            'name': forms.TextInput(attrs={
                'class': 'form-control',
            })

        }


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')
        widgets = {

            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),

            'body': forms.Textarea(attrs={
                'class': 'form-control'
            }),


        }
