from flask import Flask
import pandas as pd
from fetch_data import fetch_data
from calculate_vwap import calc_vwap
from time import sleep
app = Flask(__name__)

@app.route("/")
def default_route():
    df = pd.read_csv("data/AAPL_vwap.csv")
    html_string = "<h1>AAPL</h1>\n"
    for index, row in df.iterrows():
        html_string += f"<h3>{row['Date']} -- 30 day VWAP from this date: ${row['vwap']}</h3>\n"
    return html_string


print("Starting app...")

# TODO: Below needs to run in a scheduler, if in a loop it locks the app since its single threaded
fetch_data()
calc_vwap()

# start app
app.run(debug=True)