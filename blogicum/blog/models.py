from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MainModel(models.Model):
    is_published = models.BooleanField(
        default=True, verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Добавлено',
    )

    class Meta:
        abstract = True


class Category(MainModel):
    title = models.CharField(
        max_length=256, unique=True,
        verbose_name='Заголовок',
    )
    description = models.TextField(verbose_name='Описание')
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True,
        verbose_name='Идентификатор',
        help_text='Идентификатор страницы для URL; '
        'разрешены символы латиницы, цифры, дефис и подчёркивание.',
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(MainModel):
    name = models.CharField(
        max_length=256, verbose_name='Название места',
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(MainModel):
    title = models.CharField(
        max_length=256, unique=True, verbose_name='Заголовок',
    )
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_posts',
        verbose_name='Автор публикации',

    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        related_name='loc_posts',
        blank=True,
        verbose_name='Местоположение',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='cat_posts',
        verbose_name='Категория',
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return self.title
