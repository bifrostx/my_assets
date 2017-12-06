# -*- coding:utf-8 -*-
from decimal import *
from django.shortcuts import render
from .models import Token
from .forms import TokenForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from api import get_cny_rate, usd_rate_of_token, money_format


@login_required
def index(request):
    owner = User.objects.get(username=request.user)
    tokens = Token.objects.filter(owner=owner)
    total = 0
    cny_rate = get_cny_rate()
    for token in tokens:
        price = usd_rate_of_token(token.name) * cny_rate
        balance = token.price * token.amount
        token.price = money_format(price)
        token.balance = money_format(balance)

        token.save()

    coins = Token.objects.filter(owner=owner)

    for coin in coins:
        total += coin.balance

    if request.method == 'POST':
        new = Token.objects.create(owner=owner)
        form = TokenForm(request.POST, instance=new)
        if form.is_valid():
            form.save(commit=True)
            print(form.as_p())
            print("submitted")
        else:
            print(form.errors)
            print("error")

    return render(request, 'my_coin/index.html', {"tokens": coins, "total": total})


