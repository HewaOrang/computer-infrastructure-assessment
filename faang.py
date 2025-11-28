#!/usr/bin/env python

# Dates and times.
import datetime as dt

# Yahoo Finance data.
import yfinance as yf

# Plotting.
import matplotlib.pyplot as plt

# Get data.
df = yf.download(['META', 'AAPL', 'AMZN', 'NFLX', 'GOOG',], period='5d', interval='1h')

# Current date and time.
now =  dt.datetime.now()

# File name.
filename= "./data/" + now.strftime("%Y%m%d-%H%M%S") + '.csv'

# Save data as csv.
df.to_csv(filename)

# Create new figure and axis.
fig, ax = plt.subplots()

# Plot all closing pieces.
df['Close'].plot(ax=ax)

# Current date and time.
now =  dt.datetime.now()

# File name.
filename= "./plots/" + now.strftime("%Y%m%d-%H%M%S") + '.png'

# Save figure.
fig.savefig(filename, dpi=300)
