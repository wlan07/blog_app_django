from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


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
                
