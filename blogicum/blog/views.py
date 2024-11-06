from django.shortcuts import render, get_object_or_404
from blog.utils import q_post, q_category


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
        q_category(),
        slug=category_slug,
    )
    post_list = (
        q_post()
        .filter(category__slug=category_slug)
        .order_by('-pub_date')[:10]
    )
    context = {'category': category, 'post_list': post_list}
    return render(request, template, context)
