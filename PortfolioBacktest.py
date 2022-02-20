from tracemalloc import start
import requests
import json
import calendar
import datetime as dt
from dateutil.rrule import rrule, MONTHLY
import holidays

apiKey = ""


# Find last business day of either the previous month or the current month depending on arguments
def lastBusiness(inputDate: dt, prev=True):
    if prev:
        first = inputDate.replace(day=1)
        inputDate = first - dt.timedelta(days=1)
    lastBus = max(calendar.monthcalendar(inputDate.year, inputDate.month)[-1:][0][:5])
    inputDate = inputDate.replace(day=lastBus)
    return inputDate


'''
#Creates a list of the months between the start and end dates
#For month list to work properly, each date needs to be changed to the last business day in their respective month
def listOfMonths(start: dt, end: dt):
    monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=end)]
'''


def stockPerformance(ticker: str, start, end, apiKey: str):
    # Call API and store data in JSON format
    base_url = 'https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol='
    r = requests.get(base_url + ticker + "&apikey=" + apiKey)
    data = r.text
    parsedJSON = json.loads(data)
    # monthList = [dt for dt in rrule(MONTHLY, dtstart=start, until=end)].strftime("%Y-%m-%d")

    # Parse price from saved JSON and store in list
    '''priceList = ['']*len(monthList)
    for i in range(len(monthList)):
        priceList[i] = parsedJSON['Monthly Adjusted Time Series'][monthList[i]]['5. adjusted close']


    monthlyPerformance = ['']*(len(priceList)-1)
    for i in range(len(priceList)-1):
        monthlyPerformance[i] = priceList[i+1] / priceList[i]'''
    # Compare two adjusted security prices
    startPrice = parsedJSON['Monthly Adjusted Time Series'][start]['5. adjusted close']
    endPrice = parsedJSON['Monthly Adjusted Time Series'][end]['5. adjusted close']
    return float(endPrice) / float(startPrice)


# Calculate the total performance of a given portfolio between the start and end dates
def portfolioPerformance(start, end, apiKey: str, tickers: list, allocations: list):
    performance = 0
    for i in range(len(tickers)):
        performance += stockPerformance(tickers[i], start, end, apiKey) * float(allocations[i])
    return performance - 100


def bench(start, end, apiKey: str, benchmark: str):
    return stockPerformance(benchmark, start, end, apiKey) * 100 - 100


def backtest(start, end, apiKey: str, tickers: list, allocations: list, benchmark: str):
    portPerf = portfolioPerformance(start, end, apiKey, tickers, allocations)
    benchPerf = bench(start, end, apiKey, benchmark)
    return portPerf, benchPerf
    #print("From " + str(start) + " until " + str(end) + " your portfolio had a return of " + str(portfolioPerformance(start, end, apiKey, tickers, allocations)) + " %")
    #print("Over the same period of time, your benchmark had a return of " + str(bench(start, end, apiKey, benchmark)) + "%")


if __name__ == "__main__":
    # Setting constant variables
    # text = open("apikey.txt", "r")
    # apiKey = text.read()
    startDate = dt.datetime.strptime(input("Enter start date (YYYY-MM-DD): "), '%Y-%m-%d')
    startDate = lastBusiness(startDate, prev=False).strftime('%Y-%m-%d')
    endDate = lastBusiness(dt.date.today(), prev=True)
    endDate = endDate.strftime("%Y-%m-%d")
    numberOfTickers = int(input("How many different stocks are in your portfolio?: "))
    if numberOfTickers == 1:
        allocations = [100]
    else:
        allocations = [''] * numberOfTickers
    tickerList = [''] * numberOfTickers
    for i in range(numberOfTickers):
        tickerList[i] = input("Enter ticker number " + str(i + 1) + ": ")
        if numberOfTickers == 1:
            break
        else:
            allocations[i] = input("Enter the percent allocation of " + tickerList[i] + ": ")
    benchmark = input("What is your benchmark ticker?: ")
    perfs = backtest(startDate, endDate, apiKey, tickerList, allocations, benchmark)
    print("From " + str(startDate) + " until " + str(endDate) + " your portfolio had a return of " + str(perfs[0]) + " %")
    print("Over the same period of time, your benchmark had a return of " + str(perfs[1]) + "%")

