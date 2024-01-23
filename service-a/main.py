import requests
import time
from flask import Flask, jsonify

app = Flask(__name__)
values = []
bitcoin_value = 0

def calculate_bitcoin_value():
    global bitcoin_value
    global values
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        bitcoin_value = data["bitcoin"]["usd"]
        values.append(bitcoin_value)  # Add the price to the list
        return bitcoin_value
    else:
        print("Failed to retrieve Bitcoin value.")
        return None

def av_bitcoin_value():
    global values
    return sum(values) / len(values)

@app.route('/bitcoin_value', methods=['GET'])
def get_bitcoin():
    global bitcoin_value
    current_bitcoin_value = calculate_bitcoin_value()
    return jsonify({"bitcoin_value": current_bitcoin_value})

@app.route('/average_bitcoin_value', methods=['GET'])
def get_average_bitcoin():
    global values
    if len(values) == 10:
        return jsonify({"average_bitcoin_value": av_bitcoin_value()})

    else:
        return jsonify({"average_bitcoin_value": "No data available"})


def main():
    minute = 60  # in seconds
    current_minute = 0
    global bitcoin_value
    global values
    try:
        while True:
            # Get Bitcoin price
            bitcoin_value = calculate_bitcoin_value()

            if bitcoin_value is not None:
                print(f"Bitcoin value is: ${bitcoin_value}")

                current_minute += 1
                if current_minute == 10:
                    # Calculate and print the average
                    if len(values) > 0:
                        average_price = av_bitcoin_value()
                        print(f"The average value of Bitcoin over the last 10 minutes: ${average_price}")
                        values.clear()  # Clear the list for the next 10 minutes

                    current_minute = 0

            time.sleep(minute)

    except KeyboardInterrupt:
        print("Script terminated by user.")
    finally:
        print("Done.")

if __name__ == "__main__":
    main()
    app.run(debug=True)
