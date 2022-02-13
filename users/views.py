from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from users.forms import UserSignUpForm,UserUpdateForm

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditProfileView(generic.UpdateView):
    form_class = UserUpdateForm
    template_name = 'registration/update.html'
    success_url = reverse_lazy('home')

    def get_object(self) -> User:
        return self.request.user

    