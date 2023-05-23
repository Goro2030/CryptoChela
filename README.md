# Crypto-Chela: A Lightning Network Payment Activated Beer Faucet

Welcome to Crypto-Chela, an exciting project inspired by BitcoinBeer. Our project introduces a unique way of incorporating the emerging technology of Bitcoin and the Lightning Network into everyday life. We present to you a beer faucet that dispenses beer purchased with Bitcoin via Lightning Network payments.

The "Crypto-Chela" is being created by the "Asociacion Chilena de Criptotecnologias" (a.k.a. Asociacion Bitcoin Chile), to be deployed in Santiago, Chile.

## Introduction

The Crypto-Chela project enables users to select their preferred volume of beer through a touch display. This selection generates a QR code invoice which, once paid, activates a valve to dispense the beer. The beer continues to flow until a flow meter verifies that the paid-for amount has been poured. This integration of Bitcoin, Lightning Network, and everyday amenities heralds a new step towards a cashless society.

## Functionality 

The user interface for the Crypto-Chela beer faucet was created using Python's tkinter. The application runs on a Raspberry Pi, which is connected to a touch screen display, a valve, and a flow meter. These hardware elements work together seamlessly to deliver a user-friendly experience. 

Payments are managed through an external payment server running full nodes of Bitcoin and Lightning Network. This ensures a secure and efficient transaction process.

## Setup and Configuration

In order for the Crypto-Chela faucet to function correctly, it uses the BTCPayServer server infrastructure, that you need to have in place, or register into one existing BTCPayServer ( like transbit.cl ) and have a "Store". The BTCPayServer will handle the creation of invoices, payments, and store your sats.

To establish the connection with the BTCPayServer, you need to rename the file called "env.cfg1" to "env.cfg" and enter your Keys and URL for this connection. Detailed instructions on how to do this are provided in the `Lightning.py` file itself.

# Installing on-screen soft keyboard

To run this project, you also need to do

    git clone https://github.com/xlab/matchbox-keyboard.git 

You'll need libfakekey:

    sudo apt install libfakekey-dev libxft-dev

Then do the usual autotool jig of ./configure, make, make install. ( If building from SVN you'll need to run ./autogen.sh before this).


## Support Us

If you find this project exciting and want to support us, consider making a donation. Every little bit helps us in maintaining and improving Crypto-Chela. Here's how you can contribute:

- Lightning donations through LNURL: https://transbit.achicrip.org/plugins/lnbank/lnurl/4beb8516-70ce-477c-b4bb-ce4e66be2645 
- Lightning donations: https://achicrip.org/donaciones/
- Onchain Bitcoin: bc1pfnjxcr4tk7sfq2ws7zaql7x5fxs5pz6jlw0u2rn9nq52cn9ms6ksmfeaxl

## Demonstration Video

If you're curious to see Crypto-Chela in action, we've following the example created by our Brasilian friends at bitcoinBeer, whom recorded a demonstration video showcasing its functionality. You can watch the video [here](https://youtu.be/m26xDtktjr0).

## Get In Touch

For any queries, suggestions, or feedback, feel free to reach out to us. We appreciate your interest in Crypto-Chela and look forward to hearing from you. You can reach us to mariano@achicrip.org , or posting in GitHub.

Thank you for exploring our project!
mariano@achicrip.org
