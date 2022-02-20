from tracemalloc import start
import requests
import json
import calendar
import datetime as dt
from dateutil.rrule import rrule, MONTHLY
import holidays
apiKey = ""


# Take today's date and finds the previous month
def lastMonth():
    today = dt.date.today()
    first = today.replace(day=1)
    endMonth = first - dt.timedelta(days=1)
    endMonth = endMonth.strftime("%Y-%m")
    return endMonth


# Find the last business day of the previous month.
def lastBusiness(inputDate):
    first = inputDate.replace(day=1)
    inputDate = first - dt.timedelta(days=1)
    lastBus = max(calendar.monthcalendar(inputDate.year, inputDate.month)[-1:][0][:5])
    inputDate = inputDate.replace(day=lastBus)
    return inputDate

'''
#Creates a list of the months between the start and end dates
def listOfMonths(start, end):
    monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=end)]
'''


def individualPerformance(ticker, start, end, apiKey, priceList):
    #Call API and store data in JSON format
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol='
    r = requests.get(base_url + ticker + "&apikey=" + apiKey)
    data = r.text
    parsedJSON = json.loads(data)
    monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=end)]

    #Parse price from saved JSON and store in list
    priceList = ['']*len(monthList)
    for i in range(len(monthList)):
        priceList[i] = parsedJSON['Monthly Adjusted Time Series'][monthList[i]]['5. adjusted close']

    #Compare two adjusted security prices
    monthlyPerformance = ['']*(len(priceList)-1)
    for i in range(len(priceList)-1):
        monthlyPerformance[i] = priceList[i+1] / priceList[i]


def backtest(start, apiKey):
    last = lastBusiness(dt.date.today())
    monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=last)]

'''
if __name__ == "__main__":
    #Setting constant variables
    text = open("apikey.txt", "r")
    apiKey = text.read()
    startDate = lastBusiness(input("Enter start date (YYYY-MM-DD): "))
    print(backtest(startDate, apiKey))'''


indate = dt.date(2021, 10, 31)
print(lastBusiness(indate))