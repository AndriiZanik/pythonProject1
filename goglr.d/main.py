import requests
from bs4 import BeautifulSoup

HOST = 'https://p2p.binance.com/'
# URL = 'https://p2p.binance.com/ru-UA/trade/'
URL = 'https://p2p.binance.com/ru-UA/trade/all-payments/USDT?fiat=USD'
#URL = 'https://p2p.binance.com/ru-UA/trade/Revolut/USDT?fiat=USD'

HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

def get_html(url,params = ''):
    r = requests.get(url,headers=HEADERS,params = params)
    return r

def get_content(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('div', class_='css-cjwhpx' )
    #print(soup.prettify())
    cards = []
    print(items)
    with open('index.html', 'w') as file:
        file.write(''.join(list(map(str,items))))


html = get_html(URL)
# print(html.text)
get_content(html.text)











#
# fiat = input('Enter fiat:').upper()
# bank = input('Enter bank:')
# r = requests.get(f'https://p2p.binance.com/ru-UA/trade/{bank}/USDT?fiat={fiat}')
# r.encoding = 'utf-8' # Optional: requests infers this internally
# print(r.status_code)
# print(r.headers)
#
# `

import time
from selenium import webdriver
# import requests
#
# def get_data(url):
#     headers = {
#             'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
#         }
#     r = requests.get(url = url,headers=headers)
#     #print(r.text)
#     print(type(r.text))
#     with open('index.html','w') as file:
#         file.write(str(r.text))
#
#
# def main():
#     url = "https://p2p.binance.com/ru-UA/trade/all-payments/USDT?fiat=USD"
#     get_data(url)
#
# if __name__ == '__main__':
#     main()