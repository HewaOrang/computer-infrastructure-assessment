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
timestamp = now.strftime("%Y%m%d-%H%M%S")

# File name.
filename= "/data/" + timestamp + '.csv'
# Ensure 'data' directory exists
os.makedirs("data", exist_ok=True)

# File name.
filename = os.path.join("data", now.strftime("%Y%m%d-%H%M%S") + '.csv')

# Save data as csv.
df.to_csv(filename)

# Create new figure and axis.
# Use the same timestamp for the plot title.
ax.set_title(f'Plot date: {timestamp}')
df['Close'].plot(ax=ax)

# Current date and time.
now =  dt.datetime.now()
ax.set_title(f'Plot date: {now.strftime("%Y%m%d-%H%M%S")}')

# Add axis labels.
ax.set_xlabel("Date")
# File name.
filename= "/plots/" + timestamp + '.png'
# Add legend.
ax.legend(loc='upper right')

# Ensure 'plots' directory exists
os.makedirs("plots", exist_ok=True)

# File name.
filename = os.path.join("plots", now.strftime("%Y%m%d-%H%M%S") + '.png')

# Save figure.
fig.savefig(filename, dpi=300)
