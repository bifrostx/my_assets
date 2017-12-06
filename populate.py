# -*- coding: utf-8 -*-
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_assets.settings')

import django
django.setup()
from django.contrib.auth.models import User
from my_coin.models import Token


def populate():

    users = {'bifrost': {
             'email': 'bifrostx@gmail.com',
             'password': 'qwert12345'},
            }

    for (username, info) in users.items():
        create_user(username, info['email'], info['password'])

    user = User.objects.get(username='bifrost')

    tokens = {'btc': 1.974,
              'eth': 24.2696,
              'eos': 2635.9394,
              'qtum': 876.2514,
              'bch': 0.7337,
              'bcd': 19.74}

    for (name, amount) in tokens.items():
        add_token(user, name, amount)

    print("All finished!")


def add_token(user, token_name, amount):
    token = Token.objects.get_or_create(owner=user, name=token_name)[0]
    token.amount = amount
    token.save()
    print("%f %s is added to your account." % (amount, token_name))


def create_user(username, email, password):
    user = User.objects.get_or_create(username=username)[0]
    user.email = email
    user.set_password(password)
    user.save()
    print("user %s is created." % username)


if __name__ == "__main__":
    print("Starting token population script...")
    populate()
    tokens = Token.objects.all()
