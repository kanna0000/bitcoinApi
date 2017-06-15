#coincheck api

import json
import requests

print('Which currency do you want to know a price calculated in JPY?')
data = input(":")

def conv(currency): #convert a currency to JPY
    pair = currency + "_jpy"
    r = requests.get('https://coincheck.com/api/rate/' + pair)
    rate = json.loads(r.text)['rate']
    return rate

print(conv(data) + "JPY")
