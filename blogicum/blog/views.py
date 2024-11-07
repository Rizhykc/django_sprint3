from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.utils import q_post
from blog.models import Category


def index(request):

    template = 'blog/index.html'
    post_list = q_post().order_by('-pub_date')[:5]
    context = {'post_list': post_list}
    return render(request, template, context)


def post_detail(request, id):

    template = 'blog/detail.html'
    post_list = get_object_or_404(
        q_post(),
        pk=id,
    )
    context = {'post': post_list}
    return render(request, template, context)


def category_posts(request, category_slug):

    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = category.cat_posts.filter(
        pub_data_lte=timezone.now(),
        is_published=True,
        category__is_published=True,
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
