from django.urls import reverse_lazy
from django.views import generic

from users.forms import UserSignUpForm

# Create your views here.


class UserRegisterView(generic.CreateView):
    form_class = UserSignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
