from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        """
        Возвращаем посты которые фильтруем
        Через "__" обращаемся к Slug категории
        и получаем значение Slug
        """
        return Post.objects.filter(category__slug=self.kwargs.get("slug")).select_related('category')


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'


def home(request):
    return render(request, 'base.html')