import requests
import time


def get_bitcoin_value():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data["bitcoin"]["usd"]
    else:
        print(f"Failed.")
        return None


def main():
    values = []
    minute = 60 # in seconds
    ten_minutes = 10
    current_minute = 0

    try:
        while True:
            # Get Bitcoin price
            bitcoin_value = get_bitcoin_value()
            if bitcoin_value is not None:

                print(f"Bitcoin value is: ${bitcoin_value}")
                values.append(bitcoin_value)# Add the price to the list
                current_minute += 1
                if current_minute == ten_minutes:
                    # Calculate and print the average
                    average_price = sum(values) / len(values)

                    print(f"The average value bitcoin over the last 10 minutes: ${average_price}")

                    prices = []
                    current_minute = 0

            time.sleep(minute)
    finally:
        print(f"Done.")

if __name__ == "__main__":
    main()
