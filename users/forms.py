from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from myblogapp.models import Profile


class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100,)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs["class"] = 'form-control'


class UserUpdateForm(UserChangeForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for i in self.fields:
            if not 'is' in i:
                self.fields[i].widget.attrs["class"] = 'form-control'
            else:
                self.fields[i].widget.attrs["class"] = 'form-check'


class UserProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'fb_url',
                  'instagram_url', 'linkedIn_url', 'github_url')

class UserProfileCreationForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'fb_url',
                  'instagram_url', 'linkedIn_url', 'github_url')


class UserUpdatePasswordForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs) -> None:
        super().__init__(user, *args, **kwargs)
        for i in self.fields:
            self.fields[i].widget.attrs["class"] = 'form-control'
