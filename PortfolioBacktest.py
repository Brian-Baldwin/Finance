from tracemalloc import start
import requests
import json
import calendar
import datetime as dt
from dateutil.rrule import rrule, MONTHLY
import holidays
apiKey = ""


#Find last business day of either the previous month or the current month depending on arguments
def lastBusiness(inputDate, prev=True):
    if prev:
        first = inputDate.replace(day=1)
        inputDate = first - dt.timedelta(days=1)
    lastBus =  max(calendar.monthcalendar(inputDate.year, inputDate.month)[-1:][0][:5])
    inputDate = inputDate.replace(day=lastBus)
    return inputDate


'''
#Creates a list of the months between the start and end dates
def listOfMonths(start, end):
    monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=end)]
'''


def individualPerformance(ticker, start, end, apiKey):
    #Call API and store data in JSON format
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol='
    r = requests.get(base_url + ticker + "&apikey=" + apiKey)
    data = r.text
    parsedJSON = json.loads(data)
    #monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=end)].strftime("%Y-%m-%d")

    #Parse price from saved JSON and store in list
    '''priceList = ['']*len(monthList)
    for i in range(len(monthList)):
        priceList[i] = parsedJSON['Monthly Adjusted Time Series'][monthList[i]]['5. adjusted close']

    #Compare two adjusted security prices
    monthlyPerformance = ['']*(len(priceList)-1)
    for i in range(len(priceList)-1):
        monthlyPerformance[i] = priceList[i+1] / priceList[i]'''
    startPrice = parsedJSON['Monthly Adjusted Time Series'][start]['5. adjusted close']
    endPrice = parsedJSON['Monthly Adjusted Time Series'][end]['5. adjusted close']
    return float(endPrice) / float(startPrice)


def backtest(start, apiKey, tickers, allocations):
    lastDate = lastBusiness(dt.date.today(), True)
    #monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=last)]


if __name__ == "__main__":
    #Setting constant variables
    #text = open("apikey.txt", "r")
    #apiKey = text.read()
    startDate = dt.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), '%Y-%m-%d')
    startDate = lastBusiness(startDate, prev=False).strftime('%Y-%m-%d')
    endDate = dt.date.today()
    endDate = lastBusiness(endDate, prev=True)
    endDate = endDate.strftime("%Y-%m-%d")
    ticker = input("Enter a ticker:")
    print(individualPerformance(ticker, startDate, endDate, apiKey))

