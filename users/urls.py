from django.urls import path
from users.views import EditUserProfileView, EditUserView, UserProfileView, UserRegisterView, EditPasswordView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit-user/', EditUserView.as_view(), name="edit-user"),
    path('edit-profile/', EditUserProfileView.as_view(), name="edit-profile"),
    path('edit-password/', EditPasswordView.as_view(), name="edit-password"),
    path('profile/', UserProfileView, name='profile-view')
]
