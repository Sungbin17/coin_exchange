import urllib.request, json
from urllib.request import Request, urlopen


BINANCE_UPBIT = ['BTC', 'ETH', 'BCC', 'NEO', 'LTC', 'ADA', 'XRP']




def get_response(api):
    response = Request(api, headers={'User-Agent': 'Mozilla/5.0'})
    data = json.loads(urlopen(response).read())
    return data


def get_all_api(symbol):
    UPBIT_api = 'https://crix-api-endpoint.upbit.com/v1/crix/candles/minutes/60?code=CRIX.UPBIT.USDT-' + symbol
    BINANCE_api = 'https://api.binance.com/api/v1/ticker/price?symbol=' + symbol + 'USDT'
    list = [UPBIT_api, BINANCE_api]
    return list


def get_all_price(list):
    UPBIT_api = list[0]
    BINANCE_api = list[1]
    UPBIT_price = float(get_response(UPBIT_api)[0].get('tradePrice'))
    BINANCE_price = float(get_response(BINANCE_api).get('price'))
    price_list = [UPBIT_price, BINANCE_price]
    return price_list


def top_margin(price_list):
    sorted_list = sorted(price_list)
    profit = sorted_list[-1] - sorted_list[0]
    profit_percentage = (profit / sorted_list[0]) * 100
    return profit_percentage


def calciulate_trade(symbol):
    api = get_all_api(symbol)
    price = get_all_price(api)
    top_margins = top_margin(price)
    percentage_list.append(top_margins)
    print(percentage_list)
    sorted_percentage_list = sorted(percentage_list)
    return sorted_percentage_list


percentage_list = []

for symbol in BINANCE_UPBIT:
    a = calciulate_trade(symbol)
    print(a)
