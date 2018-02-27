from django.db import models


# Категории
class Category(models.Model):

    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:

        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


# Продукт
class Product(models.Model):

    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория')
    name = models.CharField(max_length=200, db_index=True)