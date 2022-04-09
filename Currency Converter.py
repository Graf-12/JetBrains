import requests

cache = {}
my_currency = input()
url = f"http://www.floatrates.com/daily/{my_currency}.json"
req = requests.get(url)
json_text = req.json()

if my_currency != "usd":
    cache['usd'] = json_text['usd']['rate']
if my_currency != "eur":
    cache["eur"] = json_text['eur']["rate"]

while True:
    need_currency = input()
    if need_currency == '':
        break
    money = float(input())
    print("Checking the cache...")
    if need_currency in cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
        cache[need_currency] = json_text[need_currency]["rate"]
    print(f'You received {round(money * cache[need_currency], 2)} {need_currency.upper()}.')
    
