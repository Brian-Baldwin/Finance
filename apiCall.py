from tracemalloc import start
import requests
import json
import calendar
import datetime
from dateutil.rrule import rrule, MONTHLY


#Setting constant variables
#text = open("apikey.txt", "r")
#apiKey = text.read()
apiKey = ""
startDate = "2021-01-29"
#startDate = input("Enter start year and month (YYYY-MM): ")

#Take today's date, 
today = datetime.date.today()
first = today.replace(day=1)
endDate = first - datetime.timedelta(days=1)
endDate = endDate.strftime("%Y-%m")

#If month has a leading zero, it is removed and then the last business day of that month is found
if endDate[5] == "0":
    endDate = endDate[:5] + endDate[6:7]
    lastBus = max(calendar.monthcalendar(int(endDate[:4]), int(endDate[5:6]))[-1:][0][:5])
else:
    lastBus = max(calendar.monthcalendar(int(endDate[:4]), int(endDate[5:7]))[-1:][0][:5])
#dates = [dt for dt in rrule(MONTHLY, dtstart=startDate, until=endDate)]


#Call API and store data in JSON format
def apiCall(ticker):
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol='
    r = requests.get(base_url + ticker + "&apikey=" + apiKey)
    data = r.text
    parse_json = json.loads(data)
    return parse_json


#Parse price from saved JSON
def parsePrice(date, parsedJSON):
    return parsedJSON['Monthly Adjusted Time Series'][date]['5. adjusted close']


#Compare two adjusted security prices
def individualPerformance(ticker, start, monthList):
    None


