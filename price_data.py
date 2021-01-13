from bs4 import BeautifulSoup 
import requests

def get_price(coin):
  coins = ["bitcoin", "ethereum", "aave", "maker", "yearn-finance", "sushiswap", "uniswap"] # Informative (and redundant) list.

  url = "https://coinmarketcap.com/currencies/" + coin
  HTML = requests.get(url)
  soup = BeautifulSoup(HTML.text, 'html.parser')

  price = soup.find("div", {'class':'priceValue___11gHJ'}).text

  return(price + " ")