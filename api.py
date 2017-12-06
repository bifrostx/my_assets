import requests
import json
from decimal import *


def get_coin_data(pair):
    r = requests.get("http://data.gate.io/api2/1/ticker/" + pair)
    d = json.loads(r.text)
    print("Succeeded in getting Coin data.")
    return d


def get_cny_rate():
    try:
        r = requests.get("https://api.fixer.io/latest?base=USD")
        d = json.loads(r.text)
        print("Succeeded in getting CNY rates.")
        return d['rates']['CNY']
    except:
        print("Get CNY rates failed, set rate to 6.6.")
        return 6.6


def usd_rate_of_token(token):
    pair = token + "_usdt"
    result = get_coin_data(pair)

    if result['result'] == "true":
        print("Succeeded in getting usd price of %s." % token)
        return result['last']
    else:
        print("Failed to get usd price of %s." % token)
        return 0


def money_format(value):
    return Decimal(value).quantize(Decimal('0.0'))