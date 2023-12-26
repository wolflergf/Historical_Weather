from typing import Dict
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

stations = pd.read_csv("./data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home() -> str:
    """
    Return the home page.
    """
    return render_template("home.html", data=stations.to_html())


@app.route("/api/v1/<station>/<date>")
def api(station: str, date: str) -> Dict[str, str]:
    """
    Return the temperature for a given station and date.

    Parameters:
    station (str): The station ID
    date (str): The date in YYYYMMDD format

    Returns:
    dict: A dictionary containing the station ID, date, and temperature
    """
    df = pd.read_csv(
        "./data_small/TG_STAID{}.txt".format(station.zfill(6)),
        skiprows=20,
        parse_dates=["    DATE"],
    )
    temperature = df.loc[df["    DATE"] == date]["   TG"].values[0] / 10
    return {"station": station, "date": date, "temperature": str(temperature)}


@app.route("/api/v1/<definition>/")
def api_definition(definition: str) -> Dict[str, str]:
    """
    Return the definition of a given word.

    Parameters:
    definition (str): The word to define

    Returns:
    dict: A dictionary containing the word and its definition
    """
    word = definition
    df = pd.read_csv("./dictionary/dictionary.csv", sep=",")
    definition = df.loc[df["word"] == definition]["definition"].values[0]
    return {
        "definition": definition,
        "word": word,
    }


if __name__ == "__main__":
    app.run(debug=True)
