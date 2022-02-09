from django.urls import path
from .views import AddCategoryView, FiltredBlogView, UpdatePostView, homeView, BlogDetailView, AddPostView, DeletePostView

urlpatterns = [
    path('', homeView.as_view(), name="home"),
    path('filter/<str:name>', FiltredBlogView, name="filter"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name="detail-post"),
    path('blog/add/post/', AddPostView.as_view(), name="add-post"),
    path('blog/add/category/', AddCategoryView.as_view(), name="add-category"),
    path('blog/edit/post/<int:pk>', UpdatePostView.as_view(), name="update-post"),
    path('blog/delete/post/<int:pk>', DeletePostView.as_view(), name="delete-post")
]
