# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


class PostList(ListView):
    model = Post
    template_name = 'post_list.html'
    context_object_name = 'post_list'


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post_detail.html'  # название шаблона будет post_detail.html
    context_object_name = 'post_detail'
