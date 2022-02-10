from turtle import pos
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddCategoryForm, AddPostForm, UpdatePostForm
from .models import Category, Post


def unslugify(s: str) -> str:
    return s.replace('-', ' ')

# Home
class HomeView(ListView):
    model = Post
    template_name = 'myblogapp/home.html'
    context_object_name = 'lastest_posts_list'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cat_menu'] = Category.objects.all()
        return context

def PostLikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get("post_id"))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail-post',args=[str(pk)]))


def PostUnlikeView(request,pk):
    post = get_object_or_404(Post,id=request.POST.get("post_id"))
    post.likes.remove(request.user)
    return HttpResponseRedirect(reverse('detail-post',args=[str(pk)]))


def FiltredBlogView(request, name):
    unslugified_cat_name = unslugify(name)
    filtred_list = Post.objects.filter(category__name__iexact=unslugified_cat_name)
    context = {
        'filtred_list': filtred_list,
        'category_name': unslugified_cat_name
    }
    return render(request, 'myblogapp/filtred_posts.html', context)


"""class BlogFiltredView(ListView):
    model = Post
    template_name = 'myblogapp/filtred_posts.html'
    context_object_name = 'filtred_posts_list'
    ordering = ['-id']

    def get_queryset(self):
        return self.model.objects.filter(category=1)"""


# Posts

class BlogDetailView(DetailView):
    model = Post
    template_name = 'myblogapp/details_post.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'myblogapp/add_post.html'
    form_class = AddPostForm

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


# Categories


class AddCategoryView(CreateView):
    model = Category
    template_name = 'myblogapp/add_category.html'
    form_class = AddCategoryForm

    def get_success_url(self):
        return reverse('home')
