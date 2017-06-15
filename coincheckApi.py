#coincheck api

import json
import requests

print('what pair do you want to know?')
data = input('please enter:')
param = data
def exchangeRate(param):
    r = requests.get('https://coincheck.com/api/rate/' + param)
    rate = json.loads(r.text)['rate']

    print(rate)

exchangeRate(param)

# add comment for check!
