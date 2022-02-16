from django.urls import path
from users.views import UserRegisterView,EditProfileView,EditPasswordView




urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit-profile/',EditProfileView.as_view(),name="edit-profile"),
    path('edit-password/',EditPasswordView.as_view(),name="edit-password")
]
