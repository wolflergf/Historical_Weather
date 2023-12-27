""" A simple Flask application that returns the temperature for a given station and date. """ ""
# Import necessary libraries
from typing import Dict
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

# Initialize Flask application
app = Flask(__name__)

# Load station data from file and select relevant columns
stations = pd.read_csv("./data_small/stations.txt", skiprows=17)
stations = stations[["STAID", "STANAME                                 "]]


@app.route("/")
def home() -> str:
    """
    Return the home page.
    """
    # Render the home page with station data
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
    # Load temperature data for the specified station
    df = pd.read_csv(
        "./data_small/TG_STAID{}.txt".format(station.zfill(6)),
        skiprows=20,
        parse_dates=["    DATE"],
    )
    # Find the temperature for the specified date
    temperature = df.loc[df["    DATE"] == date]["   TG"].values[0] / 10
    # Return the data as a dictionary
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
    # Save the word for later use
    word = definition
    # Load the dictionary data
    df = pd.read_csv("./dictionary/dictionary.csv", sep=",")
    # Find the definition for the specified word
    definition = df.loc[df["word"] == definition]["definition"].values[0]
    # Return the word and its definition as a dictionary
    return {
        "definition": definition,
        "word": word,
    }


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)
