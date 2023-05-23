
"""Lightning.py: API to connect to BTCPayServer instance"""

__author__      = "Mariano Silva"
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
HTTP_OK = 200
timeout = 0

#new stuff BTCPayServer
config = configparser.ConfigParser()
config.sections()
config.read('env.cfg')
config.sections()
host =  config['CONFIG']['host']
api_key = config['CONFIG']['api_key']    # Account Setting --> Mariano User level API Key "Programatic Access"
store_id = config['CONFIG']['store_id']  # Transbit_DEMO Store

# Pedir una invoice nueva por la compra
def requestPayment(amount, currency):

    currency = 'CLP'
    amount = 1000
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
            'buyerName': "Lightning Chela Customer"
            }
    }

    url = f'{host}/api/v1/stores/{store_id}/invoices'

    # Create a basic invoice.
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        invoice = response.json()
        lninvoice = invoice['id']
        print("Invoice ID: ",lninvoice)
        
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
        paymentLink = invoice[1].get('paymentLink')
        
        print("\n Invoice ID: " + paymentLink)
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

    url = f'{host}/api/v1/stores/{store_id}/invoices/{paymentId}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}',
    }

    try:
        response = requests.get(url,  headers=headers)
        response.raise_for_status()
        invoice = response.json()
        print(invoice)
        status =  invoice['status']
        print ("Invoice Status: ",status)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
    
    paid = False

    if status == "Settled": 
        paid = True

    return paid
