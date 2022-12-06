import requests
import json
import datetime
# from pytz import timezone
from config_data import symbol_list, api_key


def get_stock_data(symbol=symbol_list[0], outputsize='compact', freq='1min'):
    # url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=3CRDRNRW5333VLKA'
    url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={}&outputsize={}&interval={}&apikey={}".format(
        symbol, outputsize, freq, api_key)
    r = requests.get(url)
    # stock_data = r.json()

    if r.status_code == 200:
        raw_dataset = json.loads(r.content)
        try:
            stock_data = raw_dataset['Time Series (1min)']
            metadata = raw_dataset['Meta Data']

        except KeyError:
            print(raw_dataset)
            exit()

        timezone = metadata['6. Time Zone']

        data = {'symbol': 'symbol',
                'time': 'time',
                '1. open': 'open',
                '2. high': 'high',
                '3. low': 'low',
                '4. close': 'close',
                '5. volume': 'volume'}

        for k, v in stock_data.items():
            v.update({'symbol': symbol, 'time': k})

        stock_data = dict((key, dict((data[k], v) for (k, v) in value.items())) for (key, value) in stock_data.items())
        value = list(stock_data.values())
        print('Get {}\'s full length intraday data.'.format(symbol))



    # if request failed, return a fake data point
    else:
        timezone = timeZone
        print('  Failed: Cannot get {}\'s data at {}:{} '.format(symbol, datetime.datetime.now(timezone(timezone)),
                                                                 r.status_code))
        value = {"symbol": 'None',
                 "time": 'None',
                 "open": 0.,
                 "high": 0.,
                 "low": 0.,
                 "close": 0.,
                 "volume": 0.}

    return value, timezone


if __name__ == '__main__':
    print(get_stock_data())