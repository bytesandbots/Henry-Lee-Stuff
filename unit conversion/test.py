import requests
BASE_URL = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_wjkuyywumTDkUReNACdX5hWJTFfjaZSoQxEAM16E&currencies={}&base_currency={}"


def convert(value:float, target:str, base = "USD"):
    r = requests.get(BASE_URL.format(target, base))
    rate = r.json()['data'][target]
    return value*rate




print(convert(23, "USD", "CAD"))    