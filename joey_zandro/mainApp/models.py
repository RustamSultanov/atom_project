# coding: utf8
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import AbstractUser


# Категории
class Category(models.Model):

    parent = models.ForeignKey(u'self', verbose_name=u'Parent', blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    is_active = models.BooleanField(verbose_name=u'Доступна', default=True)
    order = models.IntegerField(verbose_name=u'Order', default=0)
    base_url = models.CharField(max_length=255, default='')

    class Meta:

        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Customer(AbstractUser):
    first_name = models.CharField(verbose_name=u'Имя покупателя', max_length=64)
    last_name = models.CharField(verbose_name=u'Фамилия покупателя', max_length=64)
    phone = models.CharField(verbose_name=u'Телефон клиента', max_length=64)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Comment(models.Model):
    text = models.CharField(max_length=1000)
    date = models.DateTimeField()
    author = models.ForeignKey(Customer, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    def __str__(self):
        return self.text


class Country(models.Model):

    title = models.CharField(verbose_name=u'Title', max_length=64)

    class Meta:
        verbose_name = u'Страна'
        verbose_name_plural = u'Страны'
        ordering = ['title']

    def __str__(self):
        return self.title


class Producer(models.Model):
    country = models.ForeignKey(Country,
                                verbose_name=u'Страна-производитель',
                                blank=True,
                                null=True,
                                on_delete=models.CASCADE)
    title = models.CharField(verbose_name=u'Имя производителя', max_length=64)
    slug = models.SlugField(max_length=100)

    class Meta:
        verbose_name = u'Производитель'
        verbose_name_plural = u'Производители'
        ordering = ['title']


class Color(models.Model):
    title = models.CharField(verbose_name=u'Название', max_length=64)
    slug = models.SlugField(max_length=80)

    class Meta:
        verbose_name = 'Цвет'
        verbose_name_plural = u'Цвета'
        ordering = ['title']


# Продукт
class Product(models.Model):

    category = models.ForeignKey(Category,
                                 related_name='products',
                                 verbose_name='Категория',
                                 on_delete=models.CASCADE)
    producer = models.ForeignKey(Producer, verbose_name=u'Производитель', blank=True, null=True, on_delete=models.CASCADE)
    color = models.ManyToManyField(Color, verbose_name=u'Цвет', blank=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    stock = models.PositiveIntegerField(verbose_name='В наличии')
    available = models.BooleanField(default=True, verbose_name='Доступен')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    comment = GenericRelation(Comment)

    class Meta:

        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUSES = (
        ('1', u'Ожидание'),     # в ожидании
        ('2', u'В обработке'),  # в обработке
        ('3', u'Отправлен'),     # отправлен
        ('4', u'Отменен'),   # отменен
        ('5', u'Закрыт'),   # завершен
        ('6', u'Возвращен'),     # возврат
        ('7', u'Доставлен'),  # доставка
    )

    name = models.CharField(verbose_name=u'Name', max_length=80)
    phone = models.CharField(verbose_name=u'Phone', max_length=16)
    ship_to = models.CharField(verbose_name=u'Адрес доставки', max_length=255)
    comment = models.TextField(verbose_name=u'Комментарий к доставке', blank=True, default=u'')
    total_price = models.FloatField(verbose_name=u'Итоговая стоимость')
    discount = models.FloatField(default=0.0)
    status = models.CharField(verbose_name=u'Статус', max_length=2, default=1, choices=STATUSES)
    registered = models.DateTimeField(verbose_name=u'Дата регистрации', auto_now_add=True)

    class Meta:
        verbose_name = u'Заказ'
        verbose_name_plural = u'Заказы'

    def __str__(self):
        return self.name


class OrderDetail(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.FloatField()

    class Meta:
        verbose_name = u'Детальный заказ'
        verbose_name_plural = u'Детальные заказы'

    def __str__(self):
        return self.product.title












































