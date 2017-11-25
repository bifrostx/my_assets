# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_assets.settings')

import django
django.setup()
from my_coin.models import Token


def populate():

    tokens = {'btc': 1.974,
              'eth': 24.2696,
              'eos': 2635.9394,
              'qtum': 876.2514,
              'bch': 0.7337,
              'bcd': 19.74}

    for (name, amount) in tokens.items():
        add_token(name, amount)

    print("All finished!")


def add_token(name, amount):
    token = Token.objects.get_or_create(name=name)[0]
    token.amount = amount
    token.save()
    print("%f %s is added to your account." % (amount, name))


if __name__ == "__main__":
    print("Starting token population script...")
    populate()
    tokens = Token.objects.all()
