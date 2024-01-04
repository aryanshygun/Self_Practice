import requests

def get_top_crypto_prices(limit=10):
    try:
        # Make a GET request to the CoinCap API for the top cryptocurrencies
        response = requests.get(f'https://api.coincap.io/v2/assets?limit={limit}')
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            
            # Extract and return a dictionary of cryptocurrency names and their prices
            crypto_prices = {crypto['name']: crypto['priceUsd'] for crypto in data['data']}
            return crypto_prices
        else:
            print(f"Error: Unable to fetch cryptocurrency prices. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Get the prices of the top 10 cryptocurrencies
top_crypto_prices = get_top_crypto_prices()

# Display the result
if top_crypto_prices is not None:
    print("Top 10 Cryptocurrency Prices:")
    for crypto, price in top_crypto_prices.items():
        print(f"{crypto}: ${price}")
