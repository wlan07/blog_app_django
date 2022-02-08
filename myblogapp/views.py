from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import AddCategoryForm, AddPostForm, UpdatePostForm
from .models import Post


class homeView(ListView):
    model = Post
    template_name = 'myblogapp/home.html'
    context_object_name = 'lastest_posts_list'
    ordering = ['-id']


class BlogDetailView(DetailView):
    model = Post
    template_name = 'myblogapp/details_post.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'myblogapp/add_post.html'
    form_class = AddPostForm

    def get_success_url(self):
        return reverse('home')


class AddCategoryView(CreateView):
    model = Post
    template_name = 'myblogapp/add_category.html'
    form_class = AddCategoryForm

    def get_success_url(self):
        return reverse('home')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'myblogapp/update_post.html'
    form_class = UpdatePostForm

    def get_success_url(self):
        return reverse('home')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'myblogapp/delete_post.html'
    success_url = reverse_lazy('home')

    """def get_success_url(self):
        return reverse('home')"""
