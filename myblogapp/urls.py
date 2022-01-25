from django.urls import path
from .views import UpdatePostView, homeView,BlogDetailView,AddPostView,DeletePostView

urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="detail"),
    path('blog/add/',AddPostView.as_view(),name="add"),
    path('blog/edit/<int:pk>',UpdatePostView.as_view(),name="update"),
    path('blog/delete/<int:pk>',DeletePostView.as_view(),name="delete")
]


