from django.db import models
from django.utils import timezone


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



