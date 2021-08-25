

import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import datetime


def intialize_ticker():
    stock_name = ""
    flag = ""
    while flag == "":

    #stock_name = "AMC"
        stock_name = input("Please enter stock name: ")
        btc = yf.Ticker(stock_name)
        btc_history = btc.history(period="50d")
        btc_data = btc_history.reset_index()
        print(btc_data)
        if btc_data.empty:
            print("Invalid Stock")
        else:
            flag = "valid"



    #print(btc_data.Close.to_string(index=False))
    btc_prices = []
    for price in btc_data["Close"]:
        print(price)
        btc_prices.append(price)

    btc_dates = []
    for close_date in btc_data["Date"]:
        print(close_date)
        btc_dates.append(close_date)

    for k,v in btc.info.items():
        if k == "regularMarketPrice":
            print("{} {}".format(k,v))

    btc_price = btc.info["regularMarketPrice"]
    print(btc_price)

    current_time = datetime.datetime.now()
    plt.rcParams['toolbar'] = 'None'
    print(current_time)
    fig = plt.figure(figsize = (9,5))
    plt.title(stock_name)
    fig.set_facecolor('darkviolet')
    #input_area = fig.add_axes([0.1,0.05,0.8,0.075])
    #text_input = TextBox(input_area,"Enter Stock")
    #text_input.on_submit(intialize_ticker)

    #plt.rcParams['figure.facecolor']='red'
    #plt.rcParams['savefig.facecolor']='red'
    plt.plot(btc_dates,btc_prices,marker=".", markersize=10)
    plt_axis = plt.gca()
    plt_axis.set_facecolor("Indigo")


    #plt.set_facecolor("Indigo")

    plt.show()

def main():


    intialize_ticker()


main()
