from blog.models import Post
from django.utils import timezone


def q_post():

    time_now = timezone.now()
    query_set = (
        Post.objects.select_related(
            'category',
            'location',
            'author',
        ).filter(
            pub_date__lte=time_now,
            is_published=True,
            category__is_published=True,
        )
    )
    return query_set
