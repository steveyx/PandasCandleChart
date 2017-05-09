# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 15:51:07 2016

@author: Steve 
"""


import pandas as pd

import matplotlib.pyplot as plt
from   matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates

def parseYMDHMS(timestamps):
    return pd.datetime.strptime(timestamps,"%Y-%m-%d %H:%M:%S")

def plot_candlestick(df, ax=None, fmt="%Y-%m-%d %H:%M"):
    if ax is None:
        ax = plt.subplot(1, 1, 1)
    idx_name = df.index.name
    dat = df.reset_index()[[idx_name, "Open", "High", "Low", "Close"]]
    dat[df.index.name] = dat[df.index.name].map(mdates.date2num)
    ax.xaxis_date()
    ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))
    ax.autoscale_view()
    plt.xticks(rotation=30)
    _ = candlestick_ohlc(ax, dat.values, width=.001, colorup='g', alpha =1)
    ax.set_title("EURUSD 5 Minutes Candle Stick Chart",fontsize=28)
    ax.set_xlabel(idx_name,fontsize=20)
    ax.set_ylabel("EURUSD",fontsize=20)
    ax.grid()
    plt.subplots_adjust(left=0.1, right=0.9, top=0.859, bottom=0.15)
    #plt.show()
    return ax

if __name__== "__main__":
    
    df = pd.read_csv("EURUSD_Week20161226.csv", parse_dates=['DateTime'],
                         date_parser=parseYMDHMS, header=0)
    df.rename(columns={'Buyopen': 'Open', 'Buyhigh': 'High',
                       'Buylow': 'Low', 'Buyclose': 'Close',
                       'DateTime': 'Time'}, inplace=True)                   
    df = df.set_index('Time')    
    plot_candlestick(df, ax=None, fmt="%Y-%m-%d %H:%M")
