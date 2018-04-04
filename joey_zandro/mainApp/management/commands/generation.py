from django.core.management.base import BaseCommand, CommandError
from mainApp.models import *
from random import randint, choice

BATCH_SIZE = 5000
DEFAULT_AMOUNT = 100000
CATEGORIES_AMOUNT = 1000
COUNTRIES_AMOUNT = 100
MIN_PRICE = 1000
MAX_PRICE = 100000


def benchmark(func):
    """ декоратор, возвращающий время работы функции """
    import time

    def wrapper(*args, **kwargs):
        t = time.clock()
        res = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return res
    return wrapper


class Command(BaseCommand):
    help = 'Generates the 100000 objects of all models'

    def handle(self, *args, **options):

        countries = [Country(title=str(_) + 'Country') for _ in range(COUNTRIES_AMOUNT)]
        Country.objects.bulk_create(countries, batch_size=BATCH_SIZE)
        country_ids = [Country.objects.all()[_].id for _ in range(COUNTRIES_AMOUNT)]

        categories = [Category(name=str(_) + 'Category') for _ in range(1000)]
        Category.objects.bulk_create(categories, batch_size=BATCH_SIZE)
        category_ids = [Category.objects.all()[_].id for _ in range(1000)]

        colors = [Color(title='Color' + str(_)) for _ in range(DEFAULT_AMOUNT)]
        Color.objects.bulk_create(colors, batch_size=BATCH_SIZE)

        orders = [Order(
            name='Order' + str(_),
            phone='Phone' + str(_),
            ship_to='Address' + str(_),
            total_price=randint(1000, 100000)
        ) for _ in range(DEFAULT_AMOUNT)]
        Order.objects.bulk_create(orders, batch_size=BATCH_SIZE)

        products = [Product(
            category_id=choice(category_ids),
            name='Product' + str(_),
            price=randint(MIN_PRICE, MAX_PRICE),
            stock=randint(1, 100)
        ) for _ in range(DEFAULT_AMOUNT)]
        Product.objects.bulk_create(products, batch_size=BATCH_SIZE)

        producers = [Producer(
            country_id=choice(country_ids),
            title='Producer' + str(_)
        ) for _ in range(DEFAULT_AMOUNT)]
        Producer.objects.bulk_create(producers, batch_size=BATCH_SIZE)
        producer_ids = [Producer.objects.all()[_].id for _ in range(DEFAULT_AMOUNT)]

        orders_details = [OrderDetail(
            order_id=choice(orders),
            quantity=randint(1, 50),
            price=randint(1000, 100000)
        ) for _ in range(DEFAULT_AMOUNT)]
        OrderDetail.objects.bulk_create(orders_details, batch_size=BATCH_SIZE)
        





