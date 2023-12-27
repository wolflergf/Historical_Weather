# Temperature and Definition API

This is a simple Flask application that provides two APIs:

1. An API that returns the temperature for a given station and date.
2. An API that returns the definition of a given word.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/wolflergf/Historical_Weather.git
   ```
2. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python main.py
   ```
2. Visit `http://localhost:5000` in your web browser to see the home page.
3. Use the `/api/v1/<station>/<date>` endpoint to get the temperature for a given station and date. Replace `<station>` with the station ID and `<date>` with the date in YYYYMMDD format.
4. Use the `/api/v1/<definition>/` endpoint to get the definition of a given word. Replace `<definition>` with the word you want to define.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
