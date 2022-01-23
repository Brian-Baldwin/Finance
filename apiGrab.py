import requests
import json


def grab(ticker, date, api_key):
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol='
    r = requests.get(base_url + ticker + api_key)
    data = r.text
    parse_json = json.loads(data)
    return parse_json['Monthly Adjusted Time Series'][date]['1. open']