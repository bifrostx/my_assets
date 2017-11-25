# -*- coding:utf-8 -*-
from decimal import *
from django.shortcuts import render
from .models import Token
from django.contrib.auth.decorators import login_required
from api import get_cny_rate, usd_rate_of_token


@login_required
def index(request):
    tokens = Token.objects.all()
    total = 0
    for token in tokens:
        price = Decimal(usd_rate_of_token(token.name) * get_cny_rate())
        balance = token.price * token.amount
        token.price = price.quantize(Decimal('.001'), rounding=ROUND_DOWN)
        token.balance = balance.quantize(Decimal('.001'), rounding=ROUND_DOWN)

        token.save()

        total = total + token.balance
    tokens = Token.objects.all()
    return render(request, 'my_coin/index.html', {"tokens": tokens, "total": total})

