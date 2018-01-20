# Ian Annase
# 1/7/2018

import math
import requests
import json
import locale
from prettytable import PrettyTable

# number formatter
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# URLs
globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

# get global market cap
request = requests.get(globalURL)
data = request.json()
globalMarketCap = float(data['total_market_cap_usd'])

# initialize the PrettyTable
t = PrettyTable(['Name', 'Ticker', '% of total global cap', 'Current', '7.7T (Gold)', '36.8T (Narrow Money)', '73T (World Stock Markets)', '90.4T (Broad Money)', '217T (Real Estate)', '544T (Derivatives)'])

# get ticker data
request = requests.get(tickerURL)
data = request.json()
for x in data:

    # retrieve data
    name = x['name']
    ticker = x['symbol']
    percentageOfGlobalCap = float(x['market_cap_usd']) / float(globalMarketCap)
    currentPrice = round(float(x['price_usd']),2)
    availableSupply = float(x['total_supply'])

    # calculate future values
    trillion7price = round(7700000000000 * percentageOfGlobalCap / availableSupply,2)
    trillion36price = round(36800000000000 * percentageOfGlobalCap / availableSupply,2)
    trillion73price = round(73000000000000 * percentageOfGlobalCap / availableSupply,2)
    trillion90price = round(90400000000000 * percentageOfGlobalCap / availableSupply,2)
    trillion217price = round(217000000000000 * percentageOfGlobalCap / availableSupply,2)
    trillion544price = round(544000000000000 * percentageOfGlobalCap / availableSupply,2)

    # format strings
    percentageOfGlobalCapString = str(round(percentageOfGlobalCap*100,2))+"%"
    currentPriceString = '$'+str(currentPrice)
    trillion7priceString = '$'+locale.format('%.2f',trillion7price,True)
    trillion36priceString = '$'+locale.format('%.2f',trillion36price,True)
    trillion73priceString = '$'+locale.format('%.2f',trillion73price,True)
    trillion90priceString = '$'+locale.format('%.2f',trillion90price,True)
    trillion217priceString = '$'+locale.format('%.2f',trillion217price,True)
    trillion544priceString = '$'+locale.format('%.2f',trillion544price,True)

    # append to the table
    t.add_row([name,ticker,percentageOfGlobalCapString,currentPriceString,trillion7priceString,trillion36priceString,trillion73priceString,trillion90priceString,trillion217priceString,trillion544priceString])

# print out the table
print(t)
