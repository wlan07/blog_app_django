from unicodedata import name
from django.urls import path
from users.views import UserRegisterView,EditProfileView




urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit-profile/',EditProfileView.as_view(),name="edit-profile")
]
