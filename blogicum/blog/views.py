from django.shortcuts import render, get_list_or_404
from blog.models import Categories, Post 

def index(request):

    template = 'blog/index.html'
    context = {
        'title': 'Лента записей',
        'content': 'Лента записей',
        'posts': ' ',
    }

    return render(request, template, context)


def post_detail(request, id):

    template = 'blog/detail.html'
    post = get_list_or_404(
        Post.post_objecst,
        id=id
    )
    context = {'posts': post}
    return render(request, template, context)


def category_posts(request, category_slug):

    template = 'blog/category.html'
    context = {
        'title': 'Публикации в категории personal',
        'content': 'Публикации в категории personal',
        'category': category_slug
    }
    return render(request, template, context)
