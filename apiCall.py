import requests
import json
import calendar
import datetime
from dateutil.rrule import rrule, MONTHLY



text = open("apikey.txt", "r")
apiKey = text.read()
startDate = "2021-01"
#startDate = input("Enter start year and month (YYYY-MM): ")
today = datetime.date.today()
first = today.replace(day=1)
endDate = first - datetime.timedelta(days=1)
endDate = endDate.strftime("%Y-%m")
#dates = [dt for dt in rrule(MONTHLY, dtstart=startDate, until=endDate)]

def apiCall(ticker, date):
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol='
    r = requests.get(base_url + ticker + "&apikey=" + apiKey)
    data = r.text
    parse_json = json.loads(data)
    return parse_json['Monthly Adjusted Time Series'][date]['5. adjusted close']


def individualPerformance(ticker, start, monthList):
    None


print(apiCall("AAPL", "2022-01-31"))