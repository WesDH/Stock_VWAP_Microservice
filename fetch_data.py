import os
import requests
from dotenv import load_dotenv
import pandas as pd
from variables import *


def fetch_data():
    # load in environment variables from .env
    load_dotenv()
    API_KEY = os.getenv("API_KEY")

    # Step 2: Define API endpoint
    BASE_URL = "https://www.alphavantage.co/query"
    for stock_ticker in stock_tickers:
        params = {
            "function": "TIME_SERIES_DAILY",   # daily time series data
            "symbol": stock_ticker,                  # Can be any stock symbol
            "apikey": API_KEY,
            "outputsize": "compact",           # compact = last 100 days
            "datatype": "json",
        }

        # Make API request
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        # Parse JSON and convert to pandas DataFrame
        if "Time Series (Daily)" in data:
            time_series = data["Time Series (Daily)"]
            df = pd.DataFrame.from_dict(time_series, orient="index")
            df.index.name = "Date"
            df = df.rename(columns=lambda x: x[3:].strip())    # Remove '1. ', '2.
            df = df.sort_index(ascending=False)
            df = df.head(35)                                   # keep the last 35 days only

            # Save to CSV
            os.makedirs("data", exist_ok=True)
            df.to_csv("data/{}_stock_data.csv".format(stock_ticker))
            print("Data saved to data/{}_stock_data.csv".format(stock_ticker))

        else:
            print("Error fetching data:")
            print(data.get("Note") or data.get("Error Message") or data)

if __name__ == "__main__":
    fetch_data()