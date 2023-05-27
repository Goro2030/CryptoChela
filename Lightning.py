
"""Lightning.py: API to connect to BTCPayServer instance"""
"""this Python script connects to the BTCPayServer to create invoices, retrieve payment links, 
and check if an invoice has been paid. The currency type for the invoice can be defined through 
the requestPayment function, which also has additional versions for Satoshis, Brazilian Real, and US Dollars."""

# Authors of the script
__author__      = "Mariano Silva"
__credits__ = ["Eduardo Schoenknecht", "Felipe Borges Alves", "Paulo Eduardo Alves"]

# Required libraries
import json
import urllib3
import os
import random
import requests
from decimal import Decimal
from requests.auth import HTTPBasicAuth
import configparser

# HTTP_OK status code
HTTP_OK = 200
# Timeout value initialized to 0
timeout = 0

# BTCPayServer configuration details loaded from env.cfg file
config = configparser.ConfigParser()
				 
config.read('env.cfg')
				 
host =  config['CONFIG']['host']
api_key = config['CONFIG']['api_key']    # Account Setting --> Mariano User level API Key "Programatic Access"
store_id = config['CONFIG']['store_id']  # Transbit_DEMO Store

# Function to request a new invoice for a purchase
def requestPayment(amount, currency):

    # Setting currency to CLP
    currency = 'CLP'
    # Creating a random order ID
    order_id = 'Test-Birra-' + str(random.randint(0, 10000))
    
    # Headers for the POST request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}',
    }

    # Data for the POST request
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

    # Attempting to create an invoice and catching any exceptions
    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        invoice = response.json()
        lninvoice = invoice['id']
        print("Invoice ID: ",lninvoice)
        
    except requests.exceptions.RequestException as e:
        print("Error:", e)

														  

    # Setting headers for the GET request
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}',
    }

    url = f'{host}/api/v1/stores/{store_id}/invoices/{lninvoice}/payment-methods'
                
    # Attempting to get the payment link and catching any exceptions
    try:
        response = requests.get(url,  headers=headers)
        response.raise_for_status()
        invoice = response.json()
        print(invoice)			  
        paymentLink = invoice[1].get('paymentLink')
        
        print("\n Invoice ID: " + paymentLink)
    except requests.exceptions.RequestException as e:
        print("Error:", e)

    # Returns the invoice ID and the payment link
    return lninvoice, paymentLink

# Additional methods for requesting payment in different currencies
def requestPaymentSat(amount):
    return requestPayment(amount, "sat")

def requestPaymentBrl(amount):
    return requestPayment(amount, "CLP")

def requestPaymentUsdl(amount):
    return requestPayment(amount, "USD")

# Method to check if a given invoice is paid
def isInvoicePaid(paymentId):

    url = f'{host}/api/v1/stores/{store_id}/invoices/{paymentId}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Token {api_key}',
    }

    # Attempting to get the status of the invoice and catching any exceptions
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

    # Checking if the invoice status is "Settled"
    if status == "Settled": 
        paid = True

    # Returns True if the invoice is paid, False otherwise
    return paid
