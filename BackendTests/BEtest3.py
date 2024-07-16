
import requests

# Definišite svoj API ključ
API_KEY = 'f440560e-66ae-4b58-a886-11bef057b80f'

# Endpoint URL za dobavljanje informacija o kriptovalutama
INFO_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

# Funkcija za dobavljanje informacija o prvih 10 kriptovaluta
def get_top_10_currencies():
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    params = {
        'id': ','.join(map(str, range(1, 11)))  # ID-ovi od 1 do 10
    }
    response = requests.get(INFO_URL, headers=headers, params=params)
    data = response.json()
    return data['data']

# Funkcija za proveru "mineable" taga i ispisivanje rezultata
def check_mineable_tags(currencies):
    mineable_currencies = []
    for currency_id, currency_info in currencies.items():
        if "mineable" in currency_info['tags']:
            mineable_currencies.append(currency_info['name'])
    print("Kriptovalute sa 'mineable' tagom:", mineable_currencies)

# Glavna funkcija
def main():
    try:
        top_10_currencies = get_top_10_currencies()
        check_mineable_tags(top_10_currencies)
    except Exception as e:
        print(f"Došlo je do greške: {e}")

if __name__ == "__main__":
    main()
