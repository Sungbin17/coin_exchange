upbit_symbol_list = ['EOS', 'TRX', 'ADA', 'BTC', 'ETH', 'XRP', 'BCC', 'STORM', 'ZIL',
                     'ZIL', 'ICX', 'GRS', 'SC', 'QTUM', 'XLM', 'SNT', 'NEO', 'GNT',
                     'GTO', 'ONT', 'ETC', 'STEEM', 'SBD', 'TIX', 'REP', 'OMG', 'MER',
                     'BTG', 'EMC2', 'IGNIS', 'ARDR', 'LTC', 'XMR', 'POWR', 'DCR', 'XEM',
                     'STRAT', 'STORJ', 'MTL', 'KMD', 'PIVX', 'MCO', 'WAVES', 'ZEC', 'LSK',
                     'DASH', 'ARK', 'VTC']


binance_symbol_list = ['ETH', 'LTC', 'BNB', 'NEO', 'BCC', 'GAS', 'HSR', 'MCO', 'WTC', 'LRC', 'QTU', 'YOY', 'OMG', 'ZRX', 'STR', 'SNG', 'BQX', 'KNC', 'FUN', 'SNM', 'IOT', 'LIN', 'XVG', 'SAL', 'MDA', 'MTL', 'SUB', 'EOS', 'SNT', 'ETC', 'MTH', 'ENG', 'DNT', 'ZEC', 'BNT', 'AST', 'DAS', 'OAX', 'ICN', 'BTG', 'EVX', 'REQ', 'VIB', 'TRX', 'POW', 'ARK', 'XRP', 'MOD', 'ENJ', 'STO', 'VEN', 'KMD', 'RCN', 'NUL', 'RDN', 'XMR', 'DLT', 'AMB', 'BAT', 'BCP', 'ARN', 'GVT', 'CDT', 'GXS', 'POE', 'QSP', 'BTS', 'XZC', 'LSK', 'TNT', 'FUE', 'MAN', 'BCD', 'DGD', 'ADX', 'ADA', 'PPT', 'CMT', 'XLM', 'CND', 'LEN', 'WAB', 'TNB', 'WAV', 'GTO', 'ICX', 'OST', 'ELF', 'AIO', 'NEB', 'BRD', 'EDO', 'WIN', 'NAV', 'LUN', 'TRI', 'APP', 'VIB', 'RLC', 'INS', 'PIV', 'IOS', 'CHA', 'STE', 'NAN', 'VIA', 'BLZ', 'AEB', 'RPX', 'NCA', 'POA', 'ZIL', 'ONT', 'STO', 'XEM', 'WAN', 'WPR', 'QLC', 'SYS', 'GRS', 'CLO', 'GNT', 'LOO', 'BCN', 'REP', 'TUS', 'ZEN', 'SKY', 'CVC', 'THE', 'BTC']

common =[]

for i in upbit_symbol_list:
    for a in binance_symbol_list:
        if i == a:
            common.append(i)
        else:
            pass
    print(common)
