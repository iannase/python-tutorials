import json
import requests
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

baseURL="https://api.coinmarketcap.com/v1/global/"
bitcoinURL="https://api.coinmarketcap.com/v1/ticker/bitcoin/"
litecoinURL="https://api.coinmarketcap.com/v1/ticker/litecoin/"
ethereumURL="https://api.coinmarketcap.com/v1/ticker/ethereum/"

# portfolio
myBitcoin = 0.18
myEthereum = 0.0
myLitecoin = 15.0

request = requests.get(baseURL)
data = request.json()
globalMarketCap = locale.format('%d',data['total_market_cap_usd'],True)

request = requests.get(bitcoinURL)
data = request.json()
bitcoinMarketCap = locale.format('%d',float(data[0]['market_cap_usd']),True)
bitcoinPrice = float(data[0]['price_usd'])
bitcoinPriceString = locale.format('%d',bitcoinPrice,True)

request = requests.get(litecoinURL)
data = request.json()
litecoinMarketCap = locale.format('%d',float(data[0]['market_cap_usd']),True)
litecoinPrice = float(data[0]['price_usd'])
litecoinPriceString = locale.format('%d',litecoinPrice,True)

request = requests.get(ethereumURL)
data = request.json()
ethereumMarketCap = locale.format('%d',float(data[0]['market_cap_usd']),True)
ethereumPrice = float(data[0]['price_usd'])
ethereumPriceString = locale.format('%d',ethereumPrice,True)

portfolioValue = myBitcoin * bitcoinPrice + myEthereum * ethereumPrice + myLitecoin * litecoinPrice
portfolioString = locale.format('%d',portfolioValue,True)

print()
print('Global:\t\t$'+globalMarketCap)
print()
print('Bitcoin:\t$'+bitcoinMarketCap+'\t$'+bitcoinPriceString)
print('Ethereum:\t$'+ethereumMarketCap+'\t\t$'+ethereumPriceString)
print('Litecoin:\t$'+litecoinMarketCap+'\t\t$'+litecoinPriceString)
print()
print('Portfolio:\t$'+portfolioString)
print()
