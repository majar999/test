import requests

# Definišite svoj API ključ
API_KEY = 'f440560e-66ae-4b58-a886-11bef057b80f'

# Endpoint URL za dobavljanje informacija o kriptovalutama
INFO_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info'

# Funkcija za dobavljanje informacija o Ethereum-u
def get_ethereum_info():
    headers = {
        'X-CMC_PRO_API_KEY': API_KEY,
    }
    params = {
        'id': '1027'
    }
    response = requests.get(INFO_URL, headers=headers, params=params) #Šalje get zahtev CoinMarketCap API-ju sa definisanim zaglavljima i parametrima.
    data = response.json()
    return data['data']['1027']

# Funkcija za potvrdu atributa
def confirm_ethereum_info(eth_info):
    print(eth_info)  # Ispisivanje celog odgovora za debug

    try:
        assert eth_info['logo'] == "https://s2.coinmarketcap.com/static/img/coins/64x64/1027.png", "Logo URL ne odgovara"
        assert 'technical_doc' in eth_info['urls'] and eth_info['urls']['technical_doc'][0] == "https://github.com/ethereum/wiki/wiki/White-Paper", "Technical doc URL ne odgovara"
        assert eth_info['symbol'] == "ETH", "Simbol ne odgovara"
        assert eth_info['date_added'] == "2015-08-07T00:00:00.000Z", "Datum dodavanja ne odgovara"
        assert eth_info['platform'] is None, "Platforma nije null"
        
        print("Tagovi: ", eth_info['tags'])  # Ispisivanje svih tagova za debug
        assert "mineable" in eth_info['tags'], "Mineable tag nije prisutan"
        
        print("Sve potvrde su uspešno prošle")
    except AssertionError as e:
        print(f"Došlo je do greške: {e}")

# Glavna funkcija
def main():
    try:
        eth_info = get_ethereum_info()
        confirm_ethereum_info(eth_info)
    except Exception as e:
        print(f"Došlo je do greške: {e}")

if __name__ == "__main__":
    main()
