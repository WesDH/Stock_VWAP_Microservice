import pandas as pd
from variables import *
"""
  Calculates MONTHLY volume-weighted average price (VWAP)
  The VWAP can be calculated for different timeframes,
  such as intraday, daily, weekly, or monthly, depending on the needs of the trader
  """

# variables needed by csv:
# high, low, close, volume for past 30 days

# variables calculated here:
# typical_price, price_x_volume,
# summation_of_typical_price_x_volume,
# summation_of_volume,
#


def calc_vwap():
    for ticker in stock_tickers:
        df = pd.read_csv("data/{}_stock_data.csv".format(ticker))

        """ Below is calculated for each trading  day """
        # typical_price = (high + low + close) / 3
        # price_x_volume = typical_price * volume
        df["typical_price"] = (df["high"] * df["low"] + df["close"]) / df["low"]
        df["price_x_volume"] = df["typical_price"]  * df["volume"]

        """ Summations for 30 days """
        # Summation of: price_x_volume for past 30 days
        # Summation of: volume for past 30 days

        """ Calculate 30 day VWAP """
        #vwap = summation_of_price_x_volume / summation_of_volume
        df['vwap'] = pd.Series(dtype='float')  # fill values with NaN

        # Iterate over the first 5 rows,
        # For a particular day, calculating monthly VWAP on that day requires 30 days of previous data
        # Since we pulled the past 35 days of data, only the 5 most recent days can look back 30 days
        for idx, row in df.iloc[:5].iterrows():
            print(f"Index: {idx}, Col1: {row['Date']}, Col2: {row['typical_price']}")
            #df["vwap"] = df["price_x_volume"] / df["price_x_volume"]
            summation_price_x_vol = df.loc[idx : idx+29, 'price_x_volume'].sum()
            summation_vol = df.loc[idx : idx+29, 'volume'].sum()
            df.at[idx, "vwap"] = summation_price_x_vol / summation_vol

        vwap_df = df[['Date', 'vwap']]
        vwap_df = vwap_df.dropna()
        vwap_df.to_csv("data/{}_vwap.csv".format(ticker), index=False)
        print("Wrote VWAP to {}_vwap.csv...".format(ticker))

if __name__ == "__main__":
    calc_vwap()