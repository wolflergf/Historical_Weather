from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    df = pd.read_csv("./data_small/TG_STAID{}.txt".format(station.zfill(6)), skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df["    DATE"] == date]["   TG"].values[0] / 10
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

@app.route("/api/v1/<definition>/")
def api_definition(definition):
    return {
        "definition": definition.upper(),
        "word": definition,
    }


if __name__ == '__main__':
    app.run(debug=True)