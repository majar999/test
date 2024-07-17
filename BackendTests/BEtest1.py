
import requests #omogućava da šaljemo HTTP zahteve putem Python-a

# Definišite svoj API ključ
API_KEY = 'f440560e-66ae-4b58-a886-11bef057b80f'

# Endpoint URL-ovi
MAP_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map' #definisanje URL-ova za dobijanje ID kriptovaluta i konverziju
PRICE_CONVERSION_URL = 'https://pro-api.coinmarketcap.com/v1/tools/price-conversion'

# Funkcija za dobavljanje ID-ova kriptovaluta,headers=recnik-kljuc
def get_currency_ids():
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    response = requests.get(MAP_URL, headers=headers)
    data = response.json()

    currency_ids = {}
    for currency in data['data']:
        if currency['symbol'] in ['BTC', 'USDT', 'ETH']:
            currency_ids[currency['symbol']] = currency['id']
    
    return currency_ids

# Funkcija za konverziju valuta
def convert_to_boliviano(currency_id):
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    params = {
        'id': currency_id,
        'convert': 'BOB',
        'amount': 1  # Dodavanje amount parametra
    }
    response = requests.get(PRICE_CONVERSION_URL, headers=headers, params=params)
    data = response.json()

    # Ispis odgovora za debug
    print(data)

    if 'data' in data:
        return data['data']['quote']['BOB']['price']
    else:
        raise ValueError("Nema podataka za valutu")

# Glavna funkcija
def main():
    try:
        currency_ids = get_currency_ids()
        for symbol, currency_id in currency_ids.items():
            price_in_bob = convert_to_boliviano(currency_id)
            print(f"{symbol} price in BOB: {price_in_bob}")
    except Exception as e:
        print(f"Došlo je do greške: {e}")

if __name__ == "__main__":
    main()
