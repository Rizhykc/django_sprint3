from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class MainModel(models.Model):
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True, verbose_name='Добавлено')

    class Meta:
        abstract = True


class Categories(MainModel):
    title = models.CharField(max_length=256, unique=True, verbose_name='Название')
    description = models.TextField()
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(MainModel):
    name = models.CharField(max_length=256, unique=True, blank=False, verbose_name='Имя')

    class Meta:
        db_table = 'Location'
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class Post(MainModel):
    title = models.CharField(max_length=256, unique=True, verbose_name='')
    text = models.TextField(verbose_name='Текст')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Время и дата размещения')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'

    )
    location = models.ForeignKey(
        to=Location,
        on_delete=models.SET_NULL,
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        to=Categories,
        on_delete=models.SET_NULL,
        verbose_name='Категория'
    )
    is_published = models.BooleanField(default=True)
    

    class Meta:
        db_table = 'Post'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
    
    def __str__(self):
        return self.title
