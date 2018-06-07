import urllib.request, json
from urllib.request import Request, urlopen
import numpy as np
import time

BITHUMB_BINANCE = ['EOS', 'XRP', 'XMR', 'BTG', 'MCO', 'VEN', 'KNC', 'TRX', 'GTO', 'ICX', 'LRC', 'ZIL',
                   'ELF', 'OMG', 'LTC', 'HSR', 'ZEC', 'ETC', 'GNT']

# binance_api = 'https://api.binance.com/api/v1/ticker/price?symbol=' + symbol + 'ETH'
#
# bithumb_api = 'https://api.bithumb.com/public/ticker/' + symbol.lower()
#

def get_coin_price(coin):
    bithumb_coin_sell_price_api = 'https://api.bithumb.com/public/ticker/' + coin
    response = Request(bithumb_coin_sell_price_api, headers={'User-Agent': 'Mozilla/5.0'})
    coin_price_won = json.loads(urlopen(response).read()).get('data').get('sell_price')
    return coin_price_won

def get_coin_price_binance(coin):
    binance_api = 'https://api.binance.com/api/v1/ticker/price?symbol=' + coin + 'ETH'
    response = Request(binance_api, headers={'User-Agent': 'Mozilla/5.0'})
    coin_price_eth = json.loads(urlopen(response).read()).get('price')
    return coin_price_eth

def get_price_in_eth(coin_price_won):
    # 특정 거래소에서 특정 코인의 가격을 이더로 알려주는 함수
    coin_price_eth = float(coin_price_won) / float(get_coin_price('eth'))
    return coin_price_eth



def exchange_price():
    # binance 와 빗썸의 특정 코인 가격을 이더 기준으로 비교 해줌
    bithumb_coins = []
    binance_coins = []
    gap = []
    for coin in BITHUMB_BINANCE:
        bithumb_coin_price_won = get_coin_price(coin)
        coin_price_eth = float(get_price_in_eth(bithumb_coin_price_won))
        bithumb_coins.append({coin:coin_price_eth})
        binance_coin_price = float(get_coin_price_binance(coin))
        binance_coins.append({coin:binance_coin_price})
        gap.append({coin: coin_price_eth-binance_coin_price})
    return bithumb_coins, binance_coins, gap





def check_profit_available(gap):
    profitable_list=[]
    # 거래소간의 차익이 최소 0.001ETH가 넘는 지 체크해주는 함수
    for i in gap:
        value = float(sorted(i.values())[0])
        rounded_value = round(value, 3)
        if rounded_value >= 0.001:
            profitable_list.append(sorted(i.keys())[0])
    print(profitable_list)
    return profitable_list




def profit_algorithm(profitable_list, bithumb_coins, binance_coins):
    # 거래 했을 때 차익이 0.001ETH가 넘는 지 체크하고 예상 수익이 얼마인지 알려주는 함수
    for coin in profitable_list:
        for bithumb_coin in bithumb_coins:
            if sorted(bithumb_coin.keys())[0] == coin:
                bithumb_value =sorted(bithumb_coin.values())[0]
        for binance_coin in binance_coins:
            if sorted(binance_coin.keys())[0] == coin:
                binance_value = sorted(binance_coin.values())[0]
        profit = (bithumb_value - binance_value) * 27.1 - 0.6
        print(profit)



while True:
    try:
        profit_algorithm(check_profit_available(exchange_price()[2]), exchange_price()[0], exchange_price()[1])
        time.sleep(1)
    except:
        pass
        time.sleep(1)
