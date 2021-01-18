from pycoingecko import CoinGeckoAPI
import requests
import json
import re

def get_gas_price():
	url = "https://etherchain.org/api/gasPriceOracle"
	response = requests.get(url).text

	gas = re.findall(r'\d+(?:\.\d+)?', response)
	return(gas[1])

def get_price(coin):
	cg = CoinGeckoAPI()

	if coin.startswith("0x"):
		price = cg.get_token_price('ethereum', coin, 'usd')
		for key in price:
   			return("$" + str(price[key]['usd']))
	else:
		price = re.findall(r'\d+', json.dumps(cg.get_price(coin, 'usd')))
		return("$" + str(price[0]))