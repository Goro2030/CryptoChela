
"""Lightning.py: API to connect to BTCPayServer instance"""

__author__      = "Mariano Daniel Silva"
__credits__ = ["Eduardo Schoenknecht", "Felipe Borges Alves", "Paulo Eduardo Alves"]


import json
import urllib3
import os
import random
import requests
from decimal import Decimal
from requests.auth import HTTPBasicAuth
import configparser

# old shit
# BASE_URL = "https://md5hash.ddns.net:8080/LndPayRequest/v1"
HTTP_OK = 200
timeout = 0

#new stuff

config = configparser.ConfigParser()
config.sections()
config.read('RaspberryGUI/env.cfg')
config.sections()
host =  config['CONFIG']['host']
api_key = config['CONFIG']['api_key']    # Account Setting --> Mariano User level API Key "Programatic Access"
store_id = config['CONFIG']['store_id']  # Transbit_DEMO Store


# Pedir una invoice nueva por la compra
def requestPayment(amount, currency):

    currency = 'CLP'
    order_id = 'Test-Birra-' + str(random.randint(0, 1000))
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}',
    }

    data = {
        'storeId': store_id,
        'currency': currency,
        'amount': str(Decimal(amount)),
        'metadata' : { 
            'orderId': order_id,
            'itemDesc': "Birrita Test",
            'buyerName': "Lightning CHela Customer"
            }
    }

    url = f'{host}/api/v1/stores/{store_id}/invoices'

    # Create a basic invoice.
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        invoice = response.json()
        lninvoice = invoice['id']
        print(lninvoice)
        
    except requests.exceptions.RequestException as e:
        print("Error:", e)


    # Obtener la ln-invoice por la compra recien realizada

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}',
    }

    url = f'{host}/api/v1/stores/{store_id}/invoices/{lninvoice}/payment-methods'
                
    # Get the Invoice paymentLink
    try:
        response = requests.get(url,  headers=headers)
        response.raise_for_status()
        invoice = response.json()
        print(invoice)
        paymentLink = invoice[0].get('paymentLink')
        
        print("\n Invoice ID:" + paymentLink)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return lninvoice, paymentLink

def requestPaymentSat(amount):
    return requestPayment(amount, "sat")


def requestPaymentBrl(amount):
    return requestPayment(amount, "BRL")


def requestPaymentUsdl(amount):
    return requestPayment(amount, "USD")


def isInvoicePaid(paymentId):
    response = requests.get(BASE_URL + "/paymentstatus/" + paymentId, verify="lndpayrequest.crt")
    if response.status_code != HTTP_OK:
        print("Error checking payment status")
        exit()

    data = json.loads(response.text)
    return bool(data["paid"])
