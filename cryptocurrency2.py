# Ian Annase
# 1/7/2018

import math
import requests
import json
import locale
from prettytable import PrettyTable
import xlsxwriter

# number formatter
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# URLs
globalURL = "https://api.coinmarketcap.com/v1/global/"
tickerURL = "https://api.coinmarketcap.com/v1/ticker/"

# excel
# open excel workbooks
cryptoWorkbook = xlsxwriter.Workbook('cryptocurrency.xlsx')

# add a sheet
cryptoSheet = cryptoWorkbook.add_worksheet()

# add headers
bold = cryptoWorkbook.add_format({'bold': True})
cryptoSheet.write('A1',"Name",bold)
cryptoSheet.write('B1',"Ticker",bold)
cryptoSheet.write('C1',"% of total global cap",bold)
cryptoSheet.write('D1',"Current",bold)
cryptoSheet.write('E1',"7.7T (Gold)",bold)
cryptoSheet.write('F1',"36.8T (Narrow Money)",bold)
cryptoSheet.write('G1',"73T (World Stock Markets)",bold)
cryptoSheet.write('H1',"90.4T (Broad Money)",bold)
cryptoSheet.write('I1',"217T (Real Estate)",bold)
cryptoSheet.write('J1',"544T (Derivatives)",bold)

# get global market cap
request = requests.get(globalURL)
data = request.json()
globalMarketCap = float(data['total_market_cap_usd'])

# initialize the PrettyTable
t = PrettyTable(['Name', 'Ticker', '% of total global cap', 'Current', '7.7T (Gold)', '36.8T (Narrow Money)', '73T (World Stock Markets)', '90.4T (Broad Money)', '217T (Real Estate)', '544T (Derivatives)'])

# get ticker data
request = requests.get(tickerURL)
data = request.json()
z=1
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
    print(name + " (" + ticker + "): " + trillion90priceString)

    # excel
    cryptoSheet.write(z,0,name)
    cryptoSheet.write(z,1,ticker)
    cryptoSheet.write(z,2,percentageOfGlobalCapString)
    cryptoSheet.write(z,3,currentPriceString)
    cryptoSheet.write(z,4,trillion7priceString)
    cryptoSheet.write(z,5,trillion36priceString)
    cryptoSheet.write(z,6,trillion73priceString)
    cryptoSheet.write(z,7,trillion90priceString)
    cryptoSheet.write(z,8,trillion217priceString)
    cryptoSheet.write(z,9,trillion544priceString)
    z+=1

# print out the table
cryptoWorkbook.close()
