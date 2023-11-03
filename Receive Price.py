import requests
from bs4 import BeautifulSoup

def trading_instruments():
    trading_instruments_req = requests.get('https://www.litefinance.org/fa/trading/trading-instruments/')
    trading_instruments_soup = BeautifulSoup(trading_instruments_req.content,"html.parser")
    separate = trading_instruments_soup.find_all("td",attrs={"data-symbol":"XAUUSD"})
    instruments_list = []
    for i in separate:
        job = i.text
        instruments_list.append(job)
    return instruments_list

trading_instruments()