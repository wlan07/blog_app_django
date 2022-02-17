from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView
from myblogapp.models import Profile
from users.forms import UserProfileCreationForm, UserProfileUpdateForm, UserSignUpForm, UserUpdateForm, UserUpdatePasswordForm

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class EditUserView(generic.UpdateView):
    form_class = UserUpdateForm
    template_name = 'registration/update-user.html'
    success_url = reverse_lazy('home')

    def get_object(self) -> User:
        return self.request.user


class EditUserProfileView(generic.UpdateView):
    template_name = 'registration/update-profile.html'
    form_class = UserProfileUpdateForm
    success_url = reverse_lazy('home')

    def get_object(self) -> Profile:
        return self.request.user.profile


class CreateUserProfileView(generic.CreateView):
    template_name = 'registration/create-profile.html'
    form_class = UserProfileCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


"""
# CLASS BASED VIEW
class UserProfileView(generic.DetailView):
    template_name = 'registration/profile-view.html'

    def get_object(self) -> User:
        return self.request.user
        
        """


def UserProfileView(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'registration/profile-view.html', context)


class EditPasswordView(PasswordChangeView):
    form_class = UserUpdatePasswordForm
    template_name = 'registration/update-password.html'
    success_url = reverse_lazy('home')
