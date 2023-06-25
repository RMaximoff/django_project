from django.db import models
from django.urls import reverse
from django.utils import timezone
from pytils.translit import slugify


NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}, {self.description}, {self.created_at}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('created_at',)


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование')
    description = models.TextField(verbose_name='Описание')
    preview = models.ImageField(upload_to='img/', verbose_name='Превью', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')

    def __str__(self):
        return f'{self.name}, {self.description}, {self.category}, {self.price}, {self.created_at}, {self.updated_at}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ('created_at',)


class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    content = models.TextField(verbose_name='Сообщение')
    image = models.ImageField(upload_to='blog/', verbose_name='Превью', blank=False)
    create_date = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    is_published = models.BooleanField(verbose_name='Опубликовать', default=True)
    count_views = models.IntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.title)
            num = 1
            for blog in Blog.objects.all():
                if blog.slug == slug:
                    slug = f'{slug}_{num}'
                    num += 1
            self.slug = slug
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_published = False
        self.save()

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Пост блога'
        verbose_name_plural = 'Посты блога'
        ordering = ['create_date']
