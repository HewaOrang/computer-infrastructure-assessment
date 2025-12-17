#!/usr/bin/env python

# Uses the system’s default Python interpreter (Unix/Linux shebang)
# https://docs.python.org/3/using/unix.html#shebang-lines

# Operating system interfaces.
import os

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
ax.set_title(f'Plot date: {now.strftime("%Y%m%d-%H%M%S")}')

# Add axis labels.
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")

# Add legend.
ax.legend(loc='upper right')

# File name.
filename = "./plots/" + now.strftime("%Y%m%d-%H%M%S") + '.png'

# Save figure.
fig.savefig(filename, dpi=300)
