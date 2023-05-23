
"""Rates.py: Get BTC prices to different currencies """

__author__      = "Mariano Silva"
__credits__ = ["Eduardo Schoenknecht", "Felipe Borges Alves", "Paulo Eduardo Alves"]

import requests

def get_rate_USD():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        r.raise_for_status()
        return int(r.json()['bpi']['USD']['rate_float'])
    except requests.RequestException as e:
        print(f"Error retrieving USD rate: {e}")
        return None
    except KeyError as e:
        print(f"Unexpected response format: {e}")
        return None

def get_rate_BRL():
    try:
        r = requests.get('https://www.buda.com/api/v2/markets/btc-clp/ticker.json')
        r.raise_for_status()
        return int(float(r.json()['ticker']['last_price'][0]))
    except requests.RequestException as e:
        print(f"Error retrieving BRL rate: {e}")
        return None
    except KeyError as e:
        print(f"Unexpected response format: {e}")
        return None
