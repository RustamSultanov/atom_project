from decimal import Decimal
from django.conf import settings
from mainApp.models import Product


class Cart(object):

    def __init__(self, request):
        # инициализация корзины
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
