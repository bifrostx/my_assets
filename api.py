import requests
import json


def get_coin_data(pair):
    r = requests.get("http://data.gate.io/api2/1/ticker/" + pair)
    d = json.loads(r.text)
    return d


def get_cny_rate():
    try:
        r = requests.get("https://api.fixer.io/latest?base=USD")
        d = json.loads(r.text)
        return d['rates']['CNY']
    except:
        return '6.6'


def usd_rate_of_token(token):
    pair = token + "_usdt"
    result = get_coin_data(pair)

    if result['result'] == "true":
        return result['last']
    else:
        return 0