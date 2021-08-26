#Samuel Bryant
#
#Simple program to display trending cryptocurrency data over the past 50 days.
#User will be prompted to enter stock name, and if valid, matplotlib chart
#will be displayed.

import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import datetime


def get_stock_data():
    '''
    Asks the user for a stock and gets the dates and prices for said stock
    over a period of 500 days, and returns the data to main for later use
    '''
    stock_name = ""
    flag = ""
    while flag == "":

        stock_name = input("Please enter stock name: ")
        coin = yf.Ticker(stock_name)
        coin_history = coin.history(period="500d")
        coin_data = coin_history.reset_index()

        #Use this for debugging stock data
        #print(coin_data)

        if coin_data.empty:
            print("Invalid Stock")
        else:
            flag = "valid"


    coin_prices = []
    for price in coin_data["Close"]:
        #use for debugging
        #print(price)
        coin_prices.append(price)

    coin_dates = []
    for close_date in coin_data["Date"]:
        #use for debugging
        #print(close_date)
        coin_dates.append(close_date)

    #If necessary, user can print the date and coin prices to the console
    '''
    for k,v in coin.info.items():
        if k == "regularMarketPrice":
            print("{} {}".format(k,v))
    '''
    coin_price = coin.info["regularMarketPrice"]
    #use console output to cross-reference stock price just in case
    print("Todays price for " + stock_name, "is $" + str(coin_price))

    return stock_name,coin_prices,coin_dates

def create_plot(stock_name,coin_dates,coin_prices):

    '''
    create_plot will take the data from get_stock_data function and make
    a plot based upon this data and display it for the user.
    '''

    current_time = datetime.datetime.now()
    plt.rcParams['toolbar'] = 'None'

    #use for debugging
    #print(current_time)

    fig = plt.figure(figsize = (9,5))
    ax = fig.add_subplot()
    ax.set_xlabel("DATE")
    ax.set_ylabel("PRICE")
    plt.title(stock_name)
    fig.set_facecolor('grey')

    plt.plot(coin_prices,coin_dates,marker=".", markersize=7, color = "indigo")
    plt_axis = plt.gca()
    plt_axis.set_facecolor("darkgrey")

    plt.show()

def main():

    stock,coins,dates = get_stock_data()
    create_plot(stock,coins,dates)

main()
