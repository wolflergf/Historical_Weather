from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/api/v1/<station>/<date>")
def api(station, date):
    temperature = 23
    return {
        "station": station,
        "date": date,
        "temperature": temperature
    }

if __name__ == '__main__':
    app.run(debug=True)