import urllib.request, json
from urllib.request import Request, urlopen

huobi_symbol_api = 'https://api.huobipro.com/v1/common/symbols'

response = Request(huobi_symbol_api, headers={'User-Agent': 'Mozilla/5.0'})

data = json.loads(urlopen(response).read())

data = data.get('data')

print(type(data))

['BTC', 'BCH', 'ETH', 'ETC', 'LTC', 'EOS', 'XRP', 'OMG', 'DASH', 'ZEC', 'ADA', 'STEEM', 'IOTA', 'SOC', 'CTXC', 'ACT', 'BTM', 'BTS', 'ONT', 'IOST', 'HT', 'TRX', 'DTA', 'NEO', 'QTUM', 'SMT', 'ELA', 'VEN', 'THETA', 'SNT', 'ZIL', 'XEM', 'NAS', 'RUFF', 'HSR', 'LET', 'MDS', 'STORJ', 'ELF', 'ITC', 'CVC', 'GNT', 'BCH', 'ETH', 'LTC', 'ETC', 'EOS', 'OMG', 'XRP', 'DASH', 'ZEC', 'ADA', 'STEEM', 'IOTA', 'POLY', 'KAN', 'LBA', 'WAN', 'BFT', 'BTM', 'ONT', 'IOST', 'HT', 'TRX', 'SMT', 'ELA', 'WICC', 'OCN', 'ZLA', 'ABT', 'MTX', 'NAS', 'VEN', 'DTA', 'NEO', 'WAX', 'BTS', 'ZIL', 'THETA', 'CTXC', 'SRN', 'XEM', 'ICX', 'DGD', 'CHAT', 'WPR', 'LUN', 'SWFTC', 'SNT', 'MEET', 'YEE', 'ELF', 'LET', 'QTUM', 'LSK', 'ITC', 'SOC', 'QASH', 'MDS', 'EKO', 'TOPC', 'MTN', 'ACT', 'HSR', 'STK', 'STORJ', 'GNX', 'DBC', 'SNC', 'CMT', 'TNB', 'RUFF', 'QUN', 'ZRX', 'KNC', 'BLZ', 'PROPY', 'RPX', 'APPC', 'AIDOC', 'POWR', 'CVC', 'PAY', 'QSP', 'DAT', 'RDN', 'MCO', 'RCN', 'MANA', 'UTK', 'TNT', 'GAS', 'BAT', 'OST', 'LINK', 'GNT', 'MTL', 'EVX', 'REQ', 'ADX', 'AST', 'ENG', 'SALT', 'EDU', 'BIFI', 'BCX', 'BCD', 'SBTC', 'BTG', 'EOS', 'OMG', 'IOTA', 'ADA', 'STEEM', 'POLY', 'KAN', 'LBA', 'WAN', 'BFT', 'ZRX', 'AST', 'KNC', 'ONT', 'HT', 'BTM', 'IOST', 'SMT', 'ELA', 'TRX', 'ABT', 'NAS', 'OCN', 'WICC', 'ZIL', 'CTXC', 'ZLA', 'WPR', 'DTA', 'MTX', 'THETA', 'SRN', 'VEN', 'BTS', 'WAX', 'HSR', 'ICX', 'MTN', 'ACT', 'BLZ', 'QASH', 'RUFF', 'CMT', 'ELF', 'MEET', 'SOC', 'QTUM', 'ITC', 'SWFTC', 'YEE', 'LSK', 'LUN', 'LET', 'GNX', 'CHAT', 'EKO', 'TOPC', 'DGD', 'STK', 'MDS', 'DBC', 'SNC', 'PAY', 'QUN', 'AIDOC', 'TNB', 'APPC', 'RDN', 'UTK', 'POWR', 'BAT', 'PROPY', 'MANA', 'REQ', 'CVC', 'QSP', 'EVX', 'DAT', 'MCO', 'GNT', 'GAS', 'OST', 'LINK', 'RCN', 'TNT', 'ENG', 'SALT', 'ADX', 'EDU']




for base_currency in data:
    base_currency_list.append(base_currency.get('base-currency').upper())

print(base_currency_list)



