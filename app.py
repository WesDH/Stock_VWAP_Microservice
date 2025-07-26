from flask import Flask
import pandas as pd
from variables import *

from time import sleep
app = Flask(__name__)

@app.route("/")
@app.route("/vwap")
def default_route():
    html_string = ""
    for stock_name in stock_tickers:
        df = pd.read_csv("data/{}_vwap.csv".format(stock_name))
        html_string += "\n\n<h1>{}</h1>\n".format(stock_name)
        for index, row in df.iterrows():
            html_string += f"<h3>{row['Date']} -- 30 day VWAP from this date: ${row['vwap']}</h3>\n"
    return html_string


print("Starting app...")


# start app
app.run(debug=True)